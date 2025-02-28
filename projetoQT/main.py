from PySide6.QtGui import QPixmap
from UI_tela import Ui_form


class MainWindow (QWidget):
    def __init__ (self):
        super(). __init__ ()
        self.ui = Ui_form ()
        self.ui.setupUI(self)
        self.ui.Open_btn.clicked.connect(self.opem_image)

    def open_image()