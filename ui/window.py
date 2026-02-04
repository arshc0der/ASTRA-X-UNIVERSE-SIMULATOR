import time
from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QSplitter, QTextEdit, QPushButton, QLabel, QFrame, 
                             QMessageBox, QDoubleSpinBox, QGroupBox, QGridLayout)
from PyQt6.QtCore import QTimer, Qt

from core.physics import PhysicsEngine
from core.runtime import MissionRuntime
from ui.viewport import SpaceViewport
from assets.theme import DARK_THEME

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ASTRA-X PRO | UNIVERSE SIMULATOR")
        self.resize(1800, 1000)
        self.setStyleSheet(DARK_THEME)

        self.physics = PhysicsEngine()
        self.runtime = MissionRuntime(self.physics, self.log)

        # Main Layout
        central = QWidget()
        self.setCentralWidget(central)
        layout = QHBoxLayout(central)
        
        splitter = QSplitter(Qt.Orientation.Horizontal)

        # --- LEFT PANEL: MISSION CONTROL ---
        left = QFrame()
        left.setMaximumWidth(600)
        l_layout = QVBoxLayout(left)
        
        # 1. LIVE HUD
        hud_group = QGroupBox("LIVE TELEMETRY")
        hud_layout = QGridLayout(hud_group)
        self.lbl_alt = QLabel("ALT: 0 km")
        self.lbl_vel = QLabel("VEL: 0 m/s")
        self.lbl_body = QLabel("ORBITING: Earth")
        self.lbl_pos = QLabel("POS: 0, 0")
        
        for i, w in enumerate([self.lbl_alt, self.lbl_vel, self.lbl_body, self.lbl_pos]):
            w.setStyleSheet("font-size: 14pt; color: #00ff00; font-family: Consolas;")
            hud_layout.addWidget(w, i // 2, i % 2)
        l_layout.addWidget(hud_group)

        # 2. LIVE TWEAKS (Change mass mid-flight!)
        tweak_group = QGroupBox("ENGINEERING OVERRIDE")
        t_layout = QHBoxLayout(tweak_group)
        self.spin_thrust = QDoubleSpinBox()
        self.spin_thrust.setPrefix("Max Thrust: ")
        self.spin_thrust.setRange(1e6, 1e8)
        self.spin_thrust.setValue(7.6e6)
        self.spin_thrust.valueChanged.connect(self.update_physics)
        t_layout.addWidget(self.spin_thrust)
        l_layout.addWidget(tweak_group)

        # 3. CODE EDITOR
        l_layout.addWidget(QLabel("GUIDANCE COMPUTER"))
        self.editor = QTextEdit()
        self.editor.setPlaceholderText("# Python Mission Script")
        l_layout.addWidget(self.editor)
        
        # 4. BUTTONS
        btn_layout = QHBoxLayout()
        btn_launch = QPushButton("LAUNCH MISSION")
        btn_launch.setStyleSheet("background-color: green; padding: 15px;")
        btn_launch.clicked.connect(self.launch)
        btn_abort = QPushButton("ABORT")
        btn_abort.setStyleSheet("background-color: red; padding: 15px;")
        btn_abort.clicked.connect(self.abort)
        btn_layout.addWidget(btn_launch)
        btn_layout.addWidget(btn_abort)
        l_layout.addLayout(btn_layout)

        # 5. CONSOLE
        self.console = QTextEdit()
        self.console.setMaximumHeight(150)
        self.console.setReadOnly(True)
        l_layout.addWidget(self.console)

        splitter.addWidget(left)

        # --- RIGHT PANEL: UNIVERSE VIEW ---
        self.viewport = SpaceViewport()
        # Initialize planets in 3D view
        self.viewport.init_bodies(self.physics.bodies)
        splitter.addWidget(self.viewport)
        
        layout.addWidget(splitter)
        splitter.setSizes([500, 1300])

        # Loop
        self.timer = QTimer()
        self.timer.timeout.connect(self.loop)
        self.timer.start(30)

    def log(self, msg):
        self.console.append(f">> {msg}")

    def update_physics(self):
        self.physics.max_thrust = self.spin_thrust.value()
        self.log(f"THRUST UPDATED: {self.physics.max_thrust/1e6:.1f} MN")

    def launch(self):
        self.physics.reset()
        code = self.editor.toPlainText()
        if self.runtime.compile_script(code):
            self.log("MISSION START.")
        else:
            self.log("COMPILATION FAILED.")

    def abort(self):
        self.runtime.is_active = False
        self.physics.thrust_level = 0
        self.log("ABORTED.")

    def loop(self):
        # Physics Step
        self.runtime.execute_step()
        if self.runtime.is_active:
            status = self.physics.step(0.05)
            if status != "FLYING":
                self.runtime.is_active = False
                QMessageBox.information(self, "RESULT", f"MISSION END: {status}")

        # Update Visuals
        self.viewport.update_scene(self.physics)

        # Update HUD
        data = self.physics.get_telemetry()
        self.lbl_alt.setText(f"ALT: {data['alt']/1000:.1f} km")
        self.lbl_vel.setText(f"VEL: {data['vel']:.0f} m/s")
        self.lbl_body.setText(f"NEAR: {data['nearest']}")
        self.lbl_pos.setText(f"X:{data['x']:.1e} Y:{data['y']:.1e}")