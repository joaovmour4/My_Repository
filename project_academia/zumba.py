from treino import Treino
class Zumba(Treino):
    def __init__(self, tipo, duracao, instrutor, cliente, dancas, ritmos):
        super().__init__(tipo, duracao, instrutor, cliente)
        self._dancas = dancas
        self._ritmos = ritmos
    
    def __str__(self):
        return super().__str__() + f'Estilo de Zumba: {self._dancas}\nRitmos: {self._ritmos}\n'