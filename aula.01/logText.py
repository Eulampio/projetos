import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit

class ReverseNameWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Santos")

        self.label_name = QLabel("Ale Santos")
        self.input_name = QLineEdit()

        self.button_reverse = QPushButton("Clique aqui")
        self.button_reverse.clicked.connect(self.reverse_name)

        self.result_label = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(self.label_name)
        layout.addWidget(self.input_name)
        layout.addWidget(self.button_reverse)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def reverse_name(self):
        name = self.input_name.text()
        self.result_label.setText(f"Nome invertido: {name[::-1]}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReverseNameWindow()
    window.show()
    sys.exit(app.exec())
