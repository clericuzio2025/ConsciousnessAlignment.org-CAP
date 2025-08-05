"""
CAP - Consciousness Alignment Protocol
File: demo_session.py
Purpose: Simulate a full CAP session — from data to diagnosis to nudge
Author: Global Consortium of Scientists, Engineers, and Thinkers
License: MIT

This script demonstrates how CAP detects evolutionary mismatch and guides alignment.
Run it to see the future of cognitive infrastructure in action.
"""

# Import the two core modules we've built
from src.ai.mismatch_score import compute_cmi_score
from src.ui.nudge_engine import generate_nudges

# —————————————————————————————
# SIMULATED USER PROFILE
# Realistic data from a knowledge worker in a high-mismatch urban environment
# —————————————————————————————

USER_PROFILE = {
    "name": "Alex Rivera",
    "age": 34,
    "occupation": "Software Developer",
    "location": "Downtown Apartment, High-Rise, Limited Green Access",
    "device": "Smartphone (Android 14)",
    "behavioral_data": {
        "indoor_hours": 6.7,                    # Hours spent indoors today
        "nature_minutes_this_week": 18,         # Total time in nature (min)
        "screen_switches_per_minute": 2.8,      # App switches / min (average)
        "late_night_screen_minutes": 110,       # Screen on between 10 PM – 6 AM
        "social_proximity_events": 1            # Bluetooth LE social pings (last 24h)
    }
}

# —————————————————————————————
# STEP 1: Run Mismatch Diagnosis
# —————————————————————————————

print("🧠 RUNNING CONSCIOUSNESS ALIGNMENT PROTOCOL v1.0")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

print(f"👤 Simulating user: {USER_PROFILE['name']} ({USER_PROFILE['occupation']})")
print("📡 Collecting passive behavioral data...\n")

data = USER_PROFILE["behavioral_data"]

print("📊 Behavioral Input:")
print(f"  • Indoor duration:       {data['indoor_hours']} hours")
print(f"  • Nature this week:      {data['nature_minutes_this_week']} min")
print(f"  • App switches/min:      {data['screen_switches_per_minute']}")
print(f"  • Late-night screen:     {data['late_night_screen_minutes']} min")
print(f"  • Social proximity:      {data['social_proximity_events']} events\n")

print("⚙️  Computing Cognitive Misalignment Index (CMI)...\n")

cmi_result = compute_cmi_score(
    indoor_hours=data['indoor_hours'],
    nature_minutes_this_week=data['nature_minutes_this_week'],
    screen_switches_per_minute=data['screen_switches_per_minute'],
    late_night_screen_minutes=data['late_night_screen_minutes'],
    social_proximity_events=data['social_proximity_events']
)

print(f"🎯 CMI Score: {cmi_result['cmi']} → {cmi_result['verdict']}")
print("🧩 Breakdown:")
for dim, score in cmi_result['components'].items():
    print(f"   {dim.capitalize()}: {score}")

print("\n" + "💬 GENERATING ALIGNMENT NUDGES" + "\n" + "━" * 30 + "\n")

# —————————————————————————————
# STEP 2: Generate Behavioral Nudges
# —————————————————————————————

nudges = generate_nudges(cmi_result, data['indoor_hours'], data['nature_minutes_this_week'])

print(f"📬 {len(nudges)} Nudges Generated:\n")

for i, n in enumerate(nudges, 1):
    priority_emoji = "⚠️" if n['priority'] == 3 else "💡" if n['priority'] == 2 else "✨"
    print(f"{i}. {priority_emoji} **{n['title']}**")
    print(f"   {n['body']}")
    print(f"   → {n['suggestion']}")
    if 'value_usd' in n:
        print(f"   💰 Cognitive recovery value: **${n['value_usd']}**")
    print()

# —————————————————————————————
# STEP 3: Show System Impact
# —————————————————————————————

print("🌍 SYSTEM-LEVEL INSIGHT (Aggregated & Anonymized)")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

city_data = {
    "users_in_network": 12_473,
    "avg_cmi": 68,
    "total_focus_recovered_today": 42_811,  # in USD
    "most_common_nudge": "Nature Deficit Detected",
    "top_restorative_location": "Riverside Park"
}

print("📊 Urban Alignment Dashboard (Sample):")
print(f"  • Connected users:       {city_data['users_in_network']:,}")
print(f"  • Avg CMI:               {city_data['avg_cmi']}")
print(f"  • Focus recovered today: ${city_data['total_focus_recovered_today']:,}")
print(f"  • Top nudge:             {city_data['most_common_nudge']}")
print(f"  • Most visited park:     {city_data['top_restorative_location']}\n")

print("✅ This data (fully anonymized) can be licensed to city planners to optimize green space investment — at no cost to users.")

# —————————————————————————————
# Final Message
# —————————————————————————————

print("\n" + "✅ CONSCIOUSNESS ALIGNMENT PROTOCOL: ACTIVE" + "\n" + "━" * 45)
print("This is not wellness. This is not gamification.")
print("This is the first system to detect and correct a problem that has existed since the evolution of man —")
print("— evolutionary mismatch — using only the phone in your pocket.")
print("And it costs nothing to run.")
print("\n#AlignWithReality")
