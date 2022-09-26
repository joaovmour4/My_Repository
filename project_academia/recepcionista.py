from funcionario import Funcionario
from pathlib import Path

class Recepcionista(Funcionario):
    def __init__(self, nome, data_admissao, turno, usuario, senha, funcao):
        super().__init__(nome, data_admissao, turno, usuario, senha, funcao)
        self._mult_salario = 1.5
        self.calcula_salario()
        self.escrita_recepcionista(usuario, senha)

    def __str__(self):
        return super().__str__()

    def calcula_salario(self):
        self._salario = super().calcula_salario() * self._mult_salario

    def escrita_recepcionista(self, usuario, senha):
        r = f'{self._nome};{self._data_admissao};{self._turno};{usuario};{senha};{self._funcao}\n'
        if Path('cadastros.txt').is_file():
            with open('cadastros.txt', encoding='utf-8') as arq:
                for linha in arq:
                    temp = linha.replace('\n', '').split(';')
                    if self._nome == temp[0] and self._data_admissao == temp[1] and usuario == temp[3]:
                        arq.close()
                        return False
        with open('cadastros.txt', 'a', encoding='utf-8') as arq:
            arq.write(r)
            arq.close() 
            