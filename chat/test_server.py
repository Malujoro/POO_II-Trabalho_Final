import pytest
from unittest.mock import MagicMock, patch
import socket
import threading
from server import ChatServer
from variaveis import *

"""
Importações:
1. Impora o framework utilizado para criação e execução de testes.
2. Importa ferramentas para criar objetos mockados e simular comportamentos, permitindo testar código sem depender de implementações reais.
3. Importa a biblioteca para criar e gerenciar conexões de rede. Utilizada para simular os sockets no servidor de chat.
4. Importa a biblioteca para manipulação de threads, usada para gerenciar as conexões simultâneas no servidor de chat.
5. Importa a classe que implementa o servidor de chat a ser testado.
6. Importa o arquivo de configurações que contém variáveis como endereços, nomes e parâmetros utilizados no servidor de chat.
"""


class TestServer:
    """
    Classe TestServer:

    Classe de testes para a implementação do servidor de chat (ChatServer).
    Contém métodos de testes para validar a funcionalidade do servidor, incluindo a inicialização,
    encaminhamento de mensagens e início do servidor.
    """

    @pytest.fixture
    def patch_socket(self, mock_socket):
        """
        Método patch_socket (Fixture):

        Aplica o patch na biblioteca socket, substituindo a implementação real por um objeto Mock.
        Esse patch é utilizado para simular a criação e o uso de sockets no servidor de chat sem
        depender de implementações de rede reais.
        Retorna o objeto socket mockado, pronto para ser utilizado nos testes.

        -> Parâmetro:
        mock_socket (MagicMock): O Mock do socket que será utilizado no servidor de chat.
        """
        with patch("socket.socket") as mock_socket:
            yield mock_socket

    @pytest.fixture
    def mock_socket(self, patch_socket):
        """
        Método mock_socket (Fixture):

        Cria um objeto Mock para simular o comportamento de um socket.
        O mock simula funções como bind, listen, accept e close com valores pré-definidos.
        Retorna o objeto socket mockado configurado para os testes.

        -> Parâmetro:
        patch_socket (MagicMock): O Mock do socket aplicado no patch.
        """
        mock_socket = patch_socket
        mock_socket.bind.return_value = None
        mock_socket.listen.return_value = None
        mock_socket.accept.return_value = None
        mock_socket.close.return_value = None
        return mock_socket

    @pytest.fixture
    def mock_conexao(self):
        """
        Método mock_conexao:

        Cria um Mock para simular uma conexão de socket. Esse mock é utilizado para simular a recepção
        de mensagens e a interação com o servidor de chat.
        Retornoa O objeto Mock que simula uma conexão com o servidor.
        """
        mock_conexao = MagicMock()
        mock_conexao.recv.return_value = None
        return mock_conexao

    @pytest.fixture
    def server(self, mock_socket):
        """
        Método server:

        Cria uma instância do servidor de chat (ChatServer) utilizando o socket mockado. Este servidor
        é utilizado para executar os testes relacionados à inicialização e funcionamento do servidor.
        Retorna uma instância do servidor de chat, pronta para os testes.

        -> Parâmetro:
        mock_socket (MagicMock): O Mock do socket utilizado na instância do servidor.
        """
        return ChatServer()

    def test_constructor_server(self, server):
        """
        Método test_constructor_server:

        Testa a inicialização do servidor de chat. Verifica se o servidor é configurado corretamente com os
        parâmetros de bind e listen, além de checar o estado inicial dos usuários e do socket do funcionário.

        -> Parâmetro:
        server (ChatServer): A instância do servidor de chat criada pela fixture.
        """
        server.server_socket.bind.assert_called_with(ADDR)
        server.server_socket.listen.assert_called_with(TOTAL_USUARIOS)
        assert server.usuarios == {}
        assert server.funcionario_socket == None

    @pytest.mark.parametrize("nome", [
        NOME_CLIENTE,
        NOME_ADMIN,
    ])
    def test_encaminhar_mensagem(self, server, mock_conexao, nome):
        """
        Método test_encaminhar_mensagem:

        Testa o método de encaminhamento de mensagens do servidor de chat. Verifica se as mensagens são
        corretamente enviadas para os outros usuários, exceto para o remetente.

        -> Parâmetros:
        server (ChatServer): A instância do servidor de chat.
        mock_conexao (MagicMock): A simulação de uma conexão de socket.
        nome (str): O nome do usuário que está enviando a mensagem.
        """
        server.funcionario_socket = MagicMock()

        server.usuarios = {
            NOME_ADMIN: server.funcionario_socket,
            NOME_CLIENTE: MagicMock(),
            "Usuario2": MagicMock()
        }

        mock_conexao.recv.side_effect = [
            "Teste".encode(),  # Mensagem simulada
            Exception,  # Gera uma exceção
        ]

        server.encaminhar_mensagem(mock_conexao, NOME_ADMIN)

        # Verifica se a mensagem foi encaminhada para os usuários, exceto para o remetente.
        for name, mock in server.usuarios.items():
            if name != nome:
                mock.send.assert_called_with(f"{NOME_ADMIN}: Teste".encode())

    def test_iniciar_servidor(self, server, mock_conexao):
        """
        Método test_iniciar_servidor:

        Testa a inicialização do servidor e o registro de clientes. Verifica se o servidor está aceitando
        conexões corretamente, registrando clientes e tratando exceções, como KeyboardInterrupt.

        -> Parâmetros:
        server (ChatServer): A instância do servidor de chat.
        mock_conexao (MagicMock): A simulação de uma conexão de socket.
        """
        server.funcionario_socket = MagicMock()

        mock_conexao.recv.side_effect = [
            NOME_CLIENTE.encode(),  # Nome do cliente simulado
        ]

        server.server_socket.accept.side_effect = [
            (mock_conexao, None),  # Simula aceitação de uma conexão
            KeyboardInterrupt,  # Simula uma interrupção no servidor
        ]

        server.iniciar_servidor()

        # Verifica se o socket do servidor foi fechado uma vez.
        server.server_socket.close.has_called_once()

        # Verifica se o cliente foi adicionado ao dicionário de usuários.
        assert NOME_CLIENTE in server.usuarios
