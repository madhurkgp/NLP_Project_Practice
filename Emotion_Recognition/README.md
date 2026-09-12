# Emotion Recognition System

An advanced AI-powered web application for detecting emotions from audio files using machine learning and deep neural networks.

## 🎯 Project Overview

This emotion recognition system analyzes audio recordings to identify human emotions using state-of-the-art machine learning techniques. The application features a modern, responsive web interface built with Django and provides real-time emotion detection capabilities.

## 🚀 Features

- **Real-time Audio Processing**: Advanced audio feature extraction using MFCC, chroma, and mel spectrograms
- **Neural Network Classification**: Multi-layer perceptron classifier trained on the RAVDESS dataset
- **Modern Web Interface**: Beautiful, responsive UI with gradient designs and smooth animations
- **Multiple Emotion Detection**: Identifies 8 different emotions: neutral, calm, happy, sad, angry, fearful, disgust, surprised
- **Drag & Drop Upload**: Intuitive file upload interface with drag-and-drop support
- **Privacy Secure**: All processing happens locally with no external API calls

## 🛠️ Technology Stack

### Backend
- **Django 3.2**: Web framework for the application backend
- **Python 3.8+**: Core programming language
- **scikit-learn 0.24.2**: Machine learning library for the MLP classifier
- **librosa 0.8.1**: Audio analysis and feature extraction
- **numpy 1.21.5**: Numerical computations and array operations
- **soundfile 0.10.3**: Audio file reading and processing
- **pickle**: Model serialization and storage

### Frontend
- **HTML5 & CSS3**: Modern web standards with responsive design
- **JavaScript**: Interactive UI elements and file handling
- **Font Awesome 6.0**: Professional icon library
- **Google Fonts (Inter)**: Modern typography
- **CSS Animations**: Smooth transitions and micro-interactions

### Dataset
- **RAVDESS Dataset**: Ryerson Audio-Visual Database of Emotional Speech and Song
- **1440 Audio Files**: Professional actors portraying 8 different emotions
- **High Quality**: 48kHz sample rate, 16-bit resolution

## 📊 Model Architecture

### Feature Extraction
- **MFCC (Mel-frequency cepstral coefficients)**: 40 coefficients capturing timbral characteristics
- **Chroma Features**: 12-dimensional pitch class profiles
- **Mel Spectrograms**: Frequency domain representation
- **Total Features**: 180-dimensional feature vector per audio sample

### Neural Network
- **Architecture**: Multi-layer Perceptron (MLP)
- **Hidden Layers**: 300 neurons with ReLU activation
- **Training Parameters**:
  - Learning rate: Adaptive
  - Batch size: 256
  - Max iterations: 500
  - Alpha (L2 regularization): 0.01
  - Epsilon: 1e-08

### Performance Metrics
- **Training Accuracy**: ~82.6%
- **Test Accuracy**: ~71.9%
- **Emotions Detected**: 4 primary emotions (calm, happy, fearful, disgust)

## 🏗️ Project Structure

```
Emotion_Recognition/
├── Code/
│   └── mysite/
│       ├── manage.py                 # Django management script
│       ├── requirements.txt          # Python dependencies
│       ├── db.sqlite3               # SQLite database
│       ├── mysite/                  # Django project settings
│       │   ├── settings.py
│       │   ├── urls.py
│       │   └── wsgi.py
│       └── polls/                   # Main application
│           ├── views.py             # Main application logic
│           ├── models.py            # Database models
│           ├── forms.py             # Django forms
│           ├── urls.py              # URL routing
│           ├── templates/           # HTML templates
│           │   ├── index.html       # Main page
│           │   └── upload.html      # Upload page
│           ├── sustain.py           # Model loading and caching
│           └── emotion_classification-model.pkl  # Trained model
├── emotion-dataset/                 # RAVDESS dataset files
└── README.md                        # This documentation
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git (for cloning)

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd Emotion_Recognition/Code/mysite
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix/MacOS
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Database Migration
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Run the Application
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## 🎵 Usage Guide

### 1. Upload Audio File
- Navigate to the main page
- Click "Upload Audio File" button
- Select an audio file (WAV, MP3, FLAC, M4A, OGG formats supported)
- Optionally provide a recording name

### 2. Emotion Analysis
- After upload, the system automatically processes the audio
- Features are extracted using librosa
- The neural network predicts the emotion
- Results are displayed with appropriate icons and animations

### 3. Supported Emotions
The system detects the following emotions:
- 😊 **Happy**: Joy, pleasure, contentment
- 😌 **Calm**: Peaceful, relaxed, serene
- 😨 **Fearful**: Scared, anxious, worried
- 🤢 **Disgust**: Repulsed, nauseated
- 😢 **Sad**: Sorrow, grief, disappointment
- 😠 **Angry**: Frustrated, irritated, enraged
- 😮 **Surprised**: Astonished, amazed
- 😐 **Neutral**: No strong emotion

## 🔧 Configuration

### Model Settings
The model can be retrained or fine-tuned by modifying the training parameters in the notebook:
- Hidden layer sizes
- Learning rate
- Batch size
- Number of iterations

### Audio Processing
Audio processing parameters can be adjusted in `views.py`:
- Sample rate
- MFCC coefficients count
- Feature extraction methods

## 📈 Performance Optimization

### Caching
The trained model is cached using Django's cache framework for faster loading and reduced memory usage.

### File Handling
Audio files are stored in the `polls/my_data/` directory and automatically cleaned up after processing.

### Database
Uses SQLite for simplicity, but can be easily migrated to PostgreSQL or MySQL for production use.

## 🐛 Troubleshooting

### Common Issues

1. **Model Loading Error**
   - Ensure the `emotion_classification-model.pkl` file exists in `polls/` directory
   - Check that all required dependencies are installed

2. **Audio Processing Error**
   - Verify audio file format is supported
   - Check that the audio file is not corrupted
   - Ensure librosa and soundfile are properly installed

3. **Django Server Issues**
   - Check if port 8000 is available
   - Verify virtual environment is activated
   - Ensure all migrations are applied

### Debug Mode
Set `DEBUG = True` in `settings.py` for detailed error messages and debugging information.

## 🔒 Security Considerations

- File uploads are restricted to audio formats only
- CSRF protection is enabled for all forms
- Media files are served securely in development
- No external API calls for privacy protection

## 🚀 Deployment

### Production Setup
1. Set `DEBUG = False` in settings.py
2. Configure proper database (PostgreSQL recommended)
3. Set up static file serving (Nginx/Apache)
4. Configure SSL certificate
5. Set up environment variables for sensitive data

### Docker Deployment
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **RAVDESS Dataset**: Provided by Ryerson University
- **Librosa Team**: For excellent audio processing library
- **Scikit-learn**: For robust machine learning tools
- **Django**: For the powerful web framework

## 📞 Contact

For questions, suggestions, or issues, please create an issue in the repository or contact the development team.

---

**Note**: This system is designed for research and educational purposes. For production use, additional validation and testing may be required.
