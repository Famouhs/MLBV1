import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_home_run_projections():
    # Simulated AI-rated home run projections
    data = [
        {"Rank": 1, "Player": "Fernando Tatis Jr.", "Team": "San Diego Padres", "HR Odds": "+255", "2025 Stats": "6 HR in 19 games", "AI Rating": "⭐⭐⭐⭐⭐"},
        {"Rank": 2, "Player": "Peter Alonso", "Team": "New York Mets", "HR Odds": "+310", "2025 Stats": "5 HR in 20 games", "AI Rating": "⭐⭐⭐⭐☆"},
        {"Rank": 3, "Player": "Tyler Soderstrom", "Team": "Oakland Athletics", "HR Odds": "+390", "2025 Stats": "9 HR in 19 games", "AI Rating": "⭐⭐⭐⭐☆"},
        {"Rank": 4, "Player": "James Wood", "Team": "Washington Nationals", "HR Odds": "+500", "2025 Stats": "6 HR in 19 games", "AI Rating": "⭐⭐⭐⭐☆"},
        {"Rank": 5, "Player": "Spencer Torkelson", "Team": "Detroit Tigers", "HR Odds": "+560", "2025 Stats": "6 HR in 20 games", "AI Rating": "⭐⭐⭐⭐☆"},
        {"Rank": 6, "Player": "Corbin Carroll", "Team": "Arizona Diamondbacks", "HR Odds": "+400", "2025 Stats": "6 HR in 20 games", "AI Rating": "⭐⭐⭐⭐☆"},
        {"Rank": 7, "Player": "Eugenio Suárez", "Team": "Arizona Diamondbacks", "HR Odds": "+430", "2025 Stats": "6 HR in 20 games", "AI Rating": "⭐⭐⭐⭐☆"},
        {"Rank": 8, "Player": "Juan Soto", "Team": "New York Mets", "HR Odds": "+430", "2025 Stats": "3 HR in 20 games", "AI Rating": "⭐⭐⭐⭐☆"},
        {"Rank": 9, "Player": "Yordan Alvarez", "Team": "Houston Astros", "HR Odds": "+330", "2025 Stats": "2 HR in 18 games", "AI Rating": "⭐⭐⭐⭐☆"},
        {"Rank": 10, "Player": "Wilmer Flores", "Team": "San Francisco Giants", "HR Odds": "+680", "2025 Stats": "6 HR in 20 games", "AI Rating": "⭐⭐⭐⭐☆"}
    ]
    return pd.DataFrame(data)

def get_probable_pitchers():
    """
    Scrapes probable pitchers from MLB.com.
    Returns a DataFrame with Team, Opponent, and Pitcher.
    """
    url = "https://www.mlb.com/probable-pitchers"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    entries = []
    for matchup in soup.find_all("li", class_="probable-pitcher-matchup"):
        teams = matchup.find_all("span", class_="team-name")
        pitchers = matchup.find_all("a", class_="probable-pitcher__name-link")
        if len(teams) == 2 and len(pitchers) == 2:
            entries.append({"Team": teams[0].text.strip(), "Opponent": teams[1].text.strip(), "Pitcher": pitchers[0].text.strip()})
            entries.append({"Team": teams[1].text.strip(), "Opponent": teams[0].text.strip(), "Pitcher": pitchers[1].text.strip()})

    return pd.DataFrame(entries)

def get_matchup_stats():
    """
    Returns mock matchup data — replace with real scraper or stats source.
    """
    return pd.DataFrame([
        {"Batter": "Fernando Tatis Jr.", "Pitcher": "Walker Buehler", "Matchup_AVG": 0.333, "Matchup_HR": 2},
        {"Batter": "Peter Alonso", "Pitcher": "Max Fried", "Matchup_AVG": 0.267, "Matchup_HR": 1},
        {"Batter": "Tyler Soderstrom", "Pitcher": "Logan Webb", "Matchup_AVG": 0.375, "Matchup_HR": 3},
    ])
