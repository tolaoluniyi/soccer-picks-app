import pandas as pd
from sklearn.preprocessing import LabelEncoder

def process_data():
    df = pd.read_csv("data/raw/matches.csv")
    
    # Encode team names and goal scorers
    encoder = LabelEncoder()
    df['home_team_encoded'] = encoder.fit_transform(df['home_team'])
    df['away_team_encoded'] = encoder.transform(df['away_team'])
    df['goal_scorers_encoded'] = encoder.fit_transform(df['goal_scorers'])

    # Add additional features
    df['home_win'] = (df['outcome'] == 'home').astype(int)
    df['draw'] = (df['outcome'] == 'draw').astype(int)
    df['away_win'] = (df['outcome'] == 'away').astype(int)
    df['over_2.5'] = (df['total_goals'] > 2.5).astype(int)

    df.to_csv("data/processed/processed_matches.csv", index=False)

if __name__ == "__main__":
    process_data()
