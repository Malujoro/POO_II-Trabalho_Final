import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
from user_class import User
from variaveis import NOME_CLIENTE
"""
Importações:

1. Importa 'sys', que é usado para interagir com o sistema e acessar os argumentos de linha de comando.
2. Importa widgets e layouts da biblioteca PyQt5 para construir a interface gráfica do cliente de chat (QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QWidget).
3. Importa QThread, pyqtSignal, QTimer do PyQt5 para gerenciar threads, sinais e temporizadores.
4. Importa a classe 'User' do módulo 'user_class' para gerenciar as ações do usuário no chat.
5. Importa 'NOME_CLIENTE' da variável 'variaveis' para definir o nome do cliente.
"""


class ListenerThread(QThread):
    """
    Classe ListenerThread:

    Gerencia a thread responsável por escutar as mensagens recebidas pelo usuário.

    -> Atributo:
    message_received (pyqtSignal): Sinal que emite mensagens recebidas.
    """
    message_received = pyqtSignal(str)

    def __init__(self, user):
        """
        Construção da classe:

        Inicializa a thread com o usuário fornecido.

        -> Atributo:
        user (User): Instância do usuário para interação com o chat.
        """
        super().__init__()
        self.user = user

    def run(self):
        """
        Método run:

        Inicia a escuta de mensagens e emite as mensagens recebidas usando o sinal message_received.
        """
        self.user.escutar_mensagens(self.message_received.emit)


class ClientWindow(QMainWindow):
    """
    Classe ClientWindow:

    Define a janela principal do cliente de chat, incluindo a interface gráfica e a lógica de interação com o chat.
    """

    def __init__(self):
        """
        Contrução da classe:

        Inicializa a interface gráfica e configura os componentes principais, como área de mensagens, 
        input de mensagens, botão de enviar e a thread de escuta de mensagens.
        """
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
        """
        Método enviar_mensagem:

        Envia a mensagem digitada pelo usuário e exibe na interface de chat.
        Após o envio, o temporizador de inatividade é reiniciado.
        """
        mensagem = self.message_input.text()
        if mensagem:
            self.user.enviar_mensagem(mensagem)
            self.chat_display.append(f"Você: {mensagem}")
            self.message_input.clear()
            self.resetar_timer()  # reinicia o temporizador após enviar msg

    def exibir_mensagem(self, mensagem):
        """
        Método exibir_mensagem:

        Exibe a mensagem recebida na área de chat. 
        Se a mensagem indicar que o funcionário está conectado, o temporizador de desconexão é parado.
        """
        self.chat_display.append(mensagem)

        # Parar o temporizador se funcionário conectar
        if "Funcionário conectado" in mensagem:
            self.desconectar_timer.stop()

    def fechar_por_timeout(self):
        """
        Método fechar_por_timeout:

        Encerra a sessão do usuário se o tempo limite de inatividade for atingido.
        Exibe uma mensagem na interface antes de fechar a janela.
        """
        self.chat_display.append(
            "Sessão encerrada por inatividade. Conecte novamente mais tarde.")
        self.close()

    def resetar_timer(self):
        """
        Método resetar_timer:

        Reinicia o temporizador de inatividade para 3 minutos.
        """
        self.inactivity_timer.stop()
        self.inactivity_timer.start(180000)  # reinicia pra 3 min

    def closeEvent(self, event):
        """
        Método closeEvent:

        Envia uma mensagem de desconexão e fecha a conexão com o usuário ao fechar a janela.
        """
        self.user.enviar_mensagem("DESCONECTAR")
        self.user.fechar_conexao()
        event.accept()


def main():
    """
    Função main:

    Inicializa a aplicação PyQt5, cria a janela do cliente e inicia o loop de eventos.
    """
    app = QApplication(sys.argv)
    window = ClientWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
