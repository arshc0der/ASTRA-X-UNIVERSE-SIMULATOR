import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from ui.window import MainWindow

def main():
    # --- CRITICAL FIX FOR 4K/RETINA SCREENS ---
    # This must be called BEFORE creating QApplication
    if hasattr(Qt.HighDpiScaleFactorRoundingPolicy, 'PassThrough'):
        QApplication.setHighDpiScaleFactorRoundingPolicy(
            Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    # Initialize the Application
    app = QApplication(sys.argv)
    
    # Create the Main Interface
    window = MainWindow()
    window.show()
    
    # Start the Event Loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()