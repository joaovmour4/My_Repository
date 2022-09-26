import abc

class Treino(abc.ABC):
    @abc.abstractmethod
    def __init__(self, tipo, duracao, instrutor, cliente):
        self._tipo = tipo
        self._duracao = duracao
        self._instrutor = instrutor
        self._cliente = cliente


    @property
    def instrutor(self):
        return self._instrutor

    @property
    def cliente(self):
        return self._cliente
    
    def __str__(self):
        return f'Tipo: {self._tipo}\nDuração: {self._duracao} minutos\nInstrutor: {self._instrutor}\nCliente: {self._cliente}\n'
