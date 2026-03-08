# DNA Classification for E.Coli Detection

A Django web application that uses machine learning to predict E.Coli presence from DNA sequences.

## Overview

This project implements a DNA sequence classification system that can detect whether a given DNA sequence contains E.Coli promoter genes. The system uses a Multi-Layer Perceptron (MLP) classifier trained on promoter gene sequences.

## Features

- **DNA Sequence Classification**: Predicts E.Coli presence from 57-nucleotide sequences
- **Machine Learning Model**: MLPClassifier with 93% accuracy
- **Web Interface**: User-friendly Django application
- **Real-time Processing**: Instant prediction results

## Project Structure

```
Dna classification/
├── DNA sequencing for detecting E.Coli.ipynb  # Jupyter notebook with model training
├── mysite/                                 # Django web application
│   ├── manage.py                           # Django management script
│   ├── mysite/                            # Django project settings
│   │   ├── settings.py                  # Django configuration
│   │   ├── urls.py                      # URL routing
│   │   └── .env                         # Environment variables
│   ├── polls/                              # Django app
│   │   ├── views.py                     # Main application logic
│   │   ├── models.py                   # Database models
│   │   ├── urls.py                     # App URL routing
│   │   ├── sustain.py                  # Model loading and caching
│   │   ├── templates/                  # HTML templates
│   │   │   └── index.html            # Main web interface
│   │   ├── E-Coli_model.pickle        # Trained ML model
│   │   └── EColi-encoder.pickle       # OneHot encoder
│   ├── db.sqlite3                         # SQLite database
│   └── requirements.txt                   # Python dependencies
└── README.md                              # This file
```

## Installation & Setup

### Prerequisites

- Python 3.10+
- Django 3.2+
- scikit-learn
- pandas
- numpy

### Step-by-Step Installation

1. **Navigate to project directory:**
   ```bash
   cd "d:\project_learning\Nlp-2\Dna classification\mysite"
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

5. **Access the application:**
   Open your web browser and go to: http://127.0.0.1:8000

## Usage

### Web Interface

1. Open http://127.0.0.1:8000 in your browser
2. Enter a DNA sequence of exactly 57 nucleotides (A, T, G, C only)
3. Click "Submit" to get prediction

### Example Sequences (57 nucleotides)

**Positive E.Coli Detection:**
```
ttaacattaataaataaggaggctctaatggcactcattagccaatcaatcaagaac
```

**Negative E.Coli Detection:**
```
ttactagcaatacgcttgcgttcggtggttaagtatgtataatgcgcgggcttgtaa
```

## Model Details

### Training Data
- **Source**: UCI Molecular Biology Promoter Gene Sequences Dataset
- **Samples**: 106 promoter gene sequences
- **Features**: 57 nucleotides per sequence
- **Classes**: Promoter (+) and Non-promoter (-)

### Model Architecture
- **Algorithm**: Multi-Layer Perceptron (MLPClassifier)
- **Hidden Layers**: (150, 100, 50)
- **Activation**: ReLU
- **Optimizer**: Adam
- **Accuracy**: 93% on test data

### Feature Engineering
- **Encoding**: One-hot encoding for nucleotides
- **Input Shape**: 57 features × 4 nucleotides = 228 features
- **Preprocessing**: Sequence alignment and standardization

## API Endpoints

### Web Interface
- **GET /**: Redirects to /home/
- **GET /home/**: Main prediction interface
- **POST /home/**: Process DNA sequence and return prediction

### Response Format

**Successful Prediction:**
```json
{
  "response": true  // E.Coli detected
}
```

```json
{
  "response": false  // E.Coli not detected
}
```

**Error Responses:**
```json
{
  "response": "invalid_length",
  "sequence_length": 56,
  "entered_sequence": "ttacatta..."
}
```

## Technical Implementation

### Django Application Structure

1. **views.py**: Main application logic with error handling
2. **sustain.py**: Model loading with caching for performance
3. **templates/index.html**: Responsive web interface
4. **urls.py**: URL routing configuration

### Error Handling

- **Length Validation**: Ensures exactly 57 nucleotides
- **Character Validation**: Only A, T, G, C allowed
- **Sklearn Compatibility**: Handles version mismatches gracefully
- **User Feedback**: Clear error messages with examples

### Performance Optimization

- **Model Caching**: Reduces loading time with Django cache
- **Efficient Encoding**: Pre-fitted OneHot encoder
- **Fast Prediction**: Optimized MLP inference

## Troubleshooting

### Common Issues

1. **"DNA sequence must be exactly 57 nucleotides long"**
   - **Solution**: Ensure your sequence has exactly 57 characters
   - **Check**: No spaces, line breaks, or extra characters

2. **Sklearn Version Compatibility Errors**
   - **Solution**: The app handles this automatically with fallback logic
   - **Restart**: Django server after changes

3. **Server Won't Start**
   - **Solution**: Check if port 8000 is available
   - **Command**: `python manage.py runserver 8080` for different port

### Dependencies Issues

If you encounter dependency conflicts:
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Model Performance

### Metrics
- **Accuracy**: 93%
- **Precision**: 83% (Positive class)
- **Recall**: 100% (Positive class)  
- **F1-Score**: 91% (Positive class)

### Confusion Matrix
```
              Predicted
              Positive  Negative
Actual Positive    10        0
Actual Negative    0         17
```

## Future Enhancements

### Planned Improvements
- [ ] Batch sequence processing
- [ ] Sequence quality scoring
- [ ] Multiple organism detection
- [ ] REST API for external integration
- [ ] Real-time sequence streaming
- [ ] Model versioning and A/B testing

### Technical Debt
- [ ] Upgrade to latest scikit-learn version
- [ ] Implement comprehensive logging
- [ ] Add unit tests
- [ ] Docker containerization
- [ ] CI/CD pipeline

## Contributing

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Code Style
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions
- Include error handling

## License

This project is for educational and research purposes. Please refer to the original dataset license for usage terms.

## Contact

For questions or support regarding this implementation, please refer to the project documentation or create an issue in the repository.

---

**Last Updated**: March 2026
**Version**: 1.0.0
**Framework**: Django 3.2 + scikit-learn
