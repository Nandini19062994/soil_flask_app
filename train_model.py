import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load dataset
data = pd.read_csv("soil_dataset.csv")

# Crop-to-quality mapping
crop_to_quality = {
    'rice': 'Fertile',
    'maize': 'Moderate',
    'wheat': 'Fertile',
    'mungbean': 'Poor',
    'lentil': 'Moderate',
    'kidneybeans': 'Moderate',
    'pigeonpeas': 'Poor',
    'mothbeans': 'Poor',
    'blackgram': 'Moderate',
    'muskmelon': 'Fertile',
    'watermelon': 'Fertile',
    'grapes': 'Fertile',
    'apple': 'Fertile',
    'orange': 'Moderate',
    'papaya': 'Fertile',
    'coconut': 'Moderate',
    'banana': 'Fertile',
    'mango': 'Fertile',
    'coffee': 'Moderate'
}

# Create new column for Soil Quality
data['Soil_Quality'] = data['Soil_type'].map(crop_to_quality)

# Drop rows where mapping failed (NaN values)
data.dropna(subset=['Soil_Quality'], inplace=True)

# Drop original crop column
data.drop(columns=['Soil_type'], inplace=True)

# Define features and label
features = ['ph', 'humidity', 'nitrogen', 'phosphorus', 'potassium', 'temperature']
X = data[features]
y = data['Soil_Quality']

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model
with open('soil_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as 'soil_model.pkl'")
