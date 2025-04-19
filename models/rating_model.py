
def rate_player(row, weather_boost, park_boost, matchup_boost):
    base_score = row["HR"] / row["G"]
    final_score = base_score + weather_boost + park_boost + matchup_boost
    if final_score > 0.25:
        return "⭐⭐⭐⭐⭐"
    elif final_score > 0.2:
        return "⭐⭐⭐⭐☆"
    elif final_score > 0.15:
        return "⭐⭐⭐☆☆"
    else:
        return "⭐⭐☆☆☆"
