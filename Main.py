
class main ():
    def __init__(self,):
    

        if __name__ == "__main__":
            app = QApplication(sys.argv)
            login = LoginDialog()
            login.showFullScreen()  # Exibe a janela em tela cheia
            sys.exit(app.exec())

            if login.exec() == QDialog.Accepted:
    
                print("Login realizado com sucesso!")
            sys.exit(app.exec())