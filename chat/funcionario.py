import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import QThread, pyqtSignal
from user_class import User
from variaveis import NOME_ADMIN
"""
Importações:

1. Importa 'sys', que é usado para interagir com o sistema e acessar os argumentos de linha de comando.
2. Importa widgets e layouts da biblioteca PyQt5 para construir a interface gráfica do funcionário (QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QWidget, QLabel).
3. Importa QThread, pyqtSignal de PyQt5 para gerenciar threads e sinais.
4. Importa a classe 'User' do módulo 'user_class' para gerenciar as ações do usuário (administrador).
5. Importa 'NOME_ADMIN' da variável 'variaveis' para definir o nome do administrador.
"""


class ListenerThread(QThread):
    """
    Classe ListenerThread:

    Gerencia a thread responsável por escutar as mensagens recebidas pelo administrador.

    -> Atributo:
    message_received (pyqtSignal): Sinal que emite mensagens recebidas.
    """
    message_received = pyqtSignal(str)

    def __init__(self, user):
        """
        Construção da classe:

        Inicializa a thread com o usuário fornecido.

        -> Parâmentro:
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


class FuncionarioWindow(QMainWindow):
    """
    Classe FuncionarioWindow:

    Define a janela principal do funcionário para a interface gráfica do chat com o cliente, 
    incluindo a exibição de mensagens e a interação com o usuário.
    """

    def __init__(self):
        """
        Construtor da classe FuncionarioWindow:

        Inicializa a interface gráfica, configura os componentes principais como área de mensagens,
        input de mensagens, botão de enviar, e configura a thread de escuta de mensagens.
        """
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
        """
        Método enviar_mensagem:

        Envia a mensagem digitada pelo administrador e exibe na interface de chat.
        Após o envio, o campo de entrada é limpo.
        """
        mensagem = self.message_input.text()
        if mensagem:
            self.user.enviar_mensagem(mensagem)
            self.chat_display.append(f"Você: {mensagem}")
            self.message_input.clear()

    def exibir_mensagem(self, mensagem):
        """
        Método exibir_mensagem:

        Exibe a mensagem recebida na área de chat. 
        Se a mensagem indicar que um cliente se conectou, o label é atualizado com o nome do cliente.
        """
        self.chat_display.append(mensagem)
        # Atualizar label de cliente se necessário

        if "conectado" in mensagem:
            self.cliente_label.setText(mensagem.split()[0])

    def closeEvent(self, event):
        """
        Método closeEvent:

        Finaliza a conexão do administrador ao fechar a janela, fechando a conexão do usuário.
        """
        self.user.fechar_conexao()
        event.accept()


def main():
    """
    Método closeEvent:

    Finaliza a conexão do administrador ao fechar a janela, fechando a conexão do usuário.
    """
    app = QApplication(sys.argv)
    window = FuncionarioWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
