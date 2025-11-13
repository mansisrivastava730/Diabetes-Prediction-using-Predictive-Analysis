# Diabetes-Prediction-using-Predictive-Analytics
# Diabetes Prediction Project
Project overview

Title: Diabetes Prediction using Predictive Analytics
Goal: Build a binary classification model to predict if a patient has diabetes (based on clinical features), evaluate and explain the model, and deploy an interactive web app for predictions.
Dataset (suggested): Pima Indians Diabetes dataset (available as CSV). The code attempts to download automatically; you can also place data/diabetes.csv.

🔄 Workflow of the Project

Here’s the full step-by-step workflow 👇

1️⃣ Data Collection

The dataset (diabetes.csv) is used, containing medical attributes like:

Pregnancies

Glucose

Blood Pressure

Skin Thickness

Insulin

BMI

Diabetes Pedigree Function

Age

Outcome (0 = No Diabetes, 1 = Diabetes)




---

2️⃣ Data Preprocessing (src/data_prep.py)

Load the dataset using pandas

Handle missing or zero values

Split the data into training and testing sets (80–20 ratio)

Prepare it for model training



---

3️⃣ Model Training (src/train_model.py)

Train a Random Forest Classifier using the training data

Evaluate model performance using accuracy and confusion matrix

Save the trained model using joblib into the /model folder



---

4️⃣ Prediction (src/predict.py)

Load the saved model (diabetes_model.pkl)

Input patient details as a list of numerical features

Predict the diabetes outcome (0 or 1)

Return the prediction result



---

5️⃣ Streamlit Web App (app/streamlit_app.py)

Collects user input (via sliders and text boxes)

Validates input using helper functions (utils.py)

Calls the trained model for prediction

Displays results dynamically:

✅ Not Diabetic

🚨 Likely Diabetic




---

6️⃣ Testing (tests/test_train.py)

Simple unit test to ensure code executes correctly using pytest



---

7️⃣ Automation & Deployment

GitHub Actions Workflow (.github/workflows/python-app.yml)

Automatically installs dependencies

Runs tests

Ensures the project works before merging any new code


Can also integrate with Streamlit Cloud or Render for free web deployment.
