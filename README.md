# Detect_Heart_Disease_using_patient_data
Detect_Heart_Disease_using_patient_data is a Flask-based ML app that predicts heart disease risk from patient inputs like age, BP, cholesterol, etc. It uses a trained model and scaler to process data, then returns predictions via a simple web form. Designed for demo/learning, not for medical diagnosis.          Ask ChatGPT
# ​​ Detect Heart Disease — Flask ML App

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.0+-black?logo=flask)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.5+-orange?logo=scikit-learn)
![License: MIT](https://img.shields.io/badge/License-MIT-green)

A **Flask-based machine learning application** that predicts the risk of heart disease from patient parameters. Designed for educational and demonstration purposes—not for medical diagnosis.

---

##  Table of Contents
- [Features](#-features)
- [Dataset & Inputs](#-dataset--inputs)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Setup & Installation](#-setup--installation)
- [Running the App](#-running-the-app)
- [Usage](#-usage)
- [Future Improvements](#-future-improvements)
- [License](#-license)

---

##  Features
- Simple web form accepts patient data like age, blood pressure, cholesterol, etc.
- Uses a trained ML model and scaler to predict heart disease risk.
- Flask backend processes inputs and returns real-time outputs.
- Clear disclaimer: not intended for clinical use.

---

##  Dataset & Inputs
Typical input features include:
- Age
- Resting Blood Pressure (BP)
- Serum Cholesterol
- Thalach (Max Heart Rate)
- Others like Fasting BS, ECG results, etc.

(Ensure your training and form inputs match these.)

---

##  Tech Stack
- **Backend:** Python, Flask  
- **ML Tools:** scikit-learn  
- **Frontend:** HTML, CSS (minimal styling)  
- **Model Persistence:** joblib or pickle

---

##  Project Structure
Detect_Heart_Disease_using_patient_data/<br>
├── app.py # Flask app<br>
├── model.pkl # Saved trained model & scaler<br>
├── templates/<br>
│ └── index.html # Frontend template<br>
├── README.md # This documentation<br>
└──Heart_diesaes_ML_Model.ipynb<br>

---

##  Setup & Installation
git clone https://github.com/Adityawagh786/Detect_Heart_Disease_using_patient_data.git
cd Detect_Heart_Disease_using_patient_data
pip install -r requirements.txt  # Flask, scikit-learn, etc.

---

Running the App:
python app.py
Open your browser and go to http://127.0.0.1:5000 to see the form.

---

Usage:<br>
1> Fill in the patient's details in the form.<br>
2> Submit — the app returns a prediction on heart disease risk.<br>
3> Use results for learning or model testing only.<br>

---

Future Improvements:<br>
*Enhanced UI with styled forms or dropdowns<br>
*Model upgrades: Tune hyperparameters or try ensemble models<br>
*Additional features: Add user authentication, logging, demo datasets<br>
*Validation: Add input checks and error handling<br>

---

Happy learning and coding!


Note: This application is for educational/demo purposes only and should not be used for actual medical diagnosis.

---


🙌 Credits

Developed by Aditya Wagh using Python, Flask, and Scikit-learn.

