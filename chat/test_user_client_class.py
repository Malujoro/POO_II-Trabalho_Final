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
    def usuario(self, mock_socket):
        """Fixture que retorna uma instância do User usuário"""
        return User("Usuario", 300, ADDR)

    def test_constructor_usuario(self, usuario: User):
        """Testa o construtor de uma instância User usuário"""
        assert usuario.nome == "Usuario"
        assert usuario.timeout == 300
        assert usuario.endereco == ADDR

        usuario.socket_user.connect.assert_called_with(ADDR)
        usuario.socket_user.settimeout.assert_not_called
        usuario.socket_user.send.assert_called_with("Usuario".encode())

    def test_usuario_nome_setter(self, usuario: User):
        """Testa a alteração do nome de um usuário"""
        usuario.nome = "Usuario2"
        assert usuario.nome == "Usuario2"
        assert usuario.timeout == 300
        assert usuario.endereco == ADDR

    def test_usuario_timeout_setter(self, usuario: User):
        """Testa a alteração do timeout de um usuário"""
        usuario.timeout = 100
        assert usuario.nome == "Usuario"
        assert usuario.timeout == 100
        assert usuario.endereco == ADDR

    def test_usuario_endereco_setter(self, usuario: User):
        """Testa a alteração do endereco de um usuário"""
        usuario.endereco = ("127.0.0.1", 1001)
        assert usuario.nome == "Usuario"
        assert usuario.timeout == 300
        assert usuario.endereco == ("127.0.0.1", 1001)

    def test_usuario_socket_user_setter(self, usuario: User, mock_socket):
        """Testa a alteração do socket_user de um usuário"""
        usuario.socket_user = mock_socket
        assert usuario.nome == "Usuario"
        assert usuario.timeout == 300
        assert usuario.endereco == ADDR
        assert usuario.socket_user == mock_socket

    def test_usuario_iniciar_conexao(self, usuario: User):
        """Testa o método iniciar_conexao de um usuário"""
        usuario.iniciar_conexao()
        usuario.socket_user.connect.assert_called_with(ADDR)
        usuario.socket_user.settimeout.assert_not_called
        usuario.socket_user.send.assert_called_with("Usuario".encode())

    def test_usuario_escutar_mensagens(self, usuario: User):
        """Testa o método escutar_mensagens de um usuário"""
        mock_callback = Mock()

        usuario.socket_user = usuario.socket_user
        usuario.socket_user.recv.side_effect = [
            "Mensagem 1".encode(),
            "Mensagem 2".encode(),
            Exception,
        ]

        usuario.escutar_mensagens(mock_callback)
        usuario.socket_user.recv.assert_called_with(BUFFER_SIZE)
        mock_callback.assert_any_call("Mensagem 1")
        mock_callback.assert_any_call("Mensagem 2")

    @pytest.mark.parametrize("mensagem", [
        "Mensagem1",
        "Mensagem2",
        "Mensagem3",
    ])
    def test_usuario_enviar_mensagem(self, usuario: User, mensagem: str):
        """Testa o método enviar_mensagem de um usuário"""
        usuario.enviar_mensagem(mensagem)
        usuario.socket_user = usuario.socket_user
        usuario.socket_user.send.assert_called_with(mensagem.encode())

    def test_usuario_fechar_conexao(self, usuario: User):
        """Testa o método fechar_conexao de um usuário"""
        usuario.fechar_conexao()
        usuario.socket_user.close.assert_called_once()