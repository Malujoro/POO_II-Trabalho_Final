import socket
import threading
from variaveis import *

class User:
    def __init__(self, nome: str, timeout: int=0, endereco: tuple[str, int]=ADDR):
        self._nome = nome
        self._timeout = timeout
        self._endereco = endereco
        self._socket_user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.iniciar_conexao()
        
    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome

    @property
    def timeout(self) -> int:
        return self._timeout
    
    @timeout.setter
    def timeout(self, timeout: int) -> None:
        self._timeout = timeout

    @property
    def endereco(self) -> tuple[str, int]:
        return self._endereco
    
    @endereco.setter
    def endereco(self, endereco: tuple[str, int]) -> None:
        self._endereco = endereco

    @property
    def socket_user(self) -> socket.socket:
        return self._socket_user
    
    @socket_user.setter
    def socket_user(self, socket_user: socket.socket) -> None:
        self._socket_user = socket_user
    
    def iniciar_conexao(self):
        try:
            self._socket_user.connect(self._endereco)
            if self._timeout > 0:
                self._socket_user.settimeout(self._timeout)
            
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
