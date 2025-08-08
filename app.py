from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load model and scaler
model = joblib.load("heart_disease_model.pkl")
scaler = joblib.load("scaler.pkl")

# Feature names (same as model input)
feature_names = [
    'age', 'sex', 'chest pain type', 'resting bp s', 'cholesterol',
    'fasting blood sugar', 'resting ecg', 'max heart rate',
    'exercise angina', 'oldpeak', 'ST slope'
]

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            # Get form data
            data = [float(request.form.get(f)) for f in feature_names]
            df = pd.DataFrame([data], columns=feature_names)

            # Scale and predict
            scaled = scaler.transform(df)
            result = model.predict(scaled)[0]
            prediction = "Heart Disease" if result == 1 else "No Heart Disease"
        except Exception as e:
            prediction = f"Error: {e}"
    
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
