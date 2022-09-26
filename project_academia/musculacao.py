from treino import Treino


class Musculacao(Treino):
    def __init__(self, tipo, duracao, instrutor, cliente, qtd_aparelhos):
        super().__init__(tipo, duracao, instrutor, cliente)
        self._qtd_aparelhos = qtd_aparelhos

    def __str__(self):
        return super().__str__() + f'Quantidade de aparelhos: {self._qtd_aparelhos}\n'
