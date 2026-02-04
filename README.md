# 🚀 AstraX — Pro Solar System Architect

> An enterprise-grade **solar system simulator & mission design lab** with real physics, real code, and real space missions.

<p align="left">
  <img src="https://img.shields.io/badge/version-2.0.0-blue.svg" />
  <img src="https://img.shields.io/badge/status-Stable-brightgreen.svg" />
  <img src="https://img.shields.io/badge/license-MIT-green.svg" />
  <img src="https://img.shields.io/badge/python-3.10%2B-yellow.svg" />
  <img src="https://img.shields.io/badge/physics-N--Body-orange.svg" />
  <img src="https://img.shields.io/badge/rendering-OpenGL-success.svg" />
  <img src="https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg" />
  <img src="https://img.shields.io/badge/simulation-Real%20Orbital%20Mechanics-red.svg" />
  <img src="https://img.shields.io/badge/contributions-welcome-yellow.svg" />
  <img src="https://img.shields.io/github/stars/arshc0der/AstraX?style=social" />
  <img src="https://img.shields.io/github/forks/arshc0der/AstraX?style=social" />
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/arshc0der/ASTRA-X-UNIVERSE-SIMULATOR/refs/heads/main/Testing/preview/logo.jpg" width="75%" />
</p>

---

## 🌌 Overview

**Astra-X** is a **professional-grade space flight simulator and mission architecture suite**.  
It is designed as a **simulation laboratory**, not a game.

With Astra-X, you can:

- 🛰 Design rockets from physical parameters  
- 🧠 Write **real Python flight software**
- 🌍 Navigate a full-scale **3D solar system**
- 🪐 Simulate **true N-Body gravity**
- 📡 Analyze telemetry like a real mission control

> Ideal for **students, researchers, engineers, educators, and space enthusiasts**.

---

## ✨ Core Features

### 🪐 Real Solar System Physics
- True **N-Body gravitational simulation**
- Sun, Earth, Moon, Mars, Jupiter
- No fake rails or scripted orbits

### 💻 Live Flight Computer
- Write real-time **Python guidance code**
- Control thrust, pitch, staging & autonomy
- Fully sandboxed runtime

### 📐 Rocket Design Lab
- Dry mass & fuel modeling
- Engine thrust tuning
- Mass-dependent dynamics

### 📊 Mission Telemetry HUD
- Velocity vectors
- Altitude & orbital parameters
- Trajectory prediction

### 🎥 High-Fidelity 3D Rendering
- OpenGL-accelerated viewport
- Dynamic camera tracking
- Planet textures & orbital paths

### 🛬 Landing & Crash Physics
- Collision detection
- Soft-landing logic
- Mission success evaluation

---

## 🖼 Preview Gallery

<p align="center">
  <img src="https://raw.githubusercontent.com/arshc0der/ASTRA-X-UNIVERSE-SIMULATOR/refs/heads/main/Testing/preview/1.png" width="90%" />
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/arshc0der/ASTRA-X-UNIVERSE-SIMULATOR/refs/heads/main/Testing/preview/2.png" width="90%" />
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/arshc0der/ASTRA-X-UNIVERSE-SIMULATOR/refs/heads/main/Testing/preview/3.png" width="90%" />
</p>

---

## 🧠 Technology Stack

| Layer        | Technology                    |
|-------------|--------------------------------|
| Language    | Python 3.10+                   |
| GUI         | PyQt6                          |
| Rendering   | OpenGL + PyQtGraph             |
| Physics     | NumPy (Vectorized N-Body math) |
| Assets      | Pillow                         |
| Architecture| Modular & sandboxed runtime    |

---

## ⚠️ Before Running

> **IMPORTANT:**  
Remove the following folder before launching:

```text
Remove: Testing
````

---

## 🛠 Installation

### 🔹 Clone Repository

```bash
git clone https://github.com/arshc0der/AstraX.git
cd AstraX
```

### 🔹 (Optional) Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 🔹 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Launch Simulator

```bash
python main.py
```

✔ Automatic **High-DPI / 4K scaling support**

---

## 🎮 Mission Workflow

### Phase 1 — Rocket Design

1. Configure **Dry Mass**
2. Set **Fuel Capacity**
3. Tune **Engine Thrust**
4. Click **INITIALIZE FLIGHT SYSTEMS**

### Phase 2 — Mission Control

1. Write your `mission_loop()`
2. Press **LAUNCH MISSION**
3. Observe real-time 3D trajectory

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

Contributions are welcome 🚀

1. 🍴 Fork the repository
2. 🌱 Create a feature branch
3. 🛠 Commit your changes
4. 🔁 Open a Pull Request

If you like Astra-X, please ⭐ **star the repo** — it helps a lot!

---

## 📦 Deployment (Standalone EXE)

```bash
python -m PyInstaller --noconsole --onefile \
--name="AstraX" \
--icon="assets/logo.png" \
--add-data "assets;assets" \
--version-file="version_info.txt" \
main.py
```

---

## 📢 Stay Connected

| Platform | Link                                                                                     |
| -------- | ---------------------------------------------------------------------------------------- |
| GitHub   | [https://github.com/arshc0der](https://github.com/arshc0der)                             |
| Issues   | [https://github.com/arshc0der/AstraX/issues](https://github.com/arshc0der/AstraX/issues) |

---

## 📜 License

Distributed under the **MIT License**.
© 2026 **Arsh**

---

### ❤️ Built for engineers, students, researchers & space dreamers.

> **Astra-X — Not a game. A real mission simulator.**

---
