import socket
import threading
from variaveis import *
"""
Importações:

1. Importa 'socket', que é usado para comunicação de rede através de TCP/IP.
2. Importa 'threading', que é usado para criar e gerenciar threads no servidor.
3. Importa variáveis do módulo 'variaveis' que contêm parâmetros como endereço, nome de usuário e configuração do servidor.
"""


class ChatServer:
    """
    Classe ChatServer:

    Esta classe gerencia o servidor de chat, que permite a comunicação entre um administrador (funcionário) e múltiplos clientes.
    O servidor escuta as conexões dos usuários, recebe e encaminha mensagens, e gerencia as desconexões.
    """

    def __init__(self):
        """
        Construtor da classe ChatServer:

        Inicializa o servidor, cria o socket de rede e configura a escuta de conexões.

        -> Atributos:
        server_socket (socket.socket): O socket usado para comunicação de rede.
        usuarios (dict): Dicionário que mantém as conexões dos usuários, usando seus nomes como chave.
        funcionario_socket (socket.socket): O socket do funcionário conectado (admin).
        lock (threading.Lock): Objeto de bloqueio usado para garantir acesso seguro ao dicionário de usuários em ambientes concorrentes.
        """
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(ADDR)
        self.server_socket.listen(TOTAL_USUARIOS)

        self.usuarios = {}
        self.funcionario_socket = None
        self.lock = threading.Lock()

    def encaminhar_mensagem(self, conexao, nome):
        """
        Método encaminhar_mensagem:

        Recebe as mensagens de um usuário (cliente ou funcionário) e as encaminha para o destinatário apropriado.
        Se o remetente for o administrador (funcionário), as mensagens são enviadas para os clientes. 
        Caso contrário, são enviadas para o administrador.

        Parâmetros:
        conexao (socket.socket): O socket da conexão com o usuário.
        nome (str): O nome do usuário que está enviando a mensagem.
        """
        try:
            while True:
                mensagem = conexao.recv(BUFFER_SIZE).decode()
                if not mensagem:
                    break

                # Verifica o remetente
                if nome == NOME_ADMIN:
                    # Se for admin, envia para o cliente
                    for user_nome, user_socket in list(self.usuarios.items()):
                        if user_nome != NOME_ADMIN:
                            try:
                                user_socket.send(
                                    f"{nome}: {mensagem}".encode())
                            except (BrokenPipeError, ConnectionResetError):
                                print(f"Erro ao enviar mensagem para o cliente {
                                      user_nome}.")
                                self.desconectar_usuario(
                                    user_socket, user_nome)
                else:
                    # Se for cliente, envia para o admin
                    if self.funcionario_socket:
                        try:
                            self.funcionario_socket.send(
                                f"{nome}: {mensagem}".encode())
                        except (BrokenPipeError, ConnectionResetError):
                            print("Erro ao enviar mensagem para o funcionário.")
                            self.desconectar_usuario(
                                self.funcionario_socket, NOME_ADMIN)

        except Exception as e:
            print(f"Erro ao encaminhar mensagem: {e}")
        finally:
            self.desconectar_usuario(conexao, nome)

    def desconectar_usuario(self, conexao, nome):
        """
        Método desconectar_usuario:

        Desconecta um usuário, fechando sua conexão e notificando os outros usuários.
        Se o usuário for o administrador, desconecta todos os clientes e limpa a lista de usuários.

        Parâmetros:
        conexao (socket.socket): O socket da conexão com o usuário a ser desconectado.
        nome (str): O nome do usuário a ser desconectado.
        """
        with self.lock:
            if nome in self.usuarios:
                del self.usuarios[nome]

            conexao.close()

            if nome == NOME_ADMIN:
                print(f"Funcionario {nome} desconectado")
                self.funcionario_socket = None

                for user_nome, user_socket in self.usuarios.items():
                    try:
                        user_socket.send(
                            "O funcionário se desconectou. O atendimento será encerrado.".encode())
                    except (BrokenPipeError, ConnectionResetError):
                        print(f"Erro ao notificar cliente {
                              user_nome} sobre a desconexão do funcionário.")
                    finally:
                        user_socket.close()

                self.usuarios.clear()

            else:
                print(f"Cliente {nome} desconectado")
                if self.funcionario_socket:
                    try:
                        self.funcionario_socket.send(
                            f"Cliente {nome} desconectado".encode())
                    except (BrokenPipeError, ConnectionResetError):
                        print(
                            "Erro ao notificar o funcionário sobre a desconexão do cliente.")

    def iniciar_servidor(self):
        """
        Método iniciar_servidor:

        Inicia o servidor de chat. O servidor escuta por conexões de clientes e funcionários, 
        aceita as conexões e cria threads para gerenciar o envio e recebimento de mensagens.

        Quando um cliente se conecta, o servidor verifica se há um funcionário disponível para atendê-lo.
        Caso o funcionário já esteja conectado, a conexão com o cliente é estabelecida. Caso contrário, o cliente é informado de que o atendimento não está disponível.

        O servidor roda indefinidamente até ser interrompido manualmente.
        """
        print(f"Servidor rodando na porta {PORT}")

        while True:
            try:
                client_socket, _ = self.server_socket.accept()
                nome_usuario = client_socket.recv(BUFFER_SIZE).decode()

                with self.lock:
                    if nome_usuario == NOME_ADMIN:
                        # Verifica se já existe um funcionário
                        if self.funcionario_socket:
                            client_socket.send(
                                "Já existe um funcionário conectado.".encode())
                            client_socket.close()
                            continue

                        self.funcionario_socket = client_socket
                        self.usuarios[nome_usuario] = client_socket
                        print(f"Funcionário {nome_usuario} conectado")

                    else:
                        # Verifica se há funcionário disponível
                        if not self.funcionario_socket:
                            client_socket.send(
                                MENSAGEM_ATENDIMENTO_INDISPONIVEL.encode())
                            client_socket.close()
                            continue

                        self.usuarios[nome_usuario] = client_socket
                        print(f"Cliente {nome_usuario} conectado")
                        self.funcionario_socket.send(
                            f"Cliente {nome_usuario} conectado".encode())

                # Cria thread para lidar com as mensagens
                thread = threading.Thread(
                    target=self.encaminhar_mensagem,
                    args=(client_socket, nome_usuario),
                    daemon=True
                )
                thread.start()

            except KeyboardInterrupt:
                break

        self.server_socket.close()


def main_server():
    """
    Função main_server:

    Inicializa o servidor de chat e inicia o loop para aceitar e gerenciar conexões de clientes e funcionários.
    """
    servidor = ChatServer()
    servidor.iniciar_servidor()


if __name__ == "__main__":
    main_server()
