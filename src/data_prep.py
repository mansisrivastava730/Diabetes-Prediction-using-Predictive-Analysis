import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(path: str):
    """Load dataset from a CSV file"""
    return pd.read_csv(path)

def prepare_data(df):
    """Split data into training and testing sets"""
    X = df.drop('Outcome', axis=1)
    y = df['Outcome']
    return train_test_split(X, y, test_size=0.2, random_state=42)
