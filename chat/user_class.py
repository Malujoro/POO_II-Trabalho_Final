import socket
import threading
from variaveis import *

class User:
    def __init__(self, nome, timeout=0, endereco=ADDR):
        self._nome = nome
        self._timeout = timeout
        self._endereco = endereco
        self._socket_user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            self._socket_user.connect(endereco)
            if timeout > 0:
                self._socket_user.settimeout(timeout)
            
            # Enviar nome ao conectar
            self._socket_user.send(self._nome.encode())
        except Exception as e:
            print(f"Erro ao conectar: {e}")
            raise

    def escutar_mensagens(self, callback):
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
        try:
            self._socket_user.send(mensagem.encode())
        except Exception as e:
            print(f"Erro ao enviar mensagem: {e}")

    def fechar_conexao(self):
        try:
            self._socket_user.close()
        except:
            pass
