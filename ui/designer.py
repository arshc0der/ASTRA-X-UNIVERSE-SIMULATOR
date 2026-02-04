from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QFormLayout, QDoubleSpinBox, 
                             QPushButton, QLabel, QGroupBox, QFrame)
from PyQt6.QtCore import pyqtSignal, Qt

class RocketDesigner(QFrame):
    on_launch_ready = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.setFrameStyle(QFrame.Shape.StyledPanel | QFrame.Shadow.Raised)
        
        layout = QVBoxLayout(self)
        
        lbl = QLabel("ROCKET CONFIGURATION LAB")
        lbl.setObjectName("Header")
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(lbl)

        # Input Group
        group = QGroupBox("Design Parameters")
        form = QFormLayout(group)
        
        self.mass_spin = QDoubleSpinBox()
        self.mass_spin.setRange(1000, 200000)
        self.mass_spin.setValue(50000)
        self.mass_spin.setSuffix(" kg")
        form.addRow("Dry Mass:", self.mass_spin)
        
        self.fuel_spin = QDoubleSpinBox()
        self.fuel_spin.setRange(10, 5000)
        self.fuel_spin.setValue(100)
        self.fuel_spin.setSuffix(" Units")
        form.addRow("Fuel Capacity:", self.fuel_spin)
        
        self.thrust_spin = QDoubleSpinBox()
        self.thrust_spin.setRange(100000, 50000000)
        self.thrust_spin.setValue(7600000)
        self.thrust_spin.setSuffix(" N")
        form.addRow("Engine Thrust:", self.thrust_spin)
        
        layout.addWidget(group)
        
        # Launch Button
        btn = QPushButton("INITIALIZE FLIGHT SYSTEMS")
        btn.setFixedHeight(45)
        btn.clicked.connect(self.submit)
        layout.addWidget(btn)

    def submit(self):
        config = {
            'mass': self.mass_spin.value(),
            'fuel': self.fuel_spin.value(),
            'thrust': self.thrust_spin.value()
        }
        self.on_launch_ready.emit(config)