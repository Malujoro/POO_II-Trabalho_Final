import pytest
from unittest.mock import Mock, patch
import socket
from .user_class import User
from .variaveis import *

"""
Importações:
1. Importa o framework utilizado para a criação e execução de testes.
2. Importa ferramentas para criar objetos mockados e simular comportamentos, permitindo testar código sem depender de implementações reais.
3. Importa a biblioteca para criar e gerenciar conexões de rede. Utilizada para simular os sockets no contexto do usuário.
4. Importa a classe que representa o usuário do sistema, com métodos para manipular sockets e realizar ações de comunicação.
5. Importa o arquivo de configurações que contém variáveis como endereços, -> parâmetros e valores utilizados nos testes.
"""


class TestUserAdmin:
    """
    Classe TestUserAdmin:

    Classe de testes para a implementação do usuário (User). Inclui a criação de instâncias de usuários, 
    a modificação de seus atributos e a verificação do comportamento dos métodos dessa classe.
    """

    @pytest.fixture
    def patch_socket(self):
        """
        Método patch_socket:

        Aplica o patch na biblioteca socket, substituindo a implementação real por um objeto Mock.
        Esse patch é utilizado para simular a criação e o uso de sockets na classe User.
        Retorna o objeto socket mockado, pronto para ser utilizado nos testes.

        -> Parâmetro:
        mock_socket (Mock): O Mock do socket que será utilizado no teste.
        """
        with patch("socket.socket") as mock_socket:
            yield mock_socket

    @pytest.fixture
    def mock_socket(self, patch_socket):
        """
        Método mock_socket:

        Cria um Mock para simular o comportamento de um socket. Esse mock é configurado para simular
        funções como connect, settimeout, send, recv e close.
        Retorna o objeto socket mockado configurado para os testes.

        -> Parâmetro:
        patch_socket (Mock): O Mock do socket aplicado no patch.
        """
        mock_socket = patch_socket
        mock_socket.connect.return_value = None
        mock_socket.settimeout.return_value = None
        mock_socket.send.return_value = None
        mock_socket.recv.return_value = None
        mock_socket.close.return_value = None
        return mock_socket

    @pytest.fixture
    def usuario(self, mock_socket):
        """
        Método usuario:

        Cria uma instância de User com o nome "Usuario" e um timeout de 300. Esse usuário será utilizado
        para testar os métodos e atributos da classe User.
        Retornoa a instância do usuário, pronta para os testes.

        -> Parâmetro:
        mock_socket (Mock): O Mock do socket utilizado para a simulação da conexão.
        """
        return User("Usuario", 300, ADDR)

    def test_constructor_usuario(self, usuario: User):
        """
        Método test_constructor_usuario:

        Testa o construtor da instância User, verificando se os atributos são corretamente inicializados
        e se o socket do usuário está configurado corretamente.

        -> Parâmetro:
        usuario (User): A instância de User representando um usuário.
        """
        assert usuario.nome == "Usuario"
        assert usuario.timeout == 300
        assert usuario.endereco == ADDR

        usuario.socket_user.connect.assert_called_with(ADDR)
        usuario.socket_user.settimeout.assert_called_once()
        usuario.socket_user.send.assert_called_with("Usuario".encode())

    def test_usuario_nome_setter(self, usuario: User):
        """
        Método test_usuario_nome_setter:

        Testa a alteração do nome de um usuário, verificando se a modificação é corretamente aplicada.

        -> Parâmetro:
        usuario (User): A instância de User representando um usuário.
        """
        usuario.nome = "Usuario2"
        assert usuario.nome == "Usuario2"
        assert usuario.timeout == 300
        assert usuario.endereco == ADDR

    def test_usuario_timeout_setter(self, usuario: User):
        """
        Método test_usuario_timeout_setter:

        Testa a alteração do timeout de um usuário, verificando se o valor é alterado corretamente.

        -> Parâmetro:
        usuario (User): A instância de User representando um usuário.
        """
        usuario.timeout = 100
        assert usuario.nome == "Usuario"
        assert usuario.timeout == 100
        assert usuario.endereco == ADDR

    def test_usuario_endereco_setter(self, usuario: User):
        """
        Método test_usuario_endereco_setter:

        Testa a alteração do endereço de um usuário, verificando se o novo endereço é corretamente atribuído.

        -> Parâmetro:
        usuario (User): A instância de User representando um usuário.
        """
        usuario.endereco = ("127.0.0.1", 1001)
        assert usuario.nome == "Usuario"
        assert usuario.timeout == 300
        assert usuario.endereco == ("127.0.0.1", 1001)

    def test_usuario_socket_user_setter(self, usuario: User, mock_socket):
        """
        Método test_usuario_socket_user_setter:

        Testa a alteração do socket_user de um usuário, verificando se o socket é atribuído corretamente.

        -> Parâmetros:
        usuario (User): A instância de User representando um usuário.
        mock_socket (Mock): O Mock do socket que será atribuído ao usuário.
        """
        usuario.socket_user = mock_socket
        assert usuario.nome == "Usuario"
        assert usuario.timeout == 300
        assert usuario.endereco == ADDR
        assert usuario.socket_user == mock_socket

    def test_usuario_iniciar_conexao(self, usuario: User):
        """
        Método test_usuario_iniciar_conexao:

        Testa o método iniciar_conexao do usuário, verificando se a conexão é iniciada corretamente.

        -> Parâmetro:
        usuario (User): A instância de User representando um usuário.
        """
        usuario.iniciar_conexao()
        usuario.socket_user.connect.assert_called_with(ADDR)
        usuario.socket_user.settimeout.asser_called_once()
        usuario.socket_user.send.assert_called_with("Usuario".encode())

    def test_usuario_escutar_mensagens(self, usuario: User):
        """
        Método test_usuario_escutar_mensagens:

        Testa o método escutar_mensagens do usuário, verificando se as mensagens são recebidas corretamente.

        -> Parâmetro:
        usuario (User): A instância de User representando um usuário.
        """
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
        """
        Método test_usuario_enviar_mensagem:

        Testa o método enviar_mensagem do usuário, verificando se a mensagem é enviada corretamente.

        -> Parâmetros:
        usuario (User): A instância de User representando um usuário.
        mensagem (str): A mensagem a ser enviada pelo usuário.
        """
        usuario.enviar_mensagem(mensagem)
        usuario.socket_user = usuario.socket_user
        usuario.socket_user.send.assert_called_with(mensagem.encode())

    def test_usuario_fechar_conexao(self, usuario: User):
        """
        Método test_usuario_fechar_conexao:

        Testa o método fechar_conexao do usuário, verificando se a conexão é encerrada corretamente.

        -> Parâmetro:
        usuario (User): A instância de User representando um usuário.
        """
        usuario.fechar_conexao()
        usuario.socket_user.close.assert_called_once()
