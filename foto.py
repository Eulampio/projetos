
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

def main():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle('minha foto')

    layout = QVBoxLayout()

    name_label = QLabel('alexandre santos')
    name_label.setAlignment(Qt.AlignCenter)

    image_label = QLabel()
    pixmap = QPixmap(r'metal-slug')  
    image_label.setPixmap(pixmap)
    image_label.setAlignment(Qt.AlignCenter)

    layout.addWidget(name_label)
    layout.addWidget(image_label)

    window.setLayout(layout)

    window.resize(400, 400) 

    window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()