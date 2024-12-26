import pytest
from unittest.mock import Mock, patch
from postgres import PostgresDB

class TestPostgres:

    @pytest.fixture
    def mock_connect(self):
        """Fixture que cria um Mock para simular o método connect"""
        with patch("psycopg2.connect") as mock_connect:
            mock_connect.return_value = None
            yield mock_connect

    @pytest.fixture
    def mock_conn(self):
        """Fixture que cria um Mock para simular o método commit do objeto conn"""
        mock_conn = Mock()
        mock_conn.cursor.return_value = None
        mock_conn.commit.return_value = None
        return mock_conn
    
    @pytest.fixture
    def mock_cursor(self):
        """Fixture que cria um Mock para simular o objeto cursor"""
        mock_cursor = Mock()
        mock_cursor.execute.return_value = None
        mock_cursor.executemany.return_value = None
        mock_cursor.fetchall.return_value = [(None, None)]
        mock_cursor.close.return_value = None
        return mock_cursor

    @pytest.fixture
    def postgres(self, mock_connect: Mock):
        """Fixture que retorna uma instância do postgres"""
        return PostgresDB(dbname="mydatabase", user="user", password="password", host="localhost", port="5410")

    @pytest.fixture
    def mock_medic(self):
        """Fixture que retorna uma função para criar um Mock que simula classe Medicamento"""

        def create_mock_medic(nome: str, preco: str, quantidade_estoque: str, medicamento_id: int = None):
            mock_medic = Mock()
            mock_medic.medicamento_id = medicamento_id
            mock_medic.nome = nome
            mock_medic.preco = preco
            mock_medic.quantidade_estoque = quantidade_estoque
            return mock_medic
        
        return create_mock_medic


    def test_constructor(self, postgres: PostgresDB, mock_connect: Mock):
        """Testa a inicialização de uma instância Postgres"""
        assert postgres._dbname == "mydatabase"
        assert postgres._user == "user"
        assert postgres._password == "password"
        assert postgres._host == "localhost"
        assert postgres._port == "5410"
        assert postgres._conn == None
        assert postgres._cursor == None
        mock_connect.assert_called_once()


    def test_connect(self, postgres: PostgresDB, mock_connect: Mock, mock_conn: Mock):
        """Testa a conexão de uma instância Postgres"""
        mock_connect.return_value = mock_conn
        
        postgres.connect()
        mock_connect.assert_called()


    def test_create_table(self, postgres: PostgresDB, mock_conn: Mock, mock_cursor: Mock):
        """Testa a criação de uma tabela de uma instância Postgres"""
        postgres._cursor = mock_cursor
        postgres._conn = mock_conn
        postgres.create_table()
        
        mock_cursor.execute.assert_called_with("""CREATE TABLE IF NOT EXISTS medicamento (medicamento_id INT PRIMARY KEY AUTO_INCREMENT, nome VARCHAR(255) NOT NULL, preco DECIMAL(10, 2), quantidade_estoque INT)""")
        mock_conn.commit.assert_called_once()


    @pytest.mark.parametrize("nome, preco, quantidade_estoque", [
        ("Teste1", "10.50", "20"),
        ("Teste2", "12.00", "10"),
        ("Teste3", "2.75", "3"),
    ])
    def test_insert(self, postgres: PostgresDB, mock_conn: Mock, mock_cursor: Mock, mock_medic: Mock, nome: str, preco: str, quantidade_estoque: str):
        """Testa a inserção de medicamentos em uma instância Postgres"""
        medicamento = mock_medic(nome, preco, quantidade_estoque)
        postgres._cursor = mock_cursor
        postgres._conn = mock_conn
        postgres.insert(medicamento)

        mock_cursor.executemany.assert_called_with("""INSERT INTO medicamento (nome, preco, quantidade_estoque) VALUES (%s, %s, %s)""", (medicamento.nome, medicamento.preco, medicamento.quantidade_estoque))
        mock_conn.commit.assert_called_once()


    def test_select_all(self, postgres: PostgresDB, mock_cursor: Mock):
        """Testa a recuperação de medicamentos em uma instância Postgres"""
        postgres._cursor = mock_cursor
        rows = postgres.select_all()

        mock_cursor.execute.assert_called_with("SELECT * FROM medicamento")
        mock_cursor.fetchall.assert_called_once()
        assert rows == [(None, None)]


    @pytest.mark.parametrize("id", [
        ("1"),
        ("2"),
        ("3"),
    ])
    def test_select_all(self, postgres: PostgresDB, mock_cursor: Mock, mock_conn: Mock, id: str):
        """Testa a deleção de um medicamento em uma instância Postgres"""
        postgres._cursor = mock_cursor
        postgres._conn = mock_conn
        rows = postgres.delete_by_id(id)

        mock_cursor.executemany.assert_called_with("""DELETE FROM medicamento WHERE medicamento_id = %s;""", id)
        mock_conn.commit.assert_called_once()


    @pytest.mark.parametrize("nome, preco, quantidade_estoque, id", [
        ("Teste1", "10.50", "20", "1"),
        ("Teste2", "12.00", "10", "2"),
        ("Teste3", "2.75", "3", "3"),
    ])
    def test_update(self, postgres: PostgresDB, mock_conn: Mock, mock_cursor: Mock, mock_medic: Mock, nome: str, preco: str, quantidade_estoque: str, id: str):
        """Testa a atualização de medicamentos em uma instância Postgres"""
        medicamento = mock_medic(nome, preco, quantidade_estoque, id)
        postgres._cursor = mock_cursor
        postgres._conn = mock_conn
        postgres.update(medicamento)

        mock_cursor.executemany.assert_called_with("""UPDATE medicamento SET nome = %s, preco = %s, quantidade_estoque = %s WHERE medicamento_id = %s;""", (medicamento.nome, medicamento.preco, medicamento.quantidade_estoque, medicamento.medicamento_id))
        mock_conn.commit.assert_called_once()

    def test_disconnect(self, postgres: PostgresDB, mock_conn: Mock, mock_cursor: Mock):
        """Testa a desconexão de uma instância Postgres"""
        postgres._cursor = mock_cursor
        postgres._conn = mock_conn
        postgres.disconnect()
        mock_cursor.close.assert_called_once()
        mock_conn.close.assert_called_once()
