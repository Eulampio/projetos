import sys
from PySide6.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QWidget,QHBoxLayout
from Main import main

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tela de Login")

        
        self.label_usuario = QLabel("Usuário:")
        self.input_usuario = QLineEdit()
        self.label_senha = QLabel("Senha:")
        self.input_senha = QLineEdit()
        self.input_senha.setEchoMode(QLineEdit.Password)
        self.botao_entrar = QPushButton("Entrar")
        self.botao_cancelar = QPushButton("Cancelar")

        
        self.botao_entrar.clicked.connect(self.verificar_login)
        self.botao_cancelar.clicked.connect(self.reject)

        
        layout_login = QVBoxLayout()
        layout_login.addWidget(self.label_usuario)
        layout_login.addWidget(self.input_usuario)
        layout_login.addWidget(self.label_senha)
        layout_login.addWidget(self.input_senha)
        layout_login.addWidget(self.botao_entrar)
        layout_login.addWidget(self.botao_cancelar)
        

        widget_central = QWidget()
        widget_central.setLayout(layout_login)


        layout_principal = QHBoxLayout()
        layout_principal = QHBoxLayout()
        layout_principal.addStretch(1)
        layout_principal.addWidget(widget_central)
        layout_principal.addStretch(1)

        layout_vertical = QVBoxLayout()
        layout_vertical.addStretch(1)
        layout_vertical.addLayout(layout_principal)
        layout_vertical.addStretch(1)


        self.setLayout(layout_vertical)






    def verificar_login(self):
        usuario = self.input_usuario.text()
        senha = self.input_senha.text()

        
        if usuario == "santos" and senha == "santo":
            QMessageBox.information(self, "Sucesso", "Login bem-sucedido!")
            self.accept()
        else:
            QMessageBox.warning(self, "Erro", "Usuário ou senha incorretos.")

