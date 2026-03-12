# Cursor Reconnaissance AI Tool
**Qualifi3d | Pentesting | Spring 2026**

## Purpose
Cursor Reconnaissance AI is a defensive cybersecurity proof-of-concept designed to identify suspicious cursor movement patterns that may resemble automation, scripted control, or non-human operator behavior.

This project captures mouse telemetry in real time and uses lightweight anomaly detection to compare live behavior against a short human baseline.

## Features
- Real-time mouse telemetry capture
- Cursor behavior feature extraction
- AI-based anomaly detection using Isolation Forest
- Detection signals based on:
  - Velocity
  - Acceleration
  - Direction change
  - Movement distance
- Beginner-friendly Python implementation
- Can be expanded for Vulhub or Docker lab environments

## Project Structure
```text
cursor-recon-ai/
├── recon_ai.py
├── README.md
├── requirements.txt
├── .gitignore
└── sample_data/
```

## How It Works
1. The tool listens for live mouse movement.
2. It collects a short baseline of normal human behavior.
3. It extracts behavioral features from cursor movement.
4. It uses an anomaly detection model to flag unusual activity.

## Quick Setup
```bash
git clone https://github.com/Qualifi3d/cursor-recon-ai.git
cd cursor-recon-ai
pip install -r requirements.txt
python recon_ai.py
```

## Example Output
```text
[+] Collecting baseline human cursor data for 10 seconds...
[+] Baseline model trained successfully.
[+] Live cursor behavior analysis started.
[OK] Normal behavior. Score: 0.0421
[ALERT] Suspicious cursor behavior detected. Anomaly score: -0.0184
```

## Educational Use
This project is intended for:
- cybersecurity learning
- behavioral analytics demos
- human-vs-automation detection research
- classroom lab environments

## Future Improvements
- GUI dashboard for alerts
- Logging to CSV or JSON
- Training on labeled human vs bot datasets
- Docker integration for isolated testing
- Web dashboard with Flask or FastAPI

## Disclaimer
This project is for educational and defensive research purposes only.

---

## GitHub Upload Guide

### Option 1: Upload with the GitHub website
1. Download and extract the project files.
2. Sign in to GitHub.
3. Click the **+** in the top-right and choose **New repository**.
4. Name the repo `cursor-recon-ai`.
5. Add an optional description such as:
   `Defensive cybersecurity tool that uses cursor telemetry and anomaly detection to identify suspicious automated cursor behavior.`
6. Choose **Public** or **Private**.
7. Click **Create repository**.
8. Select **uploading an existing file**.
9. Drag in these files:
   - `recon_ai.py`
   - `README.md`
   - `requirements.txt`
   - `.gitignore`
   - `sample_data/`
10. Use a commit message like:
    `Initial commit: added cursor telemetry capture and anomaly detection project files`
11. Click **Commit changes**.

### Option 2: Upload with Git in terminal
Open a terminal inside the project folder and run:

```bash
cd path/to/cursor-recon-ai
git init
git add .
git commit -m "Initial commit: added cursor telemetry capture and anomaly detection"
git branch -M main
git remote add origin https://github.com/Qualifi3d/cursor-recon-ai.git
git push -u origin main
```

### Tips
- Extract the zip before uploading.
- Upload the actual files, not just the zip file itself.
- Keep the repo clean and only include project-related files.
- A README helps your repo look much more complete for class and portfolio use.

## Recommended Repo Description
`Defensive cybersecurity project using cursor telemetry and anomaly detection to identify suspicious automated behavior.`
