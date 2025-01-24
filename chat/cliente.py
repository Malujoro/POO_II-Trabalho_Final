import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
from user_class import User
from variaveis import NOME_CLIENTE

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
        self.message_input.setPlaceholderText("Digite sua mensagem")
        layout.addWidget(self.message_input)

        # Botão de enviar
        send_button = QPushButton("Enviar")
        send_button.clicked.connect(self.enviar_mensagem)
        layout.addWidget(send_button)

        # Enviar mensagem com Enter
        self.message_input.returnPressed.connect(self.enviar_mensagem)

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

            # Temporizador para desconectar após 1 minuto se funcionário não conectado
            self.desconectar_timer = QTimer()
            self.desconectar_timer.timeout.connect(self.fechar_por_timeout)
            self.desconectar_timer.start(60000)  # 1 minuto

        except Exception as e:
            self.chat_display.append(f"Erro de conexão: {e}")
            self.close()

        # Timer de inatividade
        self.inactivity_timer = QTimer(self)
        self.inactivity_timer.timeout.connect(self.fechar_por_timeout)
        self.inactivity_timer.start(180000)  # 3 minutos (em milissegundos)

    def enviar_mensagem(self):
        mensagem = self.message_input.text()
        if mensagem:
            self.user.enviar_mensagem(mensagem)
            self.chat_display.append(f"Você: {mensagem}")
            self.message_input.clear()
            self.resetar_timer() #reinicia o temporizador após enviar msg

    def exibir_mensagem(self, mensagem):
        self.chat_display.append(mensagem)

        # Parar o temporizador se funcionário conectar
        if "Funcionário conectado" in mensagem:
            self.desconectar_timer.stop()

    def fechar_por_timeout(self):
        self.chat_display.append("Sessão encerrada por inatividade. Conecte novamente mais tarde.")
        self.close()

    def resetar_timer(self):
        self.inactivity_timer.stop()
        self.inactivity_timer.start(180000) #reinicia pra 3 min

    def closeEvent(self, event):
        self.user.enviar_mensagem("DESCONECTAR")
        self.user.fechar_conexao()
        event.accept()

def main():
    app = QApplication(sys.argv)
    window = ClientWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
