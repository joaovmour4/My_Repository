from funcionario import Funcionario
from pathlib import Path

# Sempre que um objeto é instanciado, é feita a escrita no arquivo, se já não existir lá
class Instrutor(Funcionario):
    def __init__(self, nome, data_admissao, turno, usuario, senha, area_de_treino, funcao):
        super().__init__(nome, data_admissao, turno, usuario, senha, funcao)
        self._area_de_treino = area_de_treino
        self._mult_salario = 2
        self.calcula_salario()
        self.escrita_instrutor(usuario, senha)


    @property
    def nome(self):
        return self._nome

    def __str__(self):
        return super().__str__() + f'Área de treino: {self._area_de_treino}\n'

    def calcula_salario(self):
        self._salario = super().calcula_salario() * self._mult_salario

    # Realiza a escrita do registro do funcionario no arquivo de registros
    def escrita_instrutor(self, usuario, senha):
        r = f'{self._nome};{self._data_admissao};{self._turno};{usuario};{senha};{self._area_de_treino};{self._funcao}\n'
        if Path('cadastros.txt').is_file():
            with open('cadastros.txt', encoding='utf-8') as arq:
                for linha in arq:
                    temp = linha.replace('\n', '').split(';')
                    if self._nome == temp[0] and self._data_admissao == temp[1]:
                        arq.close()
                        return False
        with open('cadastros.txt', 'a', encoding='utf-8') as arq:
            arq.write(r)
            arq.close()   
            