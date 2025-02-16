import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_fotmob():
    url = "https://www.fotmob.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    matches = []
    for match in soup.select('.match-row'):
        home_team = match.select_one('.home-team').text.strip()
        away_team = match.select_one('.away-team').text.strip()
        home_goals = int(match.select_one('.home-score').text.strip())
        away_goals = int(match.select_one('.away-score').text.strip())
        
        # Scrape player stats (example)
        players = match.select('.player-row')
        goal_scorers = [player.text.strip() for player in players if 'goal' in player.text.lower()]

        matches.append({
            'home_team': home_team,
            'away_team': away_team,
            'home_goals': home_goals,
            'away_goals': away_goals,
            'goal_scorers': ', '.join(goal_scorers),
            'total_goals': home_goals + away_goals,
            'btts': int(home_goals > 0 and away_goals > 0),
            'outcome': 'home' if home_goals > away_goals else ('draw' if home_goals == away_goals else 'away')
        })

    return pd.DataFrame(matches)

if __name__ == "__main__":
    matches_df = scrape_fotmob()
    matches_df.to_csv("data/raw/matches.csv", index=False)
