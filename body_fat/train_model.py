import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pickle
import numpy as np

# Load the dataset
df = pd.read_csv('bodyfat.csv')

# Select features that match the original app input
features = ['Density', 'Abdomen', 'Chest', 'Weight', 'Hip']
target = 'BodyFat'

# Prepare the data
X = df[features]
y = df[target]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Test the model
train_score = rf.score(X_train, y_train)
test_score = rf.score(X_test, y_test)

print(f"Training R² score: {train_score:.4f}")
print(f"Test R² score: {test_score:.4f}")

# Save the model
with open('bodyfatmodel_new.pkl', 'wb') as f:
    pickle.dump(rf, f)

print("New model saved as 'bodyfatmodel_new.pkl'")

# Test with sample data
sample_data = [[1.0708, 85.2, 93.1, 154.25, 94.5]]  # Sample from first row
prediction = rf.predict(sample_data)[0]
print(f"Sample prediction: {prediction:.2f}% (actual: 12.3%)")
