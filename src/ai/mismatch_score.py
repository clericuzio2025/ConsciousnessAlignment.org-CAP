def compute_cmi_score(indoor_hours=0,
                       nature_minutes_this_week=0,
                       screen_switches_per_minute=0,
                       late_night_screen_minutes=0,
                       social_proximity_events=0):
    MAX_INDOOR_HOURS = 4.0
    MIN_NATURE_MINUTES_WEEKLY = 120.0
    MAX_SWITCH_RATE = 1.5
    MAX_LATE_NIGHT_MINUTES = 120.0
    MIN_SOCIAL_EVENTS_DAILY = 3.0

    indoor_score = min(indoor_hours / MAX_INDOOR_HOURS, 1.0)

    nature_deficit = max(0, MIN_NATURE_MINUTES_WEEKLY - nature_minutes_this_week)
    nature_score = nature_deficit / MIN_NATURE_MINUTES_WEEKLY

    attention_score = min(screen_switches_per_minute / MAX_SWITCH_RATE, 1.0)

    circadian_score = min(late_night_screen_minutes / MAX_LATE_NIGHT_MINUTES, 1.0)

    social_score = max(0, 1.0 - (social_proximity_events / 7.0))
    social_score = min(social_score, 1.0)

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

    import math
    cmi_100 = int(100 / (1 + math.exp(-10 * raw_cmi + 5)))

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
