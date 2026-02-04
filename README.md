# 🚀 Astra-X: Pro Solar System Architect

![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)
![Python](https://img.shields.io/badge/Python-3.10%2B-yellow.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-Stable-brightgreen.svg)

**Astra-X** is an enterprise-grade space flight simulator and mission architecture suite. It combines a high-fidelity **N-Body Physics Engine** with a **Python Coding Sandbox**, allowing users to design rockets and write real flight software to explore a full-scale 3D Solar System.

Built by **[@arshc0der](https://github.com/arshc0der)**.

---

## 🌌 Key Features

* **🪐 Full Solar System Simulation:** Real-time N-Body gravity simulation including the Sun, Earth, Mars, Moon, and Jupiter.
* **💻 Flight Coding Sandbox:** Write your own guidance algorithms in Python to control the rocket's thrust and pitch vectoring.
* **📐 Rocket Designer Lab:** Configure your vehicle's mass, fuel capacity, and engine thrust before every mission.
* **📊 Pro Telemetry HUD:** Real-time "Head-Up Display" showing orbital velocity, altitude, and trajectory data.
* **🎥 Cinematic 3D View:** OpenGL-powered rendering with trajectory plotting, planet textures, and dynamic camera tracking.
* **🛡️ Crash Physics:** Accurate collision detection and soft-landing logic.

---

## 🛠️ Technology Stack

* **Core:** Python 3.10+
* **GUI Framework:** PyQt6 (Modern Desktop Interface)
* **Visualization:** PyQtGraph + OpenGL (High-performance 3D rendering)
* **Math/Physics:** NumPy (Vectorized orbital mechanics)
* **Assets:** Pillow (Texture management)

---

## 📥 Installation

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/arshc0der/Astra-X-Sim.git](https://github.com/arshc0der/Astra-X-Sim.git)
    cd Astra-X-Sim
    ```

2.  **Create a Virtual Environment (Optional but Recommended)**
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

---

## 🚀 How to Run

Simply execute the main controller script:

```bash
python main.py

```

*Note: If you are on a High-DPI (4K) monitor, the application automatically adjusts scaling for crisp visuals.*

---

## 🎮 How to Play

### Phase 1: The Design Lab

Upon launching, you will enter the **Rocket Configuration** screen.

1. Set your **Dry Mass** (kg).
2. Set **Fuel Capacity** (Units).
3. Set **Engine Thrust** (Newtons).
4. Click **"INITIALIZE FLIGHT SYSTEMS"**.

### Phase 2: Mission Control

You are now on the Flight Deck.

1. **Write Code:** Use the editor on the left to define your `mission_loop()`.
2. **Launch:** Click the **LAUNCH MISSION** button.
3. **Explore:** Use your mouse to zoom/pan in the 3D view.

### 📝 Sample Flight Script

Copy this into the editor to launch your first mission to Orbit!

```python
def mission_loop():
    # 1. GET TELEMETRY
    alt_km = rocket.get_altitude()
    vel = rocket.get_velocity()
    
    # 2. ASCENT LOGIC
    if alt_km < 50:
        rocket.set_pitch(90) # Vertical Climb
        rocket.set_thrust(1.0)
    elif alt_km < 150:
        rocket.set_pitch(60) # Gravity Turn
        rocket.set_thrust(1.0)
    elif vel < 7500:
        rocket.set_pitch(0) # Orbital Insertion
        rocket.set_thrust(1.0)
    else:
        rocket.set_thrust(0.0) # Coast in Orbit

```

---

## 📂 Project Structure

```text
AstraX_Sim/
├── main.py                # Entry Point & DPI Handling
├── core/
│   ├── physics.py         # N-Body Gravity Engine
│   ├── runtime.py         # Secure Python Sandbox
│   └── mission_result.py  # Crash/Land Logic
├── ui/
│   ├── window.py          # Main UI Controller
│   ├── viewport.py        # 3D OpenGL Renderer
│   └── designer.py        # Rocket Config Widget
└── assets/
    └── theme.py           # Dark Mode Stylesheet

```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

### 🌟 Show your support

Give a ⭐️ if you like this project!

**Connect with me:**
[GitHub](https://github.com/arshc0der)


### **Next Steps for You**
1.  **Create the Repository:** Go to GitHub, create a new repo named `Astra-X-Sim`.
2.  **Upload:** Run these commands in your project folder:
