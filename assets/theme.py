DARK_THEME = """
QMainWindow { background-color: #121212; }
QWidget { color: #e0e0e0; font-family: 'Segoe UI', sans-serif; font-size: 10pt; }
QFrame { border: 1px solid #333; border-radius: 4px; background-color: #1e1e1e; }
QGroupBox { font-weight: bold; border: 1px solid #444; margin-top: 10px; }
QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 3px; }
QPushButton {
    background-color: #007acc; color: white; border: none; padding: 8px 16px;
    font-weight: bold; border-radius: 2px;
}
QPushButton:hover { background-color: #0098ff; }
QPushButton#AbortBtn { background-color: #d32f2f; }
QTextEdit { 
    background-color: #0d0d0d; color: #00ff00; 
    font-family: 'Consolas', monospace; font-size: 11pt; border: 1px solid #444; 
}
QLabel#Header { font-size: 14pt; font-weight: bold; color: #00aaff; }
QLabel#Telemetry { font-size: 12pt; font-weight: bold; color: #00ffcc; }
"""