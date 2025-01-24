import pytest
from unittest.mock import Mock, patch
import socket
from .user_class import User
from .variaveis import *

"""
Importações:
1. Importa o framework utilizado para a criação e execução de testes.
2. Importa ferramentas para criar objetos mockados e simular comportamentos, permitindo testar código sem depender de implementações reais.
3. Importa a biblioteca para criar e gerenciar conexões de rede. Utilizada para simular os sockets no contexto do usuário admin.
4. Importa a classe que representa o usuário do sistema, incluindo admins, e contém métodos de interação com o servidor.
5. Importa o arquivo de configurações que contém variáveis como endereços, parâmetros e valores utilizados no contexto dos testes.
"""


class TestUserAdmin:
    """
    Classe TestUserAdmin:

    Classe de testes para a implementação do usuário admin (User), incluindo a criação de instâncias de admins,
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
        Método mock_socket (Fixture):

        Cria um Mock para simular o comportamento de um socket. Esse mock é configurado para simular
        funções como connect, settimeout, send, recv e close.
        Retorna o objeto socket mockado configurado para os testes.

        -> Parâmetros:
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
    def admin(self, mock_socket):
        """
        Método admin):

        Cria uma instância de User com o nome "Funcionario", representando um admin. Esse admin
        será utilizado em diversos testes de métodos e atributos da classe User.
        Retorna a instância do admin, pronta para os testes.

        -> Parâmetro:
        mock_socket (Mock): O Mock do socket utilizado para a simulação da conexão.
        """
        return User("Funcionario")

    def test_constructor_admin(self, admin: User):
        """
        Método test_constructor_admin:

        Testa o construtor da instância User, verificando se os atributos são corretamente inicializados
        e se o socket do admin está configurado corretamente.

        -> Parâmetros:
        admin (User): A instância de User representando um admin.
        """
        assert admin.nome == "Funcionario"
        assert admin.timeout == 0
        assert admin.endereco == ADDR

        admin.socket_user.connect.assert_called_with(ADDR)
        admin.socket_user.settimeout.assert_not_called()
        admin.socket_user.send.assert_called_with("Funcionario".encode())

    def test_admin_nome_setter(self, admin: User):
        """
        test_admin_nome_setter:

        Testa a alteração do nome de um admin, verificando se a modificação é corretamente aplicada.

        -> Parâmetro:
        admin (User): A instância de User representando um admin.
        """
        admin.nome = "Funcionario2"
        assert admin.nome == "Funcionario2"
        assert admin.timeout == 0
        assert admin.endereco == ADDR

    def test_admin_timeout_setter(self, admin: User):
        """
        Método test_admin_timeout_setter:

        Testa a alteração do timeout de um admin, verificando se o valor é alterado corretamente.

        _> Parâmetro:
        admin (User): A instância de User representando um admin.
        """
        admin.timeout = 100
        assert admin.nome == "Funcionario"
        assert admin.timeout == 100
        assert admin.endereco == ADDR

    def test_admin_endereco_setter(self, admin: User):
        """
        Método test_admin_endereco_setter:

        Testa a alteração do endereço de um admin, verificando se o novo endereço é corretamente atribuído.

        -> Parâmetro:
        admin (User): A instância de User representando um admin.
        """
        admin.endereco = ("127.0.0.1", 1001)
        assert admin.nome == "Funcionario"
        assert admin.timeout == 0
        assert admin.endereco == ("127.0.0.1", 1001)

    def test_admin_socket_user_setter(self, admin: User, mock_socket):
        """
        Método test_admin_socket_user_setter:

        Testa a alteração do socket_user de um admin, verificando se o socket é atribuído corretamente.

        -> Parâmetros:
        admin (User): A instância de User representando um admin.
        mock_socket (Mock): O Mock do socket que será atribuído ao admin.
        """
        admin.socket_user = mock_socket
        assert admin.nome == "Funcionario"
        assert admin.timeout == 0
        assert admin.endereco == ADDR
        assert admin.socket_user == mock_socket

    def test_admin_iniciar_conexao(self, admin: User):
        """
        Método test_admin_iniciar_conexao:

        Testa o método iniciar_conexao do admin, verificando se a conexão é iniciada corretamente.

        -> Parâmetro:
        admin (User): A instância de User representando um admin.
        """
        admin.iniciar_conexao()
        admin.socket_user.connect.assert_called_with(ADDR)
        admin.socket_user.settimeout.assert_not_called()
        admin.socket_user.send.assert_called_with("Funcionario".encode())

    def test_admin_escutar_mensagens(self, admin: User):
        """
        Método test_admin_escutar_mensagens:

        Testa o método escutar_mensagens do admin, verificando se as mensagens são recebidas corretamente.

        -> Parâmetro:
        admin (User): A instância de User representando um admin.
        """
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
        """
        Método test_admin_enviar_mensagem:

        Testa o método enviar_mensagem do admin, verificando se a mensagem é enviada corretamente.

        Parâmetros:
        admin (User): A instância de User representando um admin.
        mensagem (str): A mensagem a ser enviada pelo admin.
        """
        admin.enviar_mensagem(mensagem)
        admin.socket_user = admin.socket_user
        admin.socket_user.send.assert_called_with(mensagem.encode())

    def test_admin_fechar_conexao(self, admin: User):
        """
        Método test_admin_fechar_conexao:

        Testa o método fechar_conexao do admin, verificando se a conexão é encerrada corretamente.

        -> Parâmetro:
        admin (User): A instância de User representando um admin.
        """
        admin.fechar_conexao()
        admin.socket_user.close.assert_called_once()
