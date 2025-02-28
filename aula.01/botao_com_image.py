from PySide6.QtWidgets import  QApplication, QLabel, QMainWindow,QVBoxLayout,QWidget,QPushButton
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
        label.setGeometry(400,400,400,400)
        label.setStyleSheet("font-size: 40px; font-weight: bold; text-align: center")
        label.setAlignment(Qt.AlignCenter)
        
        
        
        
        img_label=QLabel(self)  
        pixmap = QPixmap("metal-slug-prisioner")
        img_label.setPixmap(pixmap)
        img_label.setAlignment(Qt.AlignCenter)


        button= QPushButton ("clique aqui" ,self)
        button.setStyleSheet('front-size: 16px; padding: 10px;')
        button.clicked.connect(self.on_click_button)


        layout.addWidget(label)
        layout.addWidget(img_label)
        layout.addWidget(button)

        self.setCentralWidget(central_widget)

    def on_click_button(self):
         print("botão clicado")
        

                
if __name__== "__main__":
        app = QApplication(sys.argv)
        window = Helloworldwindow()
        window.show ()

        sys.exit(app.exec())
