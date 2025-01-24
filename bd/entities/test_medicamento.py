import pytest
from unittest.mock import Mock, patch
from .medicamento import Medicamento
"""
Importações:
1. Framework de testes para executar os testes unitários.
2. Biblioteca para criar mocks e substituir dependências.
3. Classe a ser testada.
"""


class TestMedicamento:
    """
    Classe TestMedicamento:

    Contém testes unitários para validar a inicialização e modificação dos atributos da classe Medicamento.
    """

    @pytest.fixture
    def medicamento(self):
        """
        Método medicamento:

        Cria e retorna uma instância da classe Medicamento para uso nos testes.
        Retorna uma instância de Medicamento inicializada com valores padrão.
        """
        return Medicamento("1", "Teste1", "10.50", "15")

    def test_constructor(self, medicamento: Medicamento):
        """
        Método test_constructor:

        Testa a inicialização de uma instância da classe Medicamento.
        Verifica se os atributos são corretamente atribuídos ao objeto.
        """
        assert medicamento.medicamento_id == "1"
        assert medicamento.nome == "Teste1"
        assert medicamento.preco == "10.50"
        assert medicamento.quantidade_estoque == "15"

    def test_medicamento_id_setter(self, medicamento: Medicamento):
        """
        Método test_medicamento_id_setter:

        Testa a alteração do id de uma instância Medicamento.
        """
        medicamento.medicamento_id = "2"
        assert medicamento.medicamento_id == "2"
        assert medicamento.nome == "Teste1"
        assert medicamento.preco == "10.50"
        assert medicamento.quantidade_estoque == "15"

    def test_nome_setter(self, medicamento: Medicamento):
        """
        Método test_nome_setter:

        Testa a alteração de nome de uma instância Medicamento.
        """
        medicamento.nome = "Teste2"
        assert medicamento.medicamento_id == "1"
        assert medicamento.nome == "Teste2"
        assert medicamento.preco == "10.50"
        assert medicamento.quantidade_estoque == "15"

    def test_preco_setter(self, medicamento: Medicamento):
        """
        Método test_preco_setter:

        Testa a alteração de preco de uma instância Medicamento.
        """
        medicamento.preco = "20.99"
        assert medicamento.medicamento_id == "1"
        assert medicamento.nome == "Teste1"
        assert medicamento.preco == "20.99"
        assert medicamento.quantidade_estoque == "15"

    def test_estoque_setter(self, medicamento: Medicamento):
        """
        Método test_estoque_setter:

        Testa a alteração de quantidade em estoque de uma instância Medicamento.
        """
        medicamento.quantidade_estoque = "7"
        assert medicamento.medicamento_id == "1"
        assert medicamento.nome == "Teste1"
        assert medicamento.preco == "10.50"
        assert medicamento.quantidade_estoque == "7"
