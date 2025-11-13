import streamlit as st
import numpy as np
import joblib
from src.utils import validate_input

# Title and description
st.title("🩺 Diabetes Prediction App")
st.write("""
This web app predicts whether a person is likely to have **Diabetes** based on medical details.
Please fill in the details below 👇
""")

# Load trained model
@st.cache_resource
def load_model():
    try:
        model = joblib.load("model/diabetes_model.pkl")
        return model
    except FileNotFoundError:
        st.error("❌ Model not found! Please train and save the model first using train_model.py")
        return None

model = load_model()

# Input fields for user data
st.subheader("Enter Patient Details")

pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)
glucose = st.number_input("Glucose Level", min_value=0, max_value=300, value=120)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=200, value=70)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
insulin = st.number_input("Insulin Level", min_value=0, max_value=900, value=80)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)
diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
age = st.number_input("Age", min_value=1, max_value=120, value=30)

# Combine all inputs into a single list
user_data = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]

# Prediction button
if st.button("🔍 Predict"):
    if not validate_input(user_data):
        st.warning("⚠️ Please enter valid numeric values.")
    elif model is None:
        st.error("❌ No trained model found.")
    else:
        prediction = model.predict([user_data])[0]
        if prediction == 1:
            st.error("🚨 The person is **likely to have Diabetes.**")
        else:
            st.success("✅ The person is **not likely to have Diabetes.**")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit & Machine Learning")
