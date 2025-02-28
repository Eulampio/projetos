import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit



class ReverseNameWindow( QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()


         
    def init_ui(self ):
        self.setWindowTitle("santos")
       
        self.layout_name =QLabel ("alesantos")
        self.input_name =QLineEdit()

        self.button_reserse = QPushButton ("clique aqui" )
        self.button_reserse.clicked.connect(self.reverse_name)

        self.result_label = QLabel("")

        layout =QVBoxLayout()

        layout.addWidget(self.layout_name)
        layout.addWidget(self.input_name)
        layout.addWidget(self.button_reserse)
        layout.addWidget(self.result_label)

    def reverse_name(self):
        name = self.input_name.text()
        self.result_label.setText (f"nome imvertido: {name}")

if __name__== "__main__":
        app = QApplication(sys.argv)
        window = ReverseNameWindow()
        window.show ()

        sys.exit(app.exec())





