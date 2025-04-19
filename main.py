# main.py

import streamlit as st
import pandas as pd
from mlb_data import get_home_run_projections  # Your custom function

def main():
    # Streamlit page config
    st.set_page_config(page_title="MLB HR Projections", layout="centered")
    st.title("🔮 Daily MLB Home Run AI Projections")
    st.markdown("Get today's top projected home run hitters based on AI and real-time data.")

    # Get data
    df = get_home_run_projections()

    if df is None or df.empty:
        st.warning("No data available. Please check the scrapers or try again later.")
        return

    # Display table
    st.dataframe(df.head(10), use_container_width=True)

    # Optional: show markdown version too
    with st.expander("📋 View as Markdown Table"):
        st.markdown(df.head(10).to_markdown(index=False), unsafe_allow_html=True)

    # Optional note
    st.caption("Odds from FanDuel. AI ratings calculated using historical & matchup-based features.")

if __name__ == "__main__":
    main()

