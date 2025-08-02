from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load trained model
with open('soil_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract input values from form
        features = [float(x) for x in request.form.values()]
        final_features = [np.array(features)]
        
        # Predict with the model
        prediction = model.predict(final_features)
        soil_quality = prediction[0]

        return render_template('index.html', prediction_text=f"Soil Quality: {soil_quality}")

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)

