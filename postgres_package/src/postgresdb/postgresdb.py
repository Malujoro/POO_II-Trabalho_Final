import psycopg2
"""
Importação:

1. Importa a biblioteca do PostgreSQL.
"""


class PostgresDB:
    """
    Classe PostgresDB:

    Gerenciar as operações do banco de dados Postgres.
    Permite conectar, inserir mensagem e desconectar.
    """

    def __init__(self, dbname: str = 'mydatabase', user: str = 'user', password: str = 'password', host: str = 'localhost', port: str = '5410') -> None:
        """
        Construção da classe:

        Inicializa a instância do PostgresDB e estabelece uma conexão com o banco.

        -> Atributos (privados):

        Inicializa a classe com os parâmetros de conexão do banco de dados, com dados pré definidos caso não seja informado:
        dbname (str): nome do banco (padrão: 'mydatabase');
        user (str): nome do usuário (padrão: 'user');
        password (str): senha do usuário (padrão: 'password');
        host (str): endereço do banco (padrão: 'localhost);
        port (str): porta do banco (padrão: '5410);

        conn: atributo que contém a conexão do banco (inicializado com None);
        cursor: atributo que contém o cursor do banco (inicializado com None);
        connect: a conexão com o banco de dados é estabelecida.
        """
        self._dbname = dbname
        self._user = user
        self._password = password
        self._host = host
        self._port = port
        self._conn = None
        self._cursor = None
        self.connect()

    def connect(self) -> None:
        """
        Método connect:

        Verifica de a variável conn é None.
        Se sim, estabelece conexão com o banco de dados usando 'psycopg2.connect'.
        Inicializa o cursor para executar os comandos SQL.
        Chama o método 'create_table' para criar a tabela caso não exista.
        """
        if (self._conn == None):
            self._conn = psycopg2.connect(
                dbname=self._dbname,
                user=self._user,
                password=self._password,
                host=self._host,
                port=self._port
            )

            if(self._conn != None):
                self._cursor = self._conn.cursor()

    def create_table(self, args: list[str]) -> None:
        """
        Método create_table:

        Cria a tabela com as colunas: id, role, message e date.
        O comando 'self._conn.commit()' é usado para salvar as alterações.
        """
        if(self._cursor != None):
            for string in args:
                self._cursor.execute(string)

            self._conn.commit()

    def select_all(self, table: str):
        """
        Método select_all:
        
        O comando executado 'SELECT * FROM medicamento' seleciona todas as linhas da tabela medicamento.
        Esta função retorna todas as linhas resultantes como uma lista de tuplas.
        """
        self._cursor.execute(f"SELECT * FROM {table}")
        rows = self._cursor.fetchall()
        return rows  

    def disconnect(self) -> None:
        """
        Método disconnect:

        Fecha o cursor e a conexão (conn) com o banco de dados usando o comando close.
        """
        self._cursor.close()
        self._conn.close()