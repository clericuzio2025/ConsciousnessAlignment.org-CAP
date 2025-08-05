# 🧠 Consciousness Alignment Protocol (CAP)  
## System Architecture v1.0  
*Real-time evolutionary mismatch detection and cognitive restoration via smartphone — private, lightweight, open-source*

---

## 🌐 Overview

CAP is a **privacy-first, on-device cognitive alignment engine** that detects signs of evolutionary mismatch and prescribes restorative interventions using only existing smartphone sensors.

It operates in **four layers**:

All processing occurs **on-device**.  
No raw behavioral data leaves the phone.  
Only **aggregated, anonymized insights** are shared (opt-in).

---

## 📡 Layer 1: Sensing & Fusion

CAP uses **existing smartphone sensors** to detect behavioral patterns linked to evolutionary mismatch.

### 🔹 Sensors Used
| Sensor | Purpose | Frequency |
|-------|--------|-----------|
| GPS | Detect indoor/outdoor status, proximity to green spaces (via NDVI) | 5-min intervals |
| Screen Time API | Measure digital engagement duration and fragmentation | Real-time |
| Accelerometer | Detect movement vs. sedentary behavior | 30-sec polling |
| Ambient Light Sensor | Estimate circadian light exposure | 10-min intervals |
| Bluetooth LE (optional) | Anonymous social proximity (Dunbar-inspired clustering) | Randomized MAC, no IDs |
| Time Zone / Clock | Track circadian misalignment (e.g., late-night screen use) | Continuous |

### 🔹 Green-Space Detection
- Uses **NASA MODIS NDVI** (Normalized Difference Vegetation Index) data
- Cached locally per region (~1MB per metro area)
- Matches GPS coordinates to vegetation density
- Triggers "nature exposure" logging when user enters high-NDVI zone

> 🌿 **Definition of "Restorative Exposure"**:  
> ≥5 min in area with NDVI > 0.6 (moderate vegetation) + motion < 1.5 m/s (non-commuting)

---

## ⚙️ Layer 2: Data & Privacy Core

CAP follows **privacy-by-design** and **zero-knowledge principles**.

### 🔐 Core Rules
1. **No raw data leaves the device**
2. **No user identifiers collected**
3. **All AI runs on-device**
4. **Aggregation occurs only after anonymization**
5. **Opt-in required for any external data sharing**

### 🧱 Data Flow
```text
[Raw Sensors] 
    ↓ (on-device)
[Anonymized Feature Extraction] 
    ↓ (e.g., "User was indoors 4h, screen active 87%")
[Mismatch Score Engine] 
    ↓
[Alignment Nudge Generated] 
    ↓
[Optional: Aggregated Insight → Secure Upload]

 Layer 3: Decision Layer (On-Device AI)

The Decision Layer is the cognitive engine of CAP — a lightweight, interpretable, on-device artificial intelligence model that computes the Cognitive Misalignment Index (CMI), a real-time score (0–100) reflecting the degree of evolutionary mismatch in the user’s current behavioral pattern.

The model evaluates five biologically grounded dimensions of modern maladaptation:

Indoor Confinement – Prolonged absence from natural environments
Nature Deficit – Insufficient exposure to restorative green spaces
Attention Fragmentation – Excessive digital switching and cognitive load
Circadian Disruption – Screen use during biological night
Social Isolation – Lack of in-person social proximity
 Each dimension is weighted by meta-analytic evidence on its impact on mental performance, stress, and long-term health. The weights are:

Nature Deficit: 25%
Indoor Confinement: 20%
Attention Fragmentation: 20%
Circadian Disruption: 20%
Social Isolation: 15%
 The model is a lightweight Random Forest variant, under 500 KB, compiled to TensorFlow Lite (Android) and Core ML (iOS). All processing occurs on-device. No raw data leaves the phone.

Input features are passively collected:

Indoor duration (from GPS and Wi-Fi stability)
Weekly nature exposure (GPS + NDVI lookup)
App switch rate (from Digital Wellbeing or Screen Time API)
Late-night screen time (screen on between 10 PM and 6 AM)
Social proximity events (Bluetooth LE with randomized MAC addresses)
 The final CMI is calculated as a sigmoid-scaled weighted sum: CMI = sigmoid( Σ (weight × normalized_score) × 10 − 5 ) × 100

CMI ranges:

0–29: Aligned (no nudge)
30–59: Mild Mismatch (gentle suggestion)
60–100: High Mismatch (urgent prescription)
 The model is trained on behavioral datasets correlated with cortisol, HRV, and cognitive testing, and validated against Attention Restoration Theory, Life History Theory, and allostatic load models.

This layer transforms passive data into biological insight — without surveillance.

 💬 Layer 4: User Interface & Behavioral Nudges

The User Interface Layer is CAP’s voice — a context-aware, behaviorally intelligent nudge engine that delivers personalized, science-backed interventions at the optimal moment.

It does not command. It does not shame. It informs, reframes, and empowers.

Core design principles:

Loss Framing: Emphasize cognitive value lost (e.g., “You’re losing $0.89/min in focus”)
Immediate Actionability: Prescribe specific, achievable behaviors (e.g., “12 minutes in a park”)
Economic Translation: Convert restoration into tangible cognitive ROI ($4.27 per 10 min in nature)
Circadian Timing: Deliver nudges only during alert windows (9 AM – 8 PM)
Autonomy Preservation: All nudges are dismissible; no forced engagement
 Nudge types and examples:

Indoor Confinement: “You’ve been inside 4.3 hrs. 12 min outside = +$5.12 in recovered focus.”
Attention Fragmentation: “Your attention is splitting. 10 min of stillness can reset your focus.”
Circadian Risk: “Blue light now suppresses melatonin by 88%. Consider night mode.”
Nature Deficit: “You’re 90 min behind on nature exposure. Your brain evolved outdoors.”
Social Isolation: “Real connection reduces mortality risk. Meet someone in person today.”
High CMI Alert (CMI > 75): “⚠️ Your mind is out of alignment. Pause. Breathe. Recover.”
 Behavioral science foundation:

Nudge Theory (Thaler & Sunstein): Small cues drive big changes
Prospect Theory (Kahneman & Tversky): Losses loom larger than gains
Implementation Intentions (Gollwitzer): “If-then” prompts increase compliance
Temporal Motivation Theory: Urgency + value = action
 Localization and adaptability:

Nudges are community-translated into 100+ languages
Local green spaces detected via OpenStreetMap and NDVI
Tone adjusted by region (e.g., direct in Germany, gentle in Japan)
 This layer ensures that insight leads to action — gently, respectfully, and effectively.
