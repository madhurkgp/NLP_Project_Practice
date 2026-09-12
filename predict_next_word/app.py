from flask import Flask, render_template, request
import numpy as np
import pickle
import os

app = Flask(__name__)

# Global variables for model and tokenizer
model = None
tokenizer = None

def load_model_and_tokenizer():
    """Load model and tokenizer on demand"""
    global model, tokenizer
    if model is None or tokenizer is None:
        try:
            from tensorflow.keras.preprocessing.sequence import pad_sequences
            from tensorflow.keras.models import load_model
            
            model_path = os.path.join(os.path.dirname(__file__), 'nextWord.h5')
            tokenizer_path = os.path.join(os.path.dirname(__file__), 'tokenizer.pkl')
            
            print("Loading model and tokenizer...")
            model = load_model(model_path)
            tokenizer = pickle.load(open(tokenizer_path, 'rb'))
            print("Model and tokenizer loaded successfully!")
            return True
        except Exception as e:
            print(f"Error loading model: {e}")
            return False
    return True

def generate_seq(model, tokenizer, seq_length, seed_text, n_words):
    """Generate next words based on input text"""
    from tensorflow.keras.preprocessing.sequence import pad_sequences
    
    result = list()
    in_text = seed_text
    
    for _ in range(n_words):
        # encode the text as integer
        encoded = tokenizer.texts_to_sequences([in_text])[0]
        # truncate sequences to a fixed length
        encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')
        # predict probabilities for each word
        predict_x = model.predict(encoded, verbose=0)
        yhat = np.argmax(predict_x, axis=1)
        # map predicted word index to word
        out_word = ''
        for word, index in tokenizer.word_index.items():
            if index == yhat:
                out_word = word
                break
        # append to input
        in_text += ' ' + out_word
        result.append(out_word)
    return ' '.join(result)

@app.route('/')
def home():
    """Render the home page"""
    return render_template('index.html', response="")

@app.route('/predict', methods=['POST'])
def predict():
    """Handle prediction request"""
    response = "Input the word first"
    
    if request.method == 'POST':
        text = request.form['Name']
        if text.strip():
            try:
                if load_model_and_tokenizer():
                    seq_length = 50
                    res_length = 12  # predict next 12 words
                    generated = generate_seq(model, tokenizer, seq_length, text, res_length)
                    response = generated
                else:
                    response = "Error: Could not load the ML model. Please check TensorFlow installation."
            except Exception as e:
                response = f"Error: {str(e)}"
        else:
            response = "Please enter some text"
    
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
