import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_models():
    df = pd.read_csv("data/processed/processed_matches.csv")
    
    # Features
    X = df[['home_team_encoded', 'away_team_encoded', 'goal_scorers_encoded']]
    
    # Train models for different predictions
    models = {
        'goal_scorer': RandomForestClassifier(),
        'over_under': RandomForestClassifier(),
        'btts': RandomForestClassifier(),
        'win_draw_lose': RandomForestClassifier()
    }

    # Train each model
    for target, model in models.items():
        y = df[target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model.fit(X_train, y_train)
        joblib.dump(model, f"models/{target}_model.pkl")

if __name__ == "__main__":
    train_models()
