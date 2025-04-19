import pandas as pd
import streamlit as st
from mlb_data import get_home_run_projections  # Custom function

def main():
    # Streamlit page configuration
    st.set_page_config(page_title="MLB Home Run Projections", layout="wide")
    st.title("🔮 MLB Daily Home Run Projections")
    st.caption("AI-powered predictions using sportsbook odds, stats, and matchup data")

    # Fetch projections data
    df = get_home_run_projections()

    # Display the full projections table
    st.subheader("📊 Full Projection Table")
    st.dataframe(df, use_container_width=True)

    # Display top 3 picks by AI Rating
    st.subheader("🔥 Top 3 Home Run Picks Today")
    top_picks = df.sort_values(by="AI Rating", ascending=False).head(3)
    st.table(top_picks[["Player", "Team", "HR Odds", "2025 Stats", "AI Rating"]])

    # Optional: Footer
    st.markdown("---")
    st.caption("Built with 💻 Python and 🧠 AI | Data is illustrative for April 19, 2025")

if __name__ == "__main__":
    main()
