"""
CAP - Consciousness Alignment Protocol
File: src/ui/nudge_engine.py
Purpose: Generate behavioral nudges based on CMI result
Inputs: sensor data + CMI result
Output: list of personalized nudges with economic value
License: MIT
"""

def generate_nudges(cmi_result, indoor_hours, nature_minutes_this_week):
    """
    Generates 1-3 nudges based on CMI components and behavioral context.
    Uses loss framing, economic value, and actionable suggestions.
    """
    nudges = []
    cmi = cmi_result['cmi']
    comp = cmi_result['components']

    # Urgent: High CMI
    if cmi > 75:
        nudges.append({
            'priority': 3,
            'title': '⚠️ High Cognitive Misalignment',
            'body': 'Your mind is out of sync with its biological design. Recovery is possible — right now.',
            'suggestion': 'Pause. Breathe. Step into nature or silence for 5+ minutes.'
        })

    # Indoor confinement
    if comp['indoor'] > 70:
        value = round((indoor_hours - 2) * 1.07, 2)  # $1.07 per min of recovery
        nudges.append({
            'priority': 2,
            'title': 'You’ve Been Indoors Too Long',
            'body': f'You’ve been inside {indoor_hours:.1f} hours. Your brain evolved for open skies.',
            'suggestion': 'Step outside for 12 minutes. Any green space counts.',
            'value_usd': value
        })

    # Nature deficit
    if comp['nature'] > 70:
        weekly_shortfall = max(0, 120 - nature_minutes_this_week)
        value = round(weekly_shortfall * 0.427, 2)  # $4.27 per 10 min
        nudges.append({
            'priority': 2,
            'title': 'Nature Deficit Detected',
            'body': f'You’re {int(weekly_shortfall)} minutes behind this week on restorative nature exposure.',
            'suggestion': 'Visit a park, garden, or tree-lined street today.',
            'value_usd': value
        })

    # Attention fragmentation
    if comp['attention'] > 70:
        value = round(7.55, 2)  # avg recovery value
        nudges.append({
            'priority': 3,
            'title': 'Your Attention Is Fragmenting',
            'body': 'Excessive app switching reduces deep focus and increases stress.',
            'suggestion': 'Try 10 minutes of silent walking or stillness.',
            'value_usd': value
        })

    # Circadian disruption
    if comp['circadian'] > 70:
        nudges.append({
            'priority': 3,
            'title': 'Night Screen = Melatonin Suppression',
            'body': 'Your screen use after 10 PM is suppressing melatonin by up to 88%.',
            'suggestion': 'Enable night mode and avoid screens 1 hour before bed.'
        })

    # Social isolation
    if comp['social'] > 70:
        nudges.append({
            'priority': 2,
            'title': 'Your Brain Craves Real Connection',
            'body': 'Loneliness harms health like smoking 15 cigarettes/day.',
            'suggestion': 'Meet someone in person — even a brief chat helps.'
        })

    # Sort by priority and limit to 3
    nudges.sort(key=lambda x: x['priority'], reverse=True)
    return nudges[:3]


# ———————————————————————
# Example usage
# ———————————————————————

if __name__ == "__main__":
    # Simulated CMI result
    test_cmi = {
        'cmi': 82,
        'verdict': 'High Mismatch',
        'components': {
            'indoor': 95,
            'nature': 88,
            'attention': 92,
            'circadian': 75,
            'social': 80
        }
    }

    nudges = generate_nudges(test_cmi, indoor_hours=5.1, nature_minutes_this_week=30)

    for n in nudges:
        print(f"\n[Priority {n['priority']}] {n['title']}")
        print(f"  {n['body']}")
        print(f"  → {n['suggestion']}")
        if 'value_usd' in n:
            print(f"  💰 Focus value: ${n['value_usd']}")
