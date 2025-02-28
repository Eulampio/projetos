from PySide6.QtWidgets import  QApplication, QLabel, QMainWindow
from PySide6.QtCore import Qt
import sys

class Helloworldwindow(QMainWindow):
    def __init__(self):
        super().__init__()
         
        self.setWindowTitle("Exercicio 2")
        self.setGeometry(150,80,100,300)# x,y

        label= QLabel ("alexandre", self)
        label.setGeometry(400,400,400,400)# mudando a fonte set + a função
        label.setStyleSheet("font-size: 40px; font-weight: bold; text-align: center")
        label.setAlignment(Qt.AlignCenter)
        
        self.setCentralWidget(label)
if __name__== "__main__":
        app = QApplication(sys.argv)
        window = Helloworldwindow()
        window.show ()

        sys.exit(app.exec())

