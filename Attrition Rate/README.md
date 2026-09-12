# Employee Attrition Predictor

A machine learning-powered web application that predicts employee attrition risk based on various factors such as demographics, job characteristics, and work history.

## 🎯 Project Overview

This project uses data science techniques to analyze employee data and predict whether an employee is likely to stay with the company or leave. The system combines a Django web interface with scikit-learn machine learning models to provide real-time attrition predictions.

## 🚀 Features

- **Interactive Web Interface**: Modern, responsive design with Bootstrap 5
- **Machine Learning Models**: Multiple algorithms with Logistic Regression as the primary model
- **Real-time Predictions**: Instant attrition risk assessment
- **Data Processing Pipeline**: Comprehensive data preprocessing and feature engineering
- **Professional UI**: Gradient-based modern design with smooth animations

## 📊 Model Performance

| Algorithm | Training Accuracy | Test Accuracy |
|-----------|------------------|---------------|
| Logistic Regression | 88.97% | 84.92% |
| Random Forest | 99.72% | 87.15% |
| Decision Tree | 99.86% | 82.12% |
| Naive Bayes | 86.03% | 83.24% |
| KNN | 87.71% | 79.89% |
| SVM | 66.20% | 65.92% |

## 🛠️ Technology Stack

### Backend
- **Django 4.2.7** - Web framework
- **Python 3.10** - Programming language
- **scikit-learn 1.3.0** - Machine learning library
- **pandas 2.0.3** - Data manipulation
- **numpy 1.24.3** - Numerical computing

### Frontend
- **Bootstrap 5.3.0** - CSS framework
- **Bootstrap Icons 1.11.0** - Icon library
- **Custom CSS** - Gradient designs and animations

### Database
- **SQLite3** - Development database

## 📁 Project Structure

```
Attrition Rate/
├── Attrition Rate.ipynb          # Data analysis and model training notebook
├── Table_1.csv                   # Original employee dataset
├── finalized_model.pickle         # Trained machine learning model
├── processed table.csv           # Processed dataset for training
├── README.md                    # This file
└── mysite/                      # Django web application
    ├── Attrition/               # Main Django app
    │   ├── templates/
    │   │   └── attrition_form.html  # Web interface template
    │   ├── views.py             # Application logic and ML integration
    │   ├── urls.py              # URL routing
    │   ├── models.py           # Database models
    │   └── admin.py            # Django admin configuration
    ├── mysite/                 # Django project settings
    │   ├── settings.py         # Project configuration
    │   ├── urls.py            # Main URL routing
    │   └── wsgi.py            # WSGI configuration
    ├── manage.py               # Django management script
    ├── db.sqlite3              # SQLite database
    └── requirements.txt        # Python dependencies
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd "d:\project_learning\Nlp-2\Attrition Rate"
   ```

2. **Navigate to the Django application:**
   ```bash
   cd mysite
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   - Open your browser and go to `http://127.0.0.1:8000/`
   - The root URL will automatically redirect to the prediction form

## 📝 Usage Guide

### Using the Web Interface

1. **Fill in Employee Information:**
   - Employee Name
   - Current Location
   - Employee Group (B1, B2, B3, Other)
   - Work Function (Support, Operation, Sales)
   - Gender
   - Tenure Group
   - Experience (in years)
   - Age (in years)
   - Marital Status
   - Hiring Source
   - Promotion Status
   - Job Role Match

2. **Submit the Form:**
   - Click "Predict Attrition" to get the prediction
   - Results will display with color coding:
     - 🟢 Green: "Stay" - Low attrition risk
     - 🔴 Red: "Left" - High attrition risk

### Data Analysis

For data scientists who want to explore the model:

1. **Open the Jupyter Notebook:**
   ```bash
   jupyter notebook "Attrition Rate.ipynb"
   ```

2. **Run the cells** to see:
   - Data preprocessing steps
   - Feature engineering
   - Model training and evaluation
   - Performance metrics

## 🧠 Model Details

### Features Used
- **Demographics**: Age, Gender, Marital Status
- **Professional**: Employee Group, Function, Experience, Tenure
- **Performance**: Promotion Status, Job Role Match
- **Location**: Current work location
- **Recruitment**: Hiring Source

### Data Preprocessing
- Missing value handling
- Categorical encoding (one-hot encoding)
- Feature scaling
- Location mapping to numerical values

### Model Selection
Logistic Regression was selected as the primary model due to:
- Good balance between training and test accuracy
- Interpretability of results
- Lower risk of overfitting compared to tree-based models

## 🔧 Configuration

### Django Settings
- **Debug Mode**: Enabled for development
- **Allowed Hosts**: Configured for local development
- **Static Files**: Configured for Bootstrap and custom CSS
- **Database**: SQLite3 for development

### Model Path
The trained model is stored at:
- `finalized_model.pickle` (root directory)
- Automatically loaded by the Django application

## 🎨 UI/UX Features

- **Responsive Design**: Works on desktop, tablet, and mobile
- **Modern Gradients**: Purple-blue color scheme
- **Interactive Elements**: Hover effects and smooth transitions
- **Form Validation**: Required fields and proper input types
- **Result Visualization**: Color-coded prediction results
- **Bootstrap Icons**: Contextual icons for better UX

## 📈 Future Enhancements

- **Model Retraining**: Web interface for model updates
- **Feature Importance**: Display key factors affecting predictions
- **Historical Data**: Track prediction accuracy over time
- **Export Functionality**: Download predictions as CSV
- **Advanced Analytics**: Dashboard with attrition trends
- **Multi-language Support**: Internationalization

## 🐛 Troubleshooting

### Common Issues

1. **Server won't start:**
   - Check if port 8000 is available
   - Ensure all dependencies are installed
   - Run `python manage.py check` for configuration errors

2. **Model loading errors:**
   - Verify `finalized_model.pickle` exists in the root directory
   - Check scikit-learn version compatibility

3. **Form submission issues:**
   - Ensure all required fields are filled
   - Check browser console for JavaScript errors

### Dependencies Issues
If you encounter package conflicts, create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 📄 License

This project is for educational and demonstration purposes. Please ensure compliance with your organization's data privacy policies when using employee data.

## 👥 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For questions or issues:
- Check the troubleshooting section
- Review the Jupyter notebook for data processing details
- Verify Django configuration in settings.py

---

**Note**: This application uses machine learning predictions as a tool for insights. Always combine predictions with human judgment and organizational context when making employment decisions.
