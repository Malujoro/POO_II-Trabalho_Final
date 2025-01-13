import pytest
from unittest.mock import Mock, patch
from medicamento import Medicamento

class TestMedicamento:

    @pytest.fixture
    def medicamento(self):
        """Fixture que retorna uma instância do medicamento"""
        return Medicamento("1", "Teste1", "10.50", "15")


    def test_constructor(self, medicamento: Medicamento):
        """Testa a inicialização de uma instância Medicamento"""
        assert medicamento.medicamento_id == "1"
        assert medicamento.nome == "Teste1"
        assert medicamento.preco == "10.50"
        assert medicamento.quantidade_estoque == "15"


    def test_medicamento_id_setter(self, medicamento: Medicamento):
        """Testa a alteração do id de uma instância Medicamento"""
        medicamento.medicamento_id = "2"
        assert medicamento.medicamento_id == "2"
        assert medicamento.nome == "Teste1"
        assert medicamento.preco == "10.50"
        assert medicamento.quantidade_estoque == "15"

    
    def test_nome_setter(self, medicamento: Medicamento):
        """Testa a alteração de nome de uma instância Medicamento"""
        medicamento.nome = "Teste2"
        assert medicamento.medicamento_id == "1"
        assert medicamento.nome == "Teste2"
        assert medicamento.preco == "10.50"
        assert medicamento.quantidade_estoque == "15"

    
    def test_preco_setter(self, medicamento: Medicamento):
        """Testa a alteração de preco de uma instância Medicamento"""
        medicamento.preco = "20.99"
        assert medicamento.medicamento_id == "1"
        assert medicamento.nome == "Teste1"
        assert medicamento.preco == "20.99"
        assert medicamento.quantidade_estoque == "15"


    def test_estoque_setter(self, medicamento: Medicamento):
        """Testa a alteração de quantidade em estoque de uma instância Medicamento"""
        medicamento.quantidade_estoque = "7"
        assert medicamento.medicamento_id == "1"
        assert medicamento.nome == "Teste1"
        assert medicamento.preco == "10.50"
        assert medicamento.quantidade_estoque == "7"