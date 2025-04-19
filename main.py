import streamlit as st
from dotenv import load_dotenv
from datetime import datetime
from mlb_hr_model import load_model, get_today_predictions
from mlb_data import get_probable_pitchers, get_matchup_stats
from streamlit_autorefresh import st_autorefresh
import pandas as pd
import os

load_dotenv()

# Auto-refresh every 10 minutes
st_autorefresh(interval=600000, key="datarefresh")

# Title and Date
st.title("🔮 Daily MLB Home Run Projections")
st.markdown(f"**Date:** {datetime.now().strftime('%A, %B %d, %Y')}")

# Load model and get projections
model = load_model()
df = get_today_predictions(model)

# Get probable pitchers and matchups
pitcher_df = get_probable_pitchers()
df = pd.merge(df, pitcher_df, on=["Team", "Opponent"], how="left")

# Get matchup stats and merge
matchup_df = get_matchup_stats()
df = pd.merge(df, matchup_df, on=["Batter", "Pitcher"], how="left")

# Add star rating based on model HR probability
def get_star_rating(prob):
    if prob >= 0.3:
        return "⭐⭐⭐"
    elif prob >= 0.2:
        return "⭐⭐"
    elif prob >= 0.1:
        return "⭐"
    else:
        return ""

df["★"] = df["HR_Prob"].apply(get_star_rating)

# Sorting
df = df.sort_values(by="HR_Prob", ascending=False)

# Toggles
show_adjusted = st.toggle("Show Adjusted Projections", value=True)
show_weather = st.toggle("Enable Weather Effects", value=False)

if show_adjusted:
    if show_weather:
        df["Adj_HR_Prob"] = df["HR_Prob"] * df["WeatherFactor"]
    else:
        df["Adj_HR_Prob"] = df["HR_Prob"]
    df_display = df[["Batter", "Team", "Opponent", "Pitcher", "Adj_HR_Prob", "★", "Matchup_AVG", "Matchup_HR"]]
    df_display = df_display.rename(columns={"Adj_HR_Prob": "HR_Prob (Adj)"})
else:
    df_display = df[["Batter", "Team", "Opponent", "Pitcher", "HR_Prob", "★", "Matchup_AVG", "Matchup_HR"]]

# Table
st.dataframe(df_display.reset_index(drop=True), use_container_width=True)

# Footer
st.caption("⭐ Ratings are based on AI model probabilities")
