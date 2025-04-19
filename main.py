import pandas as pd
import streamlit as st
import time
from mlb_data import get_home_run_projections  # Your data source

def main():
    st.set_page_config(page_title="MLB Home Run Projections", layout="wide")
    st.title("🔮 MLB Daily Home Run Projections")
    st.caption("AI-powered predictions using sportsbook odds, stats, and matchup data")

    # Auto-refresh options
    refresh_interval = st.sidebar.number_input("⏱ Auto-refresh interval (seconds)", min_value=30, max_value=3600, value=300, step=30)
    auto_refresh = st.sidebar.checkbox("🔁 Enable auto-refresh")

    # Store current time
    if auto_refresh:
        st.experimental_set_query_params(_=int(time.time()))
        st.experimental_rerun()

    # Load data
    df = get_home_run_projections()

    # Display full projections table
    st.subheader("📊 Full Projection Table")
    st.dataframe(df, use_container_width=True)

    # Top 3 picks
    st.subheader("🔥 Top 3 Home Run Picks Today")
    top_picks = df.sort_values(by="AI Rating", ascending=False).head(3)
    st.table(top_picks[["Player", "Team", "HR Odds", "2025 Stats", "AI Rating"]])

    st.markdown("---")
    st.caption("Built with 💻 Python and 🧠 AI | Auto-refresh resets on each page load.")

if __name__ == "__main__":
    main()
