import pytest
from unittest.mock import Mock, patch
import socket
from user_class import User
from variaveis import *

class TestUserAdmin:

    @pytest.fixture
    def patch_socket(mock_socket):
        """Aplica o patch na biblioteca socket"""
        with patch("socket.socket") as mock_socket:
            yield mock_socket

    @pytest.fixture
    def mock_socket(self, patch_socket):
        """Fixture que cria um Mock para simular um socket"""
        mock_socket = patch_socket
        mock_socket.connect.return_value = None
        mock_socket.settimeout.return_value = None
        mock_socket.send.return_value = None
        mock_socket.recv.return_value = None
        mock_socket.close.return_value = None
        return mock_socket

    @pytest.fixture
    def admin(self, mock_socket):
        """Fixture que retorna uma instância do User admin"""
        return User("Funcionario")
    
    def test_constructor_admin(self, admin: User):
        """Testa o construtor de uma instância User admin"""
        assert admin.nome == "Funcionario"
        assert admin.timeout == 0
        assert admin.endereco == ADDR

        admin.socket_user.connect.assert_called_with(ADDR)
        admin.socket_user.settimeout.assert_not_called
        admin.socket_user.send.assert_called_with("Funcionario".encode())

    def test_admin_nome_setter(self, admin: User):
        """Testa a alteração do nome de um admin"""
        admin.nome = "Funcionario2"
        assert admin.nome == "Funcionario2"
        assert admin.timeout == 0
        assert admin.endereco == ADDR

    def test_admin_timeout_setter(self, admin: User):
        """Testa a alteração do timeout de um admin"""
        admin.timeout = 100
        assert admin.nome == "Funcionario"
        assert admin.timeout == 100
        assert admin.endereco == ADDR

    def test_admin_endereco_setter(self, admin: User):
        """Testa a alteração do endereco de um admin"""
        admin.endereco = ("127.0.0.1", 1001)
        assert admin.nome == "Funcionario"
        assert admin.timeout == 0
        assert admin.endereco == ("127.0.0.1", 1001)

    def test_admin_socket_user_setter(self, admin: User, mock_socket):
        """Testa a alteração do socket_user de um admin"""
        admin.socket_user = mock_socket
        assert admin.nome == "Funcionario"
        assert admin.timeout == 0
        assert admin.endereco == ADDR
        assert admin.socket_user == mock_socket

    def test_admin_iniciar_conexao(self, admin: User):
        """Testa o método iniciar_conexao de um admin"""
        admin.iniciar_conexao()
        admin.socket_user.connect.assert_called_with(ADDR)
        admin.socket_user.settimeout.assert_not_called
        admin.socket_user.send.assert_called_with("Funcionario".encode())

    def test_admin_escutar_mensagens(self, admin: User):
        """Testa o método escutar_mensagens de um admin"""
        mock_callback = Mock()

        admin.socket_user = admin.socket_user
        admin.socket_user.recv.side_effect = [
            "Mensagem 1".encode(),
            "Mensagem 2".encode(),
            Exception,
        ]

        admin.escutar_mensagens(mock_callback)
        admin.socket_user.recv.assert_called_with(BUFFER_SIZE)
        mock_callback.assert_any_call("Mensagem 1")
        mock_callback.assert_any_call("Mensagem 2")

    @pytest.mark.parametrize("mensagem", [
        "Mensagem1",
        "Mensagem2",
        "Mensagem3",
    ])
    def test_admin_enviar_mensagem(self, admin: User, mensagem: str):
        """Testa o método enviar_mensagem de um admin"""
        admin.enviar_mensagem(mensagem)
        admin.socket_user = admin.socket_user
        admin.socket_user.send.assert_called_with(mensagem.encode())

    def test_admin_fechar_conexao(self, admin: User):
        """Testa o método fechar_conexao de um admin"""
        admin.fechar_conexao()
        admin.socket_user.close.assert_called_once()