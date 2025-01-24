import socket
import threading
from variaveis import *

class ChatServer:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(ADDR)
        self.server_socket.listen(TOTAL_USUARIOS)
        
        self.usuarios = {}
        self.funcionario_socket = None
        self.lock = threading.Lock()


    def encaminhar_mensagem(self, conexao, nome):
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
                                user_socket.send(f"{nome}: {mensagem}".encode())
                            except (BrokenPipeError, ConnectionResetError):
                                print(f"Erro ao enviar mensagem para o cliente {user_nome}.")
                                self.desconectar_usuario(user_socket, user_nome)
                else:
                    # Se for cliente, envia para o admin
                    if self.funcionario_socket:
                        try:
                            self.funcionario_socket.send(f"{nome}: {mensagem}".encode())
                        except (BrokenPipeError, ConnectionResetError):
                            print("Erro ao enviar mensagem para o funcionário.")
                            self.desconectar_usuario(self.funcionario_socket, NOME_ADMIN)

        except Exception as e:
            print(f"Erro ao encaminhar mensagem: {e}")
        finally:
            self.desconectar_usuario(conexao, nome)
    

    def desconectar_usuario(self, conexao, nome):
        with self.lock:
            if nome in self.usuarios:
                del self.usuarios[nome]

            conexao.close()
        
            if nome == NOME_ADMIN:
                print(f"Funcionario {nome} desconectado")
                self.funcionario_socket = None

                for user_nome, user_socket in self.usuarios.items():
                    try:
                        user_socket.send("O funcionário se desconectou. O atendimento será encerrado.".encode())
                    except (BrokenPipeError, ConnectionResetError):
                        print(f"Erro ao notificar cliente {user_nome} sobre a desconexão do funcionário.")
                    finally:
                        user_socket.close()

                self.usuarios.clear()

            else:
                print(f"Cliente {nome} desconectado")
                if self.funcionario_socket:
                    try:
                        self.funcionario_socket.send(f"Cliente {nome} desconectado".encode())
                    except (BrokenPipeError, ConnectionResetError):
                        print("Erro ao notificar o funcionário sobre a desconexão do cliente.")

    def iniciar_servidor(self):
        print(f"Servidor rodando na porta {PORT}")
        
        while True:
            try:
                client_socket, _ = self.server_socket.accept()
                nome_usuario = client_socket.recv(BUFFER_SIZE).decode()

                with self.lock:
                    if nome_usuario == NOME_ADMIN:
                        # Verifica se já existe um funcionário
                        if self.funcionario_socket:
                            client_socket.send("Já existe um funcionário conectado.".encode())
                            client_socket.close()
                            continue
                        
                        self.funcionario_socket = client_socket
                        self.usuarios[nome_usuario] = client_socket
                        print(f"Funcionário {nome_usuario} conectado")

                    else:
                        # Verifica se há funcionário disponível
                        if not self.funcionario_socket:
                            client_socket.send(MENSAGEM_ATENDIMENTO_INDISPONIVEL.encode())
                            client_socket.close()
                            continue
                        
                        self.usuarios[nome_usuario] = client_socket
                        print(f"Cliente {nome_usuario} conectado")
                        self.funcionario_socket.send(f"Cliente {nome_usuario} conectado".encode())

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

def main():
    servidor = ChatServer()
    servidor.iniciar_servidor()

if __name__ == "__main__":
    main()