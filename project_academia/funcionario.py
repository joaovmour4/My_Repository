import abc
from interface_login import Interface
from pathlib import Path

class Funcionario(abc.ABC, Interface):
    salario_minimo = 1212.0
    id = 1
    
    @abc.abstractmethod
    def __init__(self, nome, data_admissao, turno, usuario, senha, funcao):
        self._matricula = Funcionario.id
        self._nome = nome
        self._data_admissao = data_admissao
        self._funcao = funcao
        self._salario = 0
        self._turno = turno
        self._mult_salario = 0
        self.cadastrar_login(usuario, senha)
        Funcionario.id += 1

    @property
    def nome(self):
        return self._nome

    @property
    def funcao(self):
        return self._funcao

    
    def __str__(self):
        return f'Nome: {self._nome}\nMatrícula: {self._matricula}\nData de admissão: {self._data_admissao}\n'\
        f'Função: {self._funcao}\nSalário: R$ {self._salario: .2f}\nTurno: {self._turno}\n'

    def calcula_salario(self):
        return Funcionario.salario_minimo

    # Verifica se o arquivo de login's existe, se sim, verifica se o usuário já existe
    def cadastrar_login(self, usuario, senha):
        if Path('usuarios.txt').is_file():
            with open('usuarios.txt', encoding='utf-8') as arq:
                for linha in arq:
                    temp = linha.replace('\n', '').split(';')
                    if usuario == temp[0]:
                        return False
                arq.close()
        # Escreve no arquivo de login's
        with open('usuarios.txt', 'a', encoding='utf-8') as cad:
            cad.write(f'{usuario};{senha}\n')
            cad.close()          

    # Verifica se usuário e senha correspondem a algum registro 
    @staticmethod
    def login(usuario, senha):
        with open('usuarios.txt', encoding='utf-8') as cad:
            for linha in cad:
                temp = linha.replace('\n', '').split(';')
                if usuario in temp and senha in temp:
                    return True
            return False
