from PySide6.QtWidgets import  QApplication, QLabel, QMainWindow,QVBoxLayout,QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys

class Helloworldwindow(QMainWindow):
    def __init__(self):
        super().__init__()
         
        self.setWindowTitle("santos")
        self.setGeometry(150,80,100,300)# x,y

        central_widget=QWidget(self)
        layout=QVBoxLayout(central_widget)
             

        label= QLabel ("alesantos", self)
        label.setGeometry(400,400,400,400)# mudando a fonte set + a função
        label.setStyleSheet("font-size: 40px; font-weight: bold; text-align: center")
        label.setAlignment(Qt.AlignCenter)
        
        
        
        
        img_label=QLabel(self)         # Carregar a imagem no QPixmap
        pixmap = QPixmap("metal-slug-prisioner") # Aqui você coloca o caminho da sua imagem
        
        img_label.setPixmap(pixmap) # Colocar a imagem no QLabel
        img_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)
        layout.addWidget(img_label)

        self.setCentralWidget(central_widget)
        

                
if __name__== "__main__":
        app = QApplication(sys.argv)
        window = Helloworldwindow()
        window.show ()

        sys.exit(app.exec())
