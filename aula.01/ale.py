import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel

# Cria a aplicação
app = QApplication(sys.argv)

# Cria a janela principal
window = QWidget()
window.setWindowTitle('Exemplo de PySide6')
window.setGeometry(100, 100, 400, 300)

# Cria um label com texto
label = QLabel('alexandre', window)
label.move(100, 100)

# Exibe a janela
window.show()

# Executa o loop da aplicação
sys.exit(app.exec())






