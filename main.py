import sys
import os
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from ui.window import MainWindow

def main():
    # 1. High-DPI Fix (Must be first)
    if hasattr(Qt.HighDpiScaleFactorRoundingPolicy, 'PassThrough'):
        QApplication.setHighDpiScaleFactorRoundingPolicy(
            Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)

    # 2. LOAD LOGO
    # We use os.path.join to make sure it works after we build the EXE later
    basedir = os.path.dirname(__file__)
    icon_path = os.path.join(basedir, "assets", "logo.png")

    app.setWindowIcon(QIcon(icon_path))

    # 3. Launch Window
    window = MainWindow()
    window.setWindowIcon(QIcon(icon_path)) # Set it on the window explicitly too
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()