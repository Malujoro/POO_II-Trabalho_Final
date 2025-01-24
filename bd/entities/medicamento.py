class Medicamento:
    """
    Classe Medicamento:

    Representa um medicamento, armazenando seu identificador, nome, preço e quantidade em estoque.
    """

    def __init__(self, medicamento_id, nome, preco, quantidade_estoque):
        """
        Construtor da classe Medicamento.

        -> Parâmetros:
        medicamento_id (int): Identificador único do medicamento.
        nome (str): Nome do medicamento.
        preco (float): Preço unitário do medicamento.
        quantidade_estoque (int): Quantidade disponível no estoque.
        """
        self._medicamento_id = medicamento_id
        self._nome = nome
        self._preco = preco
        self._quantidade_estoque = quantidade_estoque

    @property
    def medicamento_id(self) -> int:
        """
        Retorna o identificador único do medicamento.
        """
        return self._medicamento_id

    @medicamento_id.setter
    def medicamento_id(self, medicamento_id: int) -> None:
        """
        Define o identificador único do medicamento.
        """
        self._medicamento_id = medicamento_id

    @property
    def nome(self) -> str:
        """
        Retorna o nome do medicamento.
        """
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        """
        Define o nome do medicamento.
        """
        self._nome = nome

    @property
    def preco(self) -> float:
        """
        Retorna o preço do medicamento.
        """
        return self._preco

    @preco.setter
    def preco(self, preco: float) -> None:
        """
        Define o preço do medicamento.
        """
        self._preco = preco

    @property
    def quantidade_estoque(self) -> int:
        """
        Retorna a quantidade em estoque do medicamento.
        """
        return self._quantidade_estoque

    @quantidade_estoque.setter
    def quantidade_estoque(self, quantidade_estoque: int) -> None:
        """
        Define a quantidade em estoque do medicamento.
        """
        self._quantidade_estoque = quantidade_estoque
