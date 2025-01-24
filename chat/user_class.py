import socket
import threading
from variaveis import *
"""
Importações:
1. Importa o módulo socket para criação e manipulação de conexões de rede.
2. Importa o módulo threading para criar e gerenciar threads no código, permitindo execução concorrente.
3. Importa todas as variáveis definidas no módulo 'variaveis.py', como configurações de rede e mensagens.
"""


class User:
    """
    Classe User:

    Esta classe gerencia a conexão de um usuário com o servidor de chat.
    Um usuário pode ser um cliente ou funcionário, e a classe lida com as operações de conexão, 
    envio e recebimento de mensagens, além do gerenciamento do timeout de conexão.
    """

    def __init__(self, nome: str, timeout: int = 0, endereco: tuple[str, int] = ADDR):
        """
        Construtor da classe User:

        Inicializa uma instância de usuário, configurando o nome, timeout e endereço de conexão.
        Também cria o socket de rede e chama o método de inicialização da conexão.

        -> Parâmetros (privados):
        nome (str): Nome do usuário.
        timeout (int): Tempo de timeout para a conexão, em segundos (padrão: 0).
        endereco (tuple[str, int]): Endereço do servidor com o qual o usuário se conecta (padrão: ENDERECO).
        socket_user (socket.socket): O socket de rede do usuário para comunicação com o servidor.
        """
        self._nome = nome
        self._timeout = timeout
        self._endereco = endereco
        self._socket_user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.iniciar_conexao()

    @property
    def nome(self) -> str:
        """Getter do nome do usuário"""
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        """Setter do nome do usuário"""
        self._nome = nome

    @property
    def timeout(self) -> int:
        """Getter do tempo de timeout da conexão"""
        return self._timeout

    @timeout.setter
    def timeout(self, timeout: int) -> None:
        """Setter do tempo de timeout da conexão"""
        self._timeout = timeout

    @property
    def endereco(self) -> tuple[str, int]:
        """Getter do endereço de conexão do usuário"""
        return self._endereco

    @endereco.setter
    def endereco(self, endereco: tuple[str, int]) -> None:
        """Setter do endereço de conexão do usuário"""
        self._endereco = endereco

    @property
    def socket_user(self) -> socket.socket:
        """Getter do socket de rede do usuário"""
        return self._socket_user

    @socket_user.setter
    def socket_user(self, socket_user: socket.socket) -> None:
        """Setter do socket de rede do usuário"""
        self._socket_user = socket_user

    def iniciar_conexao(self):
        """
        Método iniciar_conexao:

        Estabelece a conexão com o servidor utilizando o socket configurado.
        Caso o timeout seja maior que zero, ele define o tempo limite de conexão.
        Envia o nome do usuário para o servidor após a conexão ser estabelecida.
        """
        try:
            self._socket_user.connect(self._endereco)
            if self._timeout > 0:
                self._socket_user.settimeout(self._timeout)

            self._socket_user.send(self._nome.encode())
        except Exception as e:
            print(f"Erro ao conectar: {e}")
            raise

    def escutar_mensagens(self, callback):
        """
        Método escutar_mensagens:

        Fica em um loop escutando por mensagens do servidor. Quando uma mensagem é recebida,
        ela é passada para o callback para ser processada.
        Trata erros de timeout e outros erros relacionados à conexão.

        -> Parâmetro:
        callback (function): Função a ser chamada quando uma mensagem for recebida.
        """
        while True:
            try:
                msg = self._socket_user.recv(BUFFER_SIZE).decode()
                if msg:
                    callback(msg)
            except socket.timeout:
                print("\nTimeout de conexão")
                break
            except Exception as e:
                print(f"\nErro ao receber mensagem: {e}")
                break

    def enviar_mensagem(self, mensagem):
        """
        Método enviar_mensagem:

        Envia uma mensagem para o servidor.

        -> Parâmetro:
        mensagem (str): A mensagem a ser enviada ao servidor.
        """
        try:
            self._socket_user.send(mensagem.encode())
        except Exception as e:
            print(f"Erro ao enviar mensagem: {e}")

    def fechar_conexao(self):
        """
        Método fechar_conexao:

        Fecha a conexão do socket do usuário com o servidor de forma segura.
        """
        try:
            self._socket_user.close()
        except:
            pass
