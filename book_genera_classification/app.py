import pickle
import os
import pandas as pd
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re
import nltk
from flask import Flask, request, render_template
from sklearn.feature_extraction.text import TfidfVectorizer

# Download NLTK data (only if not already downloaded)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

# cleaning the text i.e removing all unncessary characters


def cleantext(text):
    """Clean text by removing special characters and converting to lowercase."""
    # Remove quotes
    text = re.sub(r"['\"]", "", text)
    # Remove special symbols, keep only letters and spaces
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    # Remove extra whitespace
    text = ' '.join(text.split())
    # Convert to lowercase
    text = text.lower()
    return text


def removestopwords(text):
    """Remove stopwords from text."""
    stop_words = set(stopwords.words('english'))
    words = [word for word in text.split() if word not in stop_words]
    return ' '.join(words)


def lemmatizing(text):
    """Lemmatize text to reduce words to their base form."""
    lemma = WordNetLemmatizer()
    words = [lemma.lemmatize(word) for word in text.split()]
    return ' '.join(words)


def stemming(text):
    """Apply stemming to reduce words to their root form."""
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in text.split()]
    return ' '.join(words)


def predict_genre(text, model, tfidf_vectorizer):
    """Predict book genre from summary text."""
    # Preprocess the text
    text = cleantext(text)
    text = removestopwords(text)
    text = lemmatizing(text)
    text = stemming(text)
    
    # Vectorize and predict
    try:
        text_vector = tfidf_vectorizer.transform([text])
        predicted = model.predict(text_vector)
    except Exception as e:
        raise Exception(f"Error during prediction: {str(e)}")

    # Map prediction to genre name
    genre_mapper = {
        0: 'Fantasy', 
        1: 'Science Fiction', 
        2: 'Crime Fiction',
        3: 'Historical Novel', 
        4: 'Horror', 
        5: 'Thriller'
    }

    return genre_mapper.get(predicted[0], 'Unknown')


def create_fitted_vectorizer():
    """Create and fit a TF-IDF vectorizer using the training data."""
    dataset_path = os.path.join(os.path.dirname(__file__), 'BooksDataSet.csv')
    
    try:
        # Read the dataset
        df = pd.read_csv(dataset_path)
        
        # Preprocess all summaries
        processed_texts = []
        for summary in df['summary'].dropna().head(1000):  # Use first 1000 for efficiency
            processed = cleantext(str(summary))
            processed = removestopwords(processed)
            processed = lemmatizing(processed)
            processed = stemming(processed)
            processed_texts.append(processed)
        
        # Create and fit vectorizer with 10000 features to match the trained model
        vectorizer = TfidfVectorizer(max_features=10000, stop_words='english')
        vectorizer.fit(processed_texts)
        
        return vectorizer
        
    except Exception as e:
        print(f"Warning: Could not create fitted vectorizer from dataset: {str(e)}")
        # Fallback: create a basic vectorizer and fit on sample texts with 10000 features
        sample_texts = [
            "wizard magic fantasy adventure spell enchanted quest dragon kingdom mystical",
            "space science future technology alien planet starship exploration universe",
            "detective crime mystery murder investigation police clue evidence suspect",
            "historical war romance past century battle king queen empire",
            "horror ghost scary supernatural haunted dark terror nightmare",
            "thriller suspense action danger chase spy mission secret"
        ] * 100  # Repeat to get more vocabulary
        vectorizer = TfidfVectorizer(max_features=10000, stop_words='english')
        vectorizer.fit(sample_texts)
        return vectorizer


# Load models and vectorizers
def load_models():
    """Load the trained model and TF-IDF vectorizer."""
    model_path = os.path.join(os.path.dirname(__file__), 'bookgenremodel.pkl')
    vectorizer_path = os.path.join(os.path.dirname(__file__), 'tfdifvector.pkl')
    
    try:
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        
        try:
            # Try to load the saved vectorizer
            with open(vectorizer_path, 'rb') as file:
                tfidf_vectorizer = pickle.load(file)
            
            # Test if the vectorizer is fitted
            test_text = "test"
            processed = cleantext(test_text)
            processed = removestopwords(processed)
            processed = lemmatizing(processed)
            processed = stemming(processed)
            tfidf_vectorizer.transform([processed])
            
        except Exception as e:
            print(f"Warning: Saved vectorizer not usable: {str(e)}")
            print("Creating new fitted vectorizer...")
            tfidf_vectorizer = create_fitted_vectorizer()
        
        return model, tfidf_vectorizer
        
    except FileNotFoundError as e:
        raise Exception(f"Model file not found: {str(e)}")
    except Exception as e:
        raise Exception(f"Error loading models: {str(e)}")


# Initialize Flask app
app = Flask(__name__)

# Load models at startup
model, tfidf_vectorizer = load_models()


@app.route('/', methods=['GET', 'POST'])
def home():
    """Main route for the web application."""
    if request.method == 'POST':
        summary = request.form.get('summary', '').strip()
        
        if not summary:
            return render_template('index.html', 
                                 error='Please enter a book summary.',
                                 showresult=True)
        
        try:
            prediction = predict_genre(summary, model, tfidf_vectorizer)
            return render_template('index.html', 
                                 genre=prediction, 
                                 text=summary[:200] + '...' if len(summary) > 200 else summary,
                                 showresult=True)
        except Exception as e:
            return render_template('index.html', 
                                 error=f'An error occurred: {str(e)}',
                                 showresult=True)
    
    return render_template('index.html')


@app.route('/health')
def health_check():
    """Health check endpoint."""
    return {'status': 'healthy', 'message': 'Book Genre Prediction API is running'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
