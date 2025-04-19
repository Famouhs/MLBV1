
import pandas as pd
import numpy as np
import joblib
import os
from datetime import datetime

def load_model(model_path="models/hr_model.pkl"):
    """Load a pre-trained home run model from disk."""
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")
    return joblib.load(model_path)

def get_today_predictions(model, player_data_path="data/todays_players.csv"):
    """
    Generate home run predictions for today's batters using the trained model.
    
    Args:
        model: Trained sklearn-like model with a .predict_proba() method.
        player_data_path: Path to a CSV with today’s player stats/features.

    Returns:
        pd.DataFrame: Players with predictions and probabilities.
    """
    if not os.path.exists(player_data_path):
        raise FileNotFoundError(f"Player data not found at {player_data_path}")

    # Load today's player feature set
    df = pd.read_csv(player_data_path)

    # Extract features expected by the model
    # Assume the model expects these columns:
    expected_features = [
        "avg", "obp", "slg", "iso", "barrel_rate",
        "flyball_rate", "pull_rate", "hard_hit_pct",
        "hr_per_fb", "xwoba", "launch_angle", "exit_velocity"
    ]
    
    # Sanity check: ensure all required features are present
    missing = [col for col in expected_features if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    X = df[expected_features]
    preds = model.predict_proba(X)[:, 1]  # Probability of hitting a HR

    df["HR_Probability"] = preds
    df["HR_Stars"] = (preds * 5).round(1)  # Example: 5-star rating scale
    df["Prediction Date"] = datetime.now().strftime("%Y-%m-%d")

    return df.sort_values("HR_Probability", ascending=False)
