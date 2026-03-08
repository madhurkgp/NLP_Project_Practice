# Car Acceptability Prediction

A Flask-based web application that predicts car acceptability using machine learning algorithms.

## Features

- **Multiple ML Algorithms**: Choose from Random Forest, Decision Tree, and Support Vector Classifier
- **Interactive Web Interface**: User-friendly form for input parameters
- **Data Visualization**: Charts showing feature distributions
- **Real-time Predictions**: Get instant car acceptability predictions with accuracy metrics

## Dataset

The application uses the Car Evaluation Database with the following features:
- **Buying Price**: v-high, high, med, low
- **Maintenance Price**: v-high, high, med, low  
- **Number of Doors**: 2, 3, 4, 5-more
- **Persons Capacity**: 2, 4, more
- **Luggage Boot Size**: small, med, big
- **Safety Rating**: low, med, high

**Target Classes**: unacc (unacceptable), acc (acceptable), good, v-good (very good)

## Installation

1. **Clone or navigate to the project directory:**
```bash
cd "car acceptability prediction"
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## Running the Application

1. **Start the Flask server:**
```bash
python main.py
```

2. **Access the application:**
   - Open your browser and go to `http://127.0.0.1:5000`
   - The application will be running in debug mode

## Usage

1. **Select a Feature**: Choose which feature you want to analyze (for visualization)
2. **Set Car Parameters**:
   - Buying Mode: High, Low, Medium, Very High
   - Maintenance Mode: High, Low, Medium, Very High
   - Number of Doors: Two, Three, Four, Five or More
   - Persons Capacity: Two, Four, More
   - Luggage Section: big, med, small
   - Safety Medium: High, Low, Medium
3. **Choose Algorithm**: Select from Random Forest, Decision Tree, or SVM
4. **Click Predict**: Get the car acceptability prediction with accuracy

## Project Structure

```
car acceptability prediction/
├── main.py              # Main Flask application
├── modelbuilding.py     # ML model definitions
├── requirements.txt     # Python dependencies
├── car.data            # Dataset file
├── templates/
│   └── index.html      # HTML template
└── README.md           # This file
```

## Dependencies

- Flask >= 2.0.0
- scikit-learn >= 1.0.0
- pandas >= 1.3.0
- numpy >= 1.21.0
- gunicorn >= 20.0.0

## Machine Learning Models

The application implements four classification algorithms:

1. **Random Forest Classifier**: Ensemble method using multiple decision trees
2. **Decision Tree Classifier**: Tree-based classification model
3. **Support Vector Classifier (SVC)**: Finds optimal hyperplane for classification
4. **K-Nearest Neighbors (KNN)**: Instance-based learning algorithm

Each model is trained on the car evaluation dataset and provides accuracy, precision, recall, and F1-score metrics.

## Technical Details

- **Data Preprocessing**: Label encoding for categorical features
- **Train-Test Split**: 80-20 split for model evaluation
- **Feature Engineering**: Six input features mapped to numerical values
- **Model Evaluation**: Standard classification metrics for performance assessment

## Contributing

Feel free to enhance the application by:
- Adding more ML algorithms
- Improving the UI/UX
- Adding data preprocessing options
- Implementing model persistence

## License

This project is for educational purposes and demonstrates Flask web development with machine learning integration.
