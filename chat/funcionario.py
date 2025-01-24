import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import QThread, pyqtSignal
from user_class import User
from variaveis import NOME_ADMIN

class ListenerThread(QThread):
    message_received = pyqtSignal(str)

    def __init__(self, user):
        super().__init__()
        self.user = user

    def run(self):
        self.user.escutar_mensagens(self.message_received.emit)

class FuncionarioWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chat Funcionário")
        self.resize(500, 600)

        # Layout principal
        layout = QVBoxLayout()

        # Área de mensagens
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        layout.addWidget(self.chat_display)

        # Label para mostrar cliente atual
        self.cliente_label = QLabel("Nenhum cliente conectado")
        layout.addWidget(self.cliente_label)

        # Input de mensagem
        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText("Digite sua mensagem")
        self.message_input.returnPressed.connect(self.enviar_mensagem)
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
            self.user = User(NOME_ADMIN)
            
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
        # Atualizar label de cliente se necessário
        
        if "conectado" in mensagem:
            self.cliente_label.setText(mensagem.split()[0])

    def closeEvent(self, event):
        self.user.fechar_conexao()
        event.accept()

def main():
    app = QApplication(sys.argv)
    window = FuncionarioWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()