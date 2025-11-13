import joblib
from sklearn.ensemble import RandomForestClassifier
from src.data_prep import load_data, prepare_data

def train_and_save_model():
    """Train the model and save it as a .pkl file"""
    df = load_data('data/diabetes.csv')
    X_train, X_test, y_train, y_test = prepare_data(df)

    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Save the model in model/ folder
    joblib.dump(model, 'model/diabetes_model.pkl')
    print("✅ Model saved successfully!")

if __name__ == "__main__":
    train_and_save_model()
