import pandas as pd
import joblib

def predict_matches():
    df = pd.read_csv("data/processed/processed_matches.csv")
    
    # Load models
    goal_scorer_model = joblib.load("models/goal_scorer_model.pkl")
    over_under_model = joblib.load("models/over_under_model.pkl")
    btts_model = joblib.load("models/btts_model.pkl")
    win_draw_lose_model = joblib.load("models/win_draw_lose_model.pkl")

    # Make predictions
    df['likely_goal_scorer'] = goal_scorer_model.predict(df[['home_team_encoded', 'away_team_encoded', 'goal_scorers_encoded']])
    df['over_under_2.5'] = over_under_model.predict(df[['home_team_encoded', 'away_team_encoded', 'goal_scorers_encoded']])
    df['btts'] = btts_model.predict(df[['home_team_encoded', 'away_team_encoded', 'goal_scorers_encoded']])
    df['outcome'] = win_draw_lose_model.predict(df[['home_team_encoded', 'away_team_encoded', 'goal_scorers_encoded']])

    return df[['home_team', 'away_team', 'likely_goal_scorer', 'over_under_2.5', 'btts', 'outcome']]

if __name__ == "__main__":
    predictions = predict_matches()
    print(predictions)
