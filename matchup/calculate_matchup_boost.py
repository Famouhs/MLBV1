
def fetch_bvp_data(batter_name, pitcher_name):
    return {"AVG": 0.300, "SLG": 0.650, "OPS": 1.050, "HR": 2, "AB": 8}

def fetch_hand_split_data(batter_name, pitcher_hand):
    return {"SLG": 0.520, "HR_rate": 0.07}

def calculate_matchup_boost(batter_name, pitcher_name, pitcher_hand):
    try:
        data = fetch_bvp_data(batter_name, pitcher_name)
        if data["AB"] >= 5:
            hr_boost = data["HR"] / data["AB"]
            slg_boost = (data["SLG"] - 0.400)
            return min(0.15, hr_boost + slg_boost * 0.05)
        else:
            raise ValueError("Not enough AB")
    except Exception:
        split = fetch_hand_split_data(batter_name, pitcher_hand)
        return min(0.10, split["HR_rate"] + (split["SLG"] - 0.400) * 0.04)
