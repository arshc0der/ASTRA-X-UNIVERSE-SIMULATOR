
<h1 align="center">🚀 Astra-X: Pro Solar System Architect</h1>

<p align="center">
  <b>An enterprise-grade solar system simulator with real physics, real code, and real missions.</b>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/arshc0der/ASTRA-X-UNIVERSE-SIMULATOR/refs/heads/main/Testing/preview/logo.jpg" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-2.0.0-blue.svg" />
  <img src="https://img.shields.io/badge/python-3.10%2B-yellow.svg" />
  <img src="https://img.shields.io/badge/physics-N--Body-orange.svg" />
  <img src="https://img.shields.io/badge/rendering-OpenGL-success.svg" />
  <img src="https://img.shields.io/badge/license-MIT-green.svg" />
  <img src="https://img.shields.io/badge/status-Stable-brightgreen.svg" />
  <img src="https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20MacOS-lightgrey.svg" />
</p>

<p align="center">
  Built by <a href="https://github.com/arshc0der">@arshc0der</a>
</p>

---

## 🌌 About Astra-X

**Astra-X** is a professional-grade **space flight simulator and mission architecture suite**.  
It combines a **high-fidelity N-Body Physics Engine** with a **live Python Flight Computer**, allowing you to:

- Design rockets  
- Write real guidance software  
- Launch missions  
- Navigate a full-scale 3D solar system  

This is **not a game** — it’s a **simulation lab**.

---

## 🖼️ Preview Gallery

<p align="center">
  <img src="https://raw.githubusercontent.com/arshc0der/ASTRA-X-UNIVERSE-SIMULATOR/refs/heads/main/Testing/preview/1.png" />
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/arshc0der/ASTRA-X-UNIVERSE-SIMULATOR/refs/heads/main/Testing/preview/2.png" />
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/arshc0der/ASTRA-X-UNIVERSE-SIMULATOR/refs/heads/main/Testing/preview/3.png" />
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/arshc0der/ASTRA-X-UNIVERSE-SIMULATOR/refs/heads/main/Testing/preview/4.png" />
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/arshc0der/ASTRA-X-UNIVERSE-SIMULATOR/refs/heads/main/Testing/preview/5.png" />
</p>

---

## 🌟 Core Features

### 🪐 Full Solar System Physics
- Real-time **N-Body gravity simulation**
- Sun, Earth, Moon, Mars, Jupiter
- True orbital mechanics (no fake rails)

### 💻 Live Flight Coding Sandbox
- Write **real Python code**
- Control thrust, pitch, staging
- Autonomous mission logic

### 📐 Rocket Design Lab
- Dry mass configuration
- Fuel capacity modeling
- Engine thrust tuning

### 📊 Professional Telemetry HUD
- Velocity vectors
- Altitude & orbital parameters
- Trajectory prediction

### 🎥 Cinematic 3D Rendering
- OpenGL-accelerated viewport
- Planet textures & orbits
- Dynamic camera tracking

### 🛡️ Crash & Landing Physics
- Collision detection
- Soft-landing logic
- Mission result evaluation

---

## 🧠 Technology Stack

| Layer | Technology |
|-----|-----------|
| Core Language | Python 3.10+ |
| GUI | PyQt6 |
| Rendering | OpenGL + PyQtGraph |
| Physics | NumPy (Vectorized math) |
| Assets | Pillow |
| Architecture | Modular, sandboxed runtime |

---

## ⚠️ Important Before Running

> **Remove the folder**

```text
Remove:  Testing 
````

---

## 📥 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/arshc0der/Astra-X.git
cd Astra-X
```

### 2️⃣ (Optional) Create Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Launch Simulator

```bash
python main.py
```

✔ Automatically handles **High-DPI / 4K scaling**

---

## 🎮 Mission Workflow

### Phase 1 — Rocket Design

1. Set **Dry Mass**
2. Configure **Fuel Capacity**
3. Adjust **Engine Thrust**
4. Click **INITIALIZE FLIGHT SYSTEMS**

### Phase 2 — Mission Control

1. Write your `mission_loop()`
2. Press **LAUNCH MISSION**
3. Observe trajectory in 3D space

---

## 📝 Example Flight Program

```python
def mission_loop():
    alt_km = rocket.get_altitude()
    vel = rocket.get_velocity()

    if alt_km < 50:
        rocket.set_pitch(90)
        rocket.set_thrust(1.0)
    elif alt_km < 150:
        rocket.set_pitch(60)
        rocket.set_thrust(1.0)
    elif vel < 7500:
        rocket.set_pitch(0)
        rocket.set_thrust(1.0)
    else:
        rocket.set_thrust(0.0)
```

---

## 📂 Project Structure

```text
AstraX_Sim/
├── main.py
├── core/
│   ├── physics.py
│   ├── runtime.py
│   └── mission_result.py
├── ui/
│   ├── window.py
│   ├── viewport.py
│   └── designer.py
└── assets/
    └── theme.py
```

---

## 🤝 Contributing

1. Fork the repo
2. Create feature branch
3. Commit changes
4. Open Pull Request

---

## 📜 License

MIT License © 2026
See `LICENSE` for details.

---

## ⭐ Support the Project

If this project impressed you — **give it a star** ⭐
It helps a lot!

🔗 **Author:** [https://github.com/arshc0der](https://github.com/arshc0der)


If you want next upgrades, I can also:
- 🔥 Add **animated GIF previews**
- 🌍 Add **mission roadmap section**
- 🧪 Add **research / educational positioning**
- 🛰️ Add **“Why Astra-X?” comparison section**
- 🧾 Auto-generate **docs site from README**

Just say the word 😌🚀