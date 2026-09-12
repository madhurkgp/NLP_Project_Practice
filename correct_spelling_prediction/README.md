# Spelling Correction Application

A comprehensive spelling correction system that suggests corrections for misspelled words using advanced NLP techniques. This project includes both a standalone Python script and a Django web application.

## 🚀 Features

- **Intelligent Spelling Correction**: Uses edit distance algorithms to generate spelling suggestions
- **Dual Interface**: Both command-line and web-based interfaces
- **Probability-Based Rankings**: Suggestions are ranked by statistical probability
- **Multi-Level Editing**: Supports one-letter and two-letter edit operations
- **Modern Web UI**: Clean, responsive web interface with gradient design
- **Pre-trained Models**: Includes pre-trained vocabulary and probability models

## 📁 Project Structure

```
correct_spelling_prediction/
├── README.md                          # This file
├── spelling_corrector.py              # Standalone Python application
├── requirements.txt                   # Python dependencies
├── dataset/                           # Training data
│   └── papers.csv                     # Research papers dataset
└── code/                             # Django web application
    └── mysite/
        ├── manage.py                  # Django management script
        ├── requirements.txt           # Django dependencies
        ├── mysite/                   # Django project settings
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        └── polls/                    # Django app
            ├── views.py               # Main application logic
            ├── models.py              # Database models
            ├── urls.py                # URL routing
            ├── templates/
            │   └── index.html         # Web interface template
            ├── string_manipulation.py # String processing functions
            ├── sustain.py             # Model loading utilities
            ├── vocab-spellings.pkl    # Vocabulary model
            └── word-probability-spellings.pkl # Probability model
```

## 🛠️ Technologies & Libraries Used

### Core NLP Libraries
- **NLTK (Natural Language Toolkit)**: Text preprocessing, tokenization, stopwords removal, and lemmatization
- **Pandas**: Data manipulation and processing of the training dataset
- **NumPy**: Numerical operations and array handling
- **Scikit-learn**: Machine learning utilities and data preprocessing

### Web Development
- **Django 3.2**: Web framework for the application interface
- **HTML5/CSS3**: Modern, responsive frontend design
- **JavaScript**: Enhanced user interactions

### Data Processing
- **Pickle**: Model serialization and persistence
- **Regex (re)**: Pattern matching and text cleaning
- **Collections**: Counter for word frequency analysis

### Development Tools
- **Python 3.7+**: Core programming language
- **Jupyter Notebook**: Original development and experimentation
- **SQLite**: Database backend for Django

## 📋 Installation & Setup

### Option 1: Standalone Python Application

1. **Clone or download the project**
   ```bash
   cd correct_spelling_prediction
   ```

2. **Install Python dependencies**
   ```bash
   pip install nltk pandas numpy scikit-learn
   ```

3. **Run the standalone application**
   ```bash
   python spelling_corrector.py
   ```

### Option 2: Django Web Application

1. **Navigate to the Django project**
   ```bash
   cd code/mysite
   ```

2. **Install Django dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

4. **Start the development server**
   ```bash
   python manage.py runserver
   ```

5. **Open in browser**
   ```
   http://127.0.0.1:8000/
   ```

## 🧠 How It Works

### 1. Data Preprocessing
- **Text Cleaning**: Removes HTML tags, special characters, and digits
- **Lowercase Conversion**: Standardizes text to lowercase
- **Stopword Removal**: Eliminates common words (articles, prepositions, etc.)
- **Lemmatization**: Reduces words to their base form using WordNetLemmatizer
- **Length Filtering**: Removes words shorter than 3 characters

### 2. Model Training
- **Vocabulary Building**: Creates a set of unique words from processed text
- **Probability Calculation**: Computes word frequencies and probabilities
- **Model Persistence**: Saves vocabulary and probability models using pickle

### 3. Spelling Correction Algorithm
The system uses a multi-step approach:

#### Edit Operations
- **Delete Letter**: Removes one character at each position
- **Switch Letter**: Swaps adjacent characters
- **Replace Letter**: Replaces each character with all alphabet letters
- **Insert Letter**: Inserts all alphabet letters at each position

#### Suggestion Generation
1. **Direct Match**: Checks if word exists in vocabulary
2. **One-Edit Suggestions**: Generates all possible one-letter edits
3. **Two-Edit Suggestions**: Generates all possible two-letter edits (if needed)
4. **Probability Ranking**: Ranks suggestions by statistical probability

## 🎯 Usage Examples

### Standalone Application
```python
# Interactive mode
python spelling_corrector.py

# Programmatic usage
from spelling_corrector import SpellingCorrector

corrector = SpellingCorrector()
suggestions = corrector.get_corrections("propose", n=5)
print(suggestions)
# Output: [('propose', 0.000376), ('proposed', 0.000829), ...]
```

### Web Application
1. Open the web interface
2. Enter a word in the input field
3. Click "Check Spelling"
4. View ranked suggestions with probabilities

## 📊 Performance & Accuracy

- **Vocabulary Size**: ~90,000 unique words (trained on research papers)
- **Edit Distance**: Supports up to 2-letter edits for comprehensive coverage
- **Response Time**: < 1 second for typical queries
- **Accuracy**: High precision for common misspellings

## 🔧 Configuration

### Custom Dataset
To train with your own dataset:
1. Place your CSV file in the `dataset/` directory
2. Ensure it has a `paper_text` column containing text data
3. Update the `data_path` parameter in `SpellingCorrector` initialization

### Model Retraining
```python
corrector = SpellingCorrector()
corrector._train_model()  # Force retraining
```

## 🐛 Troubleshooting

### Common Issues

1. **NLTK Data Missing**
   ```bash
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
   ```

2. **Model Files Not Found**
   - The application will automatically train new models if `.pkl` files are missing
   - Ensure `dataset/papers.csv` exists for training

3. **Django Server Not Starting**
   ```bash
   # Check Python version (3.7+ required)
   python --version
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

4. **Memory Issues**
   - Reduce dataset size in `_train_model()` method
   - Use smaller vocabulary for testing

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is open source and available under the MIT License.

## 🔮 Future Enhancements

- **Context-Aware Correction**: Consider surrounding words for better suggestions
- **Multiple Language Support**: Extend to other languages
- **Machine Learning Integration**: Use neural networks for improved accuracy
- **API Development**: RESTful API for integration with other applications
- **Performance Optimization**: Implement caching and indexing for faster responses

## 📞 Support

For questions, issues, or contributions:
- Create an issue in the project repository
- Check the troubleshooting section above
- Review the code comments for detailed explanations

---

**Note**: This project was originally developed as part of an NLP practice series and has been enhanced for production use with improved error handling, modern UI, and comprehensive documentation.
