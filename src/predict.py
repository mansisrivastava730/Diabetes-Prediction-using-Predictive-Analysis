import joblib

def predict_diabetes(data):
    """Load trained model and predict"""
    model = joblib.load('model/diabetes_model.pkl')
    prediction = model.predict([data])[0]
    return prediction
