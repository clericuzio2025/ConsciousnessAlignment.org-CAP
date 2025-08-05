"""
CAP - Consciousness Alignment Protocol
File: src/ai/mismatch_score.py
Purpose: Compute Cognitive Misalignment Index (CMI) 0-100
Inputs: indoor_hours, nature_minutes_this_week, screen_switches_per_minute, 
        late_night_screen_minutes, social_proximity_events
Output: CMI score + component breakdown
License: MIT
"""

def compute_cmi_score(indoor_hours=0, 
                      nature_minutes_this_week=0, 
                      screen_switches_per_minute=0, 
                      late_night_screen_minutes=0, 
                      social_proximity_events=0):
    """
    Computes Cognitive Misalignment Index (CMI) from 0 to 100.
    Based on evolutionary mismatch theory and behavioral neuroscience.
    All processing happens on-device. No data leaves the phone.
    """
    
    # Thresholds (based on research)
    MAX_INDOOR_HOURS = 4.0
    MIN_NATURE_MINUTES_WEEKLY = 120.0
    MAX_SWITCH_RATE = 1.5  # app switches per minute
    MAX_LATE_NIGHT_MINUTES = 120.0  # 2 hours max penalty
    MIN_SOCIAL_EVENTS_DAILY = 3.0

    # Normalize inputs to 0-1 scale (1 = maximum mismatch)
    indoor_score = min(indoor_hours / MAX_INDOOR_HOURS, 1.0)
    
    nature_deficit = max(0, MIN_NATURE_MINUTES_WEEKLY - nature_minutes_this_week)
    nature_score = nature_deficit / MIN_NATURE_MINUTES_WEEKLY
    
    attention_score = min(screen_switches_per_minute / MAX_SWITCH_RATE, 1.0)
    
    circadian_score = min(late_night_screen_minutes / MAX_LATE_NIGHT_MINUTES, 1.0)
    
    social_score = max(0, 1.0 - (social_proximity_events / 7.0))  # cap at 7
    social_score = min(social_score, 1.0)

    # Weighted sum (weights from meta-analysis)
    weights = {
        'nature': 0.25,
        'indoor': 0.20,
        'attention': 0.20,
        'circadian': 0.20,
        'social': 0.15
    }

    raw_cmi = (
        weights['nature'] * nature_score +
        weights['indoor'] * indoor_score +
        weights['attention'] * attention_score +
        weights['circadian'] * circadian_score +
        weights['social'] * social_score
    )

    # Apply sigmoid to map to human-perceived stress curve
    import math
    cmi_100 = int(100 / (1 + math.exp(-10 * raw_cmi + 5)))

    # Return full breakdown
    return {
        'cmi': cmi_100,
        'verdict': 'High Mismatch' if cmi_100 > 60 else 'Mild Mismatch' if cmi_100 > 30 else 'Aligned',
        'components': {
            'indoor': int(indoor_score * 100),
            'nature': int(nature_score * 100),
            'attention': int(attention_score * 100),
            'circadian': int(circadian_score * 100),
            'social': int(social_score * 100)
        }
    }


# ———————————————————————
# Example usage (for testing)
# ———————————————————————

if __name__ == "__main__":
    result = compute_cmi_score(
        indoor_hours=5.1,
        nature_minutes_this_week=30,
        screen_switches_per_minute=2.3,
        late_night_screen_minutes=90,
        social_proximity_events=1
    )
    print("Cognitive Misalignment Index (CMI):", result['cmi'])
    print("Verdict:", result['verdict'])
    print("Breakdown:", result['components'])
