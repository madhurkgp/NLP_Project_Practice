# 📚 Book Genre Prediction

An AI-powered web application that predicts book genres based on plot summaries using machine learning and natural language processing.

![Book Genre Prediction](https://img.shields.io/badge/Genre-Prediction-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🌟 Features

- **AI-Powered Analysis**: Uses machine learning to analyze book summaries
- **6 Genre Categories**: Predicts from Fantasy, Science Fiction, Crime Fiction, Historical Novel, Horror, and Thriller
- **Modern UI**: Clean, responsive interface with smooth animations
- **Real-time Processing**: Instant genre predictions
- **Character Counter**: Track your summary length as you type
- **Error Handling**: Graceful error messages and validation
- **Mobile Friendly**: Works perfectly on all devices

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd book_genera_classification
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:8080`

## 📋 Supported Genres

The application can predict the following book genres:

| Genre | Description |
|-------|-------------|
| 🧙‍♂️ Fantasy | Magic, mythical creatures, and imaginary worlds |
| 🚀 Science Fiction | Future technology, space, and scientific concepts |
| 🔍 Crime Fiction | Mysteries, detectives, and criminal investigations |
| 📜 Historical Novel | Stories set in historical periods |
| 👻 Horror | Supernatural and frightening content |
| ⚡ Thriller | Suspenseful and exciting plots |

## 🛠️ Technology Stack

- **Backend**: Flask 2.3.3
- **Machine Learning**: Scikit-learn 1.3.2
- **Text Processing**: NLTK 3.8.1
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: Bootstrap 5.3.0
- **Icons**: Font Awesome 6.4.0
- **Fonts**: Google Fonts (Inter)

## 📊 Model Details

The application uses a machine learning pipeline that includes:

1. **Text Preprocessing**:
   - Cleaning and removing special characters
   - Stop word removal
   - Lemmatization
   - Stemming

2. **Feature Extraction**:
   - TF-IDF Vectorization

3. **Classification**:
   - Pre-trained model saved as `bookgenremodel.pkl`
   - TF-IDF vectorizer saved as `tfdifvector.pkl`

## 📁 Project Structure

```
book_genera_classification/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── bookgenremodel.pkl     # Trained ML model
├── tfdifvector.pkl        # TF-IDF vectorizer
├── BooksDataSet.csv       # Training dataset
├── templates/
│   └── index.html        # Frontend template
└── README.md             # This file
```

## 🎯 How to Use

1. **Enter a Book Summary**: Type or paste a book summary in the text area
2. **Click Predict**: Press the "Predict Genre" button
3. **View Results**: See the predicted genre with a confidence badge
4. **Summary Preview**: Review a preview of your entered summary

## 🔧 Configuration

### Environment Variables

You can configure the application using environment variables:

```bash
export FLASK_ENV=development  # Enable debug mode
export FLASK_PORT=8080        # Change port (default: 8080)
```

### Customization

- **Port**: Modify the port in `app.py` (line 142)
- **Host**: Change the host in `app.py` (default: 0.0.0.0)
- **Genres**: Update the genre mapping in the `predict_genre` function

## 🐛 Troubleshooting

### Common Issues

1. **Port already in use**:
   ```bash
   # Kill the process using the port
   # On Windows
   netstat -ano | findstr :8080
   taskkill /PID <PID> /F
   
   # On macOS/Linux
   lsof -ti:8080 | xargs kill -9
   ```

2. **NLTK data not found**:
   The application automatically downloads required NLTK data on first run.

3. **Model file not found**:
   Ensure `bookgenremodel.pkl` and `tfdifvector.pkl` are in the same directory as `app.py`.

4. **Dependencies not installed**:
   ```bash
   pip install -r requirements.txt
   ```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 API Endpoints

### GET `/`
Returns the main web interface.

### POST `/`
Accepts a book summary and returns genre prediction.

**Request Body**:
```
summary: <book_summary_text>
```

### GET `/health`
Health check endpoint.

**Response**:
```json
{
  "status": "healthy",
  "message": "Book Genre Prediction API is running"
}
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **CMU Book Summary Dataset**: For providing the training data
- **Scikit-learn**: For the machine learning framework
- **NLTK**: For natural language processing tools
- **Flask**: For the web framework
- **Bootstrap**: For the responsive UI components

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Search existing [Issues](../../issues)
3. Create a new issue with detailed information

## 🔄 Updates

### Version 1.0.0
- Initial release with basic genre prediction
- Modern responsive UI
- Error handling and validation
- Character counter
- Health check endpoint

---

**Made with ❤️ using Python and Flask**

Enjoy predicting book genres! 📚✨
