from treino import Treino
class Boxe(Treino):
    def __init__(self, tipo, duracao, instrutor, cliente, golpes, repeticao):
        super().__init__(tipo, duracao, instrutor, cliente)
        self._golpes = golpes
        self._repeticao = repeticao
    
    def __str__(self):
        return super().__str__() + f'Tipos de Golpes: {self._golpes}\nNúmero de repetições: {self._repeticao}\n'
    