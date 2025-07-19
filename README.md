# 🛡️ Silver Lining AI — Threat Detection System

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Live Demo](https://img.shields.io/badge/Try_Online-Here-green)](https://github.com/vinayack7/Silver-Lining/blob/main/SL.html)
[![Video Demo](https://img.shields.io/badge/Video_Demo-Here-red)](https://drive.google.com/file/d/1FOLh3OPfuckIW0o2swGFXAWhN9ICngMA/view)
[![Explanation Video](https://img.shields.io/badge/Watch_Video-Here-purple)](https://drive.google.com/file/d/1SNCplL_UkRUdFjr8UqSbhFkSsRqC65uM/view?usp=drivesdk)

> **Silver Lining** is a modern AI-based security tool designed to simulate phishing protection, deepfake detection, and real-time risk scoring using an interactive web UI. Ideal for users, developers, and evaluators who want to experience cybersecurity through an intuitive frontend and smart backend logic.

---

## 🌟 Features Overview

| Feature            | Description                                | Example/Test                      |
|-------------------|--------------------------------------------|----------------------------------|
| 🔍 URL Scanner     | Detects phishing/malware threat patterns    | `https://secure-paypal-login.com` |
| 🎭 Deepfake AI     | Flags AI-manipulated image/video files      | [Sample Image](assets/test-image.jpg) |
| 🛡️ Real-Time Block | Displays a blocking screen for known threats | `https://malicious-site.com`     |
| 📊 Trust Scoring   | Assigns 1–10 trust level with reasons        | `Score: 3/10 → Warning`          |

---

## ⚙️ Tech Stack

- **Frontend:** HTML5, CSS3, JavaScript, Font Awesome  
- **Backend:** Python (Flask)  
- **AI Logic (Simulated):** Custom scoring with Gemini/TensorFlow placeholders  
- **Demo & Hosting:** GitHub Pages, Localhost Flask

---

## 🚀 Getting Started (30 Seconds)

# 1. Clone the repo
git clone https://github.com/vinayack7/Silver-Lining.git
cd Silver-Lining

# 2. Run frontend (Option 1)
open SL.html         # Or drag into any browser

# 3. (Optional) Run backend with Flask
pip install -r requirements.txt
python app.py        # Then go to http://localhost:5000

---

## 🧪 Testing Guide

Action	Expected Result
Input: https://wikipedia.org	✅ Trust Score: 9/10 — Safe
Input: https://phishing-example.com	🚫 Blocked Page Screen Shown
Upload: AI-generated image	🎭 Flagged as "Suspicious"

---

## 🧠 Architecture
''bash

SL.html (Frontend UI)
   │
   ├── JavaScript Logic (Threat Analysis Simulation)
   │
   └── Flask API (app.py)  ← Handles POST /analyze-url + /check-media
        └── Simulated DeepSeek AI scoring

⚠️ The current backend is simulated for demonstration. Production version would integrate real AI models or services (e.g., VirusTotal, DeepFace, Gemini).

---

## 🎯 Roadmap

✅ Static UI + Demo Simulation

🧪 Flask-based API scoring

🔄 Real API integration (DeepSeek, HuggingFace)

🔌 Chrome Extension

📱 Mobile App

🧠 ML model deployment on HuggingFace/Vertex AI

---

👨‍💻 Project Lead G. Vinayack
📧 22kq1a0546cse@gmail.com
🔗 GitHub
