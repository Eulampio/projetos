 
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtCore import Qt

def main():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle('Este é ,meu nome')

    label = QLabel('alexandre santos', parent=window)
    label.setAlignment(Qt.AlignCenter)  

    window.resize(400,400)

    window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
