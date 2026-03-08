# Keyword Extraction Application

A Django-based web application that extracts keywords from text using TF-IDF (Term Frequency-Inverse Document Frequency) and Natural Language Processing techniques.

## 🚀 Features

- **Text Processing**: Advanced text preprocessing including lowercase conversion, tag removal, special character elimination, and lemmatization
- **Stopword Removal**: Custom stopwords filtering including domain-specific terms
- **TF-IDF Algorithm**: Uses scikit-learn's TF-IDF vectorization for keyword extraction
- **Web Interface**: Clean, responsive web interface for text input and keyword display
- **Pre-trained Models**: Includes pre-trained vectorizer and TF-IDF models for immediate use

## 📁 Project Structure

```
keyword_extraction/
├── code/
│   ├── Keyword_Extraction.ipynb    # Jupyter notebook with model training code
│   └── mysite/                     # Django web application
│       ├── manage.py               # Django management script
│       ├── requirements.txt        # Python dependencies
│       ├── mysite/                 # Django project configuration
│       │   ├── settings.py
│       │   ├── urls.py
│       │   └── wsgi.py
│       └── polls/                  # Django app
│           ├── views.py            # Main application logic
│           ├── urls.py             # URL routing
│           ├── models.py           # Database models
│           ├── templates/
│           │   └── index.html     # Web interface template
│           ├── sustain.py          # Model caching utilities
│           └── *.pkl               # Pre-trained model files
└── dataset/                         # Training dataset (if available)
```

## 🛠️ Technology Stack

- **Backend**: Django 3.2
- **Machine Learning**: scikit-learn 1.0.2
- **Natural Language Processing**: NLTK 3.6.7
- **Frontend**: HTML, CSS
- **Database**: SQLite (default)

## 📋 Requirements

- Python 3.8+
- pip package manager

## 🚀 Installation and Setup

### 1. Clone the Repository
```bash
cd keyword_extraction/code/mysite
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Development Server
```bash
python manage.py runserver
```

### 4. Access the Application
Open your web browser and navigate to: `http://127.0.0.1:8000/`

## 🔧 Usage

1. **Open the Web Interface**: Navigate to the application URL in your browser
2. **Enter Text**: Type or paste the text you want to analyze in the input field
3. **Submit**: Click the "Submit" button to extract keywords
4. **View Results**: The extracted keywords will be displayed below the input field

## 📊 Model Details

### Text Preprocessing Pipeline
1. **Lowercase Conversion**: Converts all text to lowercase
2. **Tag Removal**: Removes HTML/XML tags
3. **Special Character Removal**: Eliminates digits and special characters
4. **Stopword Filtering**: Removes common English words and custom stopwords
5. **Length Filtering**: Removes words shorter than 3 characters
6. **Lemmatization**: Reduces words to their base form using WordNet lemmatizer

### TF-IDF Configuration
- **Max Document Frequency**: 85% (ignores words appearing in 85% of documents)
- **Max Features**: 1500 (vocabulary size)
- **N-gram Range**: (1,3) (includes unigrams, bigrams, and trigrams)
- **Top Keywords**: Returns top 10 keywords per document

### Custom Stopwords
The application uses an extended stopwords list including:
- Standard NLTK English stopwords
- Domain-specific terms: "fig", "figure", "image", "sample", "using", "show", "result", "large", "also", "one", "two", "three", "four", "five", "seven", "eight", "nine"

## 🏗️ Architecture

### Django Application Structure
- **views.py**: Contains the main keyword extraction logic and HTTP request handling
- **sustain.py**: Implements model caching for performance optimization
- **templates/index.html**: Frontend interface with responsive design
- **urls.py**: URL routing configuration

### Model Files
- `keywords-count-vectorizer.pkl`: Pre-trained CountVectorizer for text vectorization
- `keywords-tfidf-model.pkl`: Pre-trained TF-IDF transformer
- `keywords-feature-names.pkl`: Feature names vocabulary

## 🎨 Web Interface

The application features a clean, modern interface with:
- Gradient background design
- Responsive layout
- Text input field with placeholder
- Submit button with hover effects
- Keyword results display as a bulleted list

## 🔍 Example Usage

**Input Text:**
```
Neural networks are powerful machine learning models that can learn complex patterns from data. 
Deep learning architectures like convolutional neural networks have revolutionized computer vision 
and natural language processing tasks.
```

**Extracted Keywords:**
- neural (0.45)
- networks (0.38)
- learning (0.32)
- models (0.28)
- data (0.25)
- patterns (0.22)
- convolutional (0.19)
- vision (0.17)
- processing (0.15)
- architectures (0.13)

## 🐛 Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: Ensure all dependencies are installed via `pip install -r requirements.txt`
2. **Server Not Starting**: Check if port 8000 is available or use a different port: `python manage.py runserver 8080`
3. **Model Loading Errors**: Verify that all `.pkl` files are present in the `polls/` directory

### Performance Optimization

The application uses Django's caching framework to optimize model loading:
- Models are cached after first load
- Subsequent requests use cached models for faster response times

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the MIT License.

## 🔮 Future Enhancements

- Support for multiple languages
- Advanced keyword ranking algorithms
- Batch text processing
- Export functionality (CSV, JSON)
- User authentication and history
- API endpoints for integration
- Real-time keyword extraction
- Custom keyword filtering
- Integration with external NLP services

## 📞 Support

For questions, issues, or contributions, please refer to the project documentation or create an issue in the repository.
