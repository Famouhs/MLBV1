
import pandas as pd

def get_player_stats(date):
    return pd.DataFrame([
        {"Player": "Fernando Tatis Jr.", "Team": "San Diego Padres", "Opponent": "Dodgers", "Stadium": "Petco Park", "HR": 6, "G": 19},
        {"Player": "Peter Alonso", "Team": "New York Mets", "Opponent": "Giants", "Stadium": "Citi Field", "HR": 5, "G": 20}
    ])
