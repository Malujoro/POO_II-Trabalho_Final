import pytest
from unittest.mock import MagicMock, patch
import socket
import threading
from server import ChatServer
from variaveis import *

class TestServer:

    @pytest.fixture
    def patch_socket(mock_socket):
        """Aplica o patch na biblioteca socket"""
        with patch("socket.socket") as mock_socket:
            yield mock_socket

    @pytest.fixture
    def mock_socket(self, patch_socket):
        """Fixture que cria um Mock para simular um socket"""
        mock_socket = patch_socket
        mock_socket.bind.return_value = None
        mock_socket.listen.return_value = None
        mock_socket.accept.return_value = None
        mock_socket.close.return_value = None
        return mock_socket
    
    @pytest.fixture
    def mock_conexao(self):
        """Fixture que cria um Mock para simular um socket"""
        mock_conexao = MagicMock()
        mock_conexao.recv.return_value = None
        return mock_conexao
    
    @pytest.fixture
    def server(self, mock_socket):
        return ChatServer()

    def test_constructor_server(self, server):
        """Testa o construtor de uma instância ChatServer"""
        server.server_socket.bind.assert_called_with(ADDR)
        server.server_socket.listen.assert_called_with(TOTAL_USUARIOS)
        assert server.usuarios == {}
        assert server.funcionario_socket == None

    @pytest.mark.parametrize("nome", [
        NOME_CLIENTE,
        NOME_ADMIN,
    ])
    def test_encaminhar_mensagem(self, server, mock_conexao, nome):
        """Testa o método encaminhar_mensagem do Server"""
        server.funcionario_socket = MagicMock()
        
        server.usuarios = {
            NOME_ADMIN: server.funcionario_socket, 
            NOME_CLIENTE: MagicMock(), 
            "Usuario2": MagicMock()
        }

        mock_conexao.recv.side_effect = [
            "Teste".encode(),
            Exception,
        ]

        server.encaminhar_mensagem(mock_conexao, NOME_ADMIN)

        for name, mock in server.usuarios.items():
            if(name != nome):
                mock.send.assert_called_with(f"{NOME_ADMIN}: Teste".encode())

    def test_iniciar_servidor(self, server, mock_conexao):
        server.funcionario_socket = MagicMock()

        mock_conexao.recv.side_effect = [
            NOME_CLIENTE.encode(),
        ]

        server.server_socket.accept.side_effect = [
            (mock_conexao, None),
            KeyboardInterrupt,
        ]

        server.iniciar_servidor()

        server.server_socket.close.has_called_once()
        assert NOME_CLIENTE in server.usuarios