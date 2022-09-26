from treino import Treino
class Pilates(Treino):
    def __init__(self, tipo, duracao, instrutor, cliente, exercicios, repeticoes):
        super().__init__(tipo, duracao, instrutor, cliente)
        self._exercicios = exercicios
        self._repeticoes = repeticoes
    
    def __str__(self):
        return super().__str__() + f'Tipos de Exercícios: {self._exercicios}\nRepetições por Exercício: {self._repeticoes}\n'