# Body Fat Percentage Estimator

A Flask-based web application that estimates body fat percentage using machine learning and body measurements.

## Overview

This application uses a trained Random Forest model to predict body fat percentage based on:
- Body density (from underwater weighing)
- Abdomen circumference
- Chest circumference  
- Weight
- Hip circumference

## Features

- Clean, responsive web interface
- Real-time body fat percentage prediction
- Input validation and error handling
- Bootstrap-based UI for better user experience

## Dataset

The model is trained on the Body Fat Prediction Dataset containing measurements from 252 men. The dataset includes:
- Density determined from underwater weighing
- Various body circumference measurements
- Age, weight, and height measurements

Dataset can be downloaded from [Kaggle](https://www.kaggle.com/fedesoriano/body-fat-prediction-dataset)

## Requirements

- Python 3.7+
- Flask and dependencies (see requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/madhurkgp/nlp1.git
cd nlp1/body_fat
```

2. Create a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix/MacOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Method 1: Development Server
```bash
python app.py
```
The application will be available at `http://localhost:5000`

### Method 2: Production Server (Gunicorn)
```bash
gunicorn app:app
```

## Usage

1. Open the application in your web browser
2. Enter your measurements in the form:
   - Body density (from underwater weighing)
   - Abdomen circumference (cm)
   - Chest circumference (cm)
   - Weight (lbs)
   - Hip circumference (cm)
3. Click "Calculate Body Fat" to get your estimate

## Model Information

- **Algorithm**: Random Forest Regressor
- **Features**: 5 body measurements
- **Output**: Body fat percentage (rounded to 2 decimal places)
- **Model file**: `bodyfatmodel.pkl`

## File Structure

```
body_fat/
├── app.py              # Main Flask application
├── bodyfatmodel.pkl    # Trained ML model
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
│   ├── home_clean.html # Input form
│   └── show_clean.html # Results page
├── bodyfat.csv         # Dataset (optional)
├── Procfile           # Heroku deployment
└── Deployment.md      # Deployment instructions
```

## API Endpoints

- `GET /` - Returns the input form
- `POST /` - Processes form data and returns prediction

## Error Handling

The application includes:
- Input validation for numeric values
- Graceful error messages for invalid inputs
- Exception handling for model prediction failures

## Deployment

The application is ready for deployment on platforms like:
- Heroku (using Procfile)
- PythonAnywhere
- Any server with Python and Flask support

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is for educational purposes. The dataset is provided for non-commercial use.

## Acknowledgments

- Dataset provided by Dr. A. Garth Fisher
- Original research by K.W. Penrose, A.G. Nelson, A.G. Fisher
- Based on research published in Medicine and Science in Sports and Exercise, vol. 17, no. 2, April 1985