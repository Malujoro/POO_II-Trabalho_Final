class Reserva:
    """
    Classe Reserva:

    Representa uma reserva de medicamentos feita por um cliente.
    """

    def __init__(self, reserva_id=None, cpf_cliente=None, nome_cliente=None, data_limite=None, medicamentos=[]):
        """
        Construção da classe:

        Inicializa uma instância de Reserva.

        -> Parâmetros:
        reserva_id (int, opcional): identificador único da reserva (padrão: None).
        cpf_cliente (str, opcional): CPF do cliente que fez a reserva (padrão: None).
        nome_cliente (str, opcional): Nome do cliente que fez a reserva (padrão: None).
        data_limite (datetime, opcional): Data limite da reserva (padrão: None).
        medicamentos (list, opcional): Lista de medicamentos associados à reserva (padrão: lista vazia).
        """

        self._reserva_id = reserva_id
        self._cpf_cliente = cpf_cliente
        self._nome_cliente = nome_cliente
        self._data_limite = data_limite
        self._medicamentos = medicamentos

    @property
    def reserva_id(self):
        """
        Retorna o identificador único da reserva.
        """
        return self._reserva_id

    @reserva_id.setter
    def reserva_id(self, value):
        """
        Define o identificador único da reserva.
        """
        self._reserva_id = value

    @property
    def cpf_cliente(self):
        """
        Retorna o CPF do cliente que realizou a reserva.
        """
        return self._cpf_cliente

    @cpf_cliente.setter
    def cpf_cliente(self, value):
        """
        Define o CPF do cliente que realizou a reserva.
        """
        self._cpf_cliente = value

    @property
    def nome_cliente(self):
        """
        Retorna o nome do cliente que realizou a reserva.
        """
        return self._nome_cliente

    @nome_cliente.setter
    def nome_cliente(self, value):
        """
        Define o nome do cliente que realizou a reserva.
        """
        self._nome_cliente = value

    @property
    def data_limite(self):
        """
        Retorna a data limite da reserva.
        """
        return self._data_limite

    @data_limite.setter
    def data_limite(self, value):
        """
        Define a data limite da reserva.
        """
        self._data_limite = value

    @property
    def medicamentos(self):
        """
        Retorna a lista de medicamentos associados à reserva.
        """
        return self._medicamentos

    @medicamentos.setter
    def medicamentos(self, value):
        """
        Define a lista de medicamentos associados à reserva.
        """
        self._medicamentos = value