# main.py
import os
from dotenv import load_dotenv
import pandas as pd
from mlb_hr_model import load_model, get_today_predictions
import requests

# Load API keys from .env file
load_dotenv()
ODDS_API_KEY = os.getenv("ODDS_API_KEY")  # Set in .env file

# --- Weather Integration (Open-Meteo is free and keyless)
def get_weather_forecast(latitude, longitude):
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        f"&hourly=temperature_2m,wind_speed_10m"
        f"&current_weather=true"
    )
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        current_weather = data.get("current_weather", {})
        return {
            "temperature": current_weather.get("temperature"),
            "wind_speed": current_weather.get("windspeed")
        }
    return {"temperature": None, "wind_speed": None}

# --- Sportsbook Integration (The Odds API)
def get_mlb_odds():
    if not ODDS_API_KEY:
        print("⚠️ ODDS_API_KEY not found. Skipping odds fetch.")
        return []
    url = (
        f"https://api.the-odds-api.com/v4/sports/baseball_mlb/odds"
        f"?regions=us&markets=h2h&apiKey={ODDS_API_KEY}"
    )
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    print(f"Failed to fetch odds: {response.status_code}")
    return []

def format_output(df):
    print("\n🔥 Top Home Run Candidates Today 🔥\n")
    print(f"{'Player':25} {'Team':>6} {'HR Probability':>15}")
    print("=" * 50)
    for _, row in df.iterrows():
        print(f"{row['player_name'][:25]:25} {row['team']:>6} {row['hr_prob']*100:14.2f}%")
    print()

def main():
    print("🔄 Loading AI model...")
    model = load_model()

    print("📊 Fetching today's player data...")
    df = get_today_predictions(model)

    if df.empty:
        print("⚠️ No data available yet for today.")
        return

    # Optional: add weather data for each game if location info is available
    # df['temperature'], df['wind_speed'] = ...

    # Optional: fetch sportsbook odds (can be joined to df if teams match)
    odds_data = get_mlb_odds()

    top_10 = df.sort_values("hr_prob", ascending=False).head(10)
    format_output(top_10)

if __name__ == "__main__":
    main()
