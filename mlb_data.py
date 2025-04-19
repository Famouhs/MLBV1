
import pandas as pd

# This is a placeholder function; real implementation should pull from live data sources.
def get_home_run_projections():
    # Simulated AI-rated home run projections (can be replaced with scraped/API data)
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
