import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QThread, pyqtSignal
from user_class import User
from variaveis import NOME_CLIENTE, ADDR

class ListenerThread(QThread):
    message_received = pyqtSignal(str)

    def __init__(self, user):
        super().__init__()
        self.user = user

    def run(self):
        self.user.escutar_mensagens(self.message_received.emit)

class ClientWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chat Cliente")
        self.resize(400, 500)

        # Layout principal
        layout = QVBoxLayout()

        # Área de mensagens
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        layout.addWidget(self.chat_display)

        # Input de mensagem
        self.message_input = QLineEdit()
        layout.addWidget(self.message_input)

        # Botão de enviar
        send_button = QPushButton("Enviar")
        send_button.clicked.connect(self.enviar_mensagem)
        layout.addWidget(send_button)

        # Widget central
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Configurar usuário
        try:
            self.user = User(NOME_CLIENTE)
            
            # Thread de escuta
            self.listener_thread = ListenerThread(self.user)
            self.listener_thread.message_received.connect(self.exibir_mensagem)
            self.listener_thread.start()

        except Exception as e:
            self.chat_display.append(f"Erro de conexão: {e}")
            self.close()

    def enviar_mensagem(self):
        mensagem = self.message_input.text()
        if mensagem:
            self.user.enviar_mensagem(mensagem)
            self.chat_display.append(f"Você: {mensagem}")
            self.message_input.clear()

    def exibir_mensagem(self, mensagem):
        self.chat_display.append(mensagem)

    def closeEvent(self, event):
        self.user.fechar_conexao()
        event.accept()

def main():
    app = QApplication(sys.argv)
    window = ClientWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()