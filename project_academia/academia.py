from administrador import Administrador
from auxiliar_de_limpeza import Auxiliar_de_limpeza
from instrutor import Instrutor
from nutricionista import Nutricionista
from recepcionista import Recepcionista
from boxe import Boxe
from pilates import Pilates
from zumba import Zumba
from musculacao import Musculacao
from pathlib import Path


class Academia:
    def __init__(self, nome, funcionarios, treinos):
        self.__nome = nome
        self.__funcionarios = funcionarios
        self.__treinos = treinos

    def __str__(self):
        r = f'{self.__nome}\n\n'
        for elemento in self.__funcionarios:
            r += f'{elemento}' + '\n'
        return r


    @property
    def funcionarios(self):
        return self.__funcionarios

    def cadastrar_funcionario(self, nome, data_admissao, turno, usuario, senha, funcao):
        if funcao == 'Administrador':
            funcionario = Administrador(nome, data_admissao, turno, usuario, senha, funcao)
        elif funcao == 'Nutricionista':
            funcionario = Nutricionista(nome, data_admissao, turno, usuario, senha, funcao)
        elif funcao == 'Recepcionista':
            funcionario = Recepcionista(nome, data_admissao, turno, usuario, senha, funcao)
        elif funcao == 'Auxiliar de limpeza':
            funcionario = Auxiliar_de_limpeza(nome, data_admissao, turno, usuario, senha, funcao)
        self.__funcionarios.append(funcionario)

    
    def cadastrar_instrutor(self, nome, data_admissao, turno, usuario, senha, area_de_treino, funcao):
        funcionario = Instrutor(nome, data_admissao, turno, usuario, senha, area_de_treino, funcao)
        self.__funcionarios.append(funcionario)
        
    def cadastrar_treino(self, tipo, duracao, instrutor, cliente, qtd_aparelhos=None, dancas=None, ritmos=None,
                                                            exercicios=None, repeticoes=None, golpes=None):
        treinos = open('treinos.txt', 'a', encoding='utf-8')
        if tipo == 'Boxe':
            treinos.write(f'{tipo};{duracao};{instrutor.nome};{cliente};{golpes};{repeticoes}\n')
            treino = Boxe(tipo, duracao, instrutor, cliente, golpes, repeticoes)
        elif tipo == 'Pilates':
            treinos.write(f'{tipo};{duracao};{instrutor.nome};{cliente};{exercicios};{repeticoes}\n')
            treino = Pilates(tipo, duracao, instrutor, cliente, exercicios, repeticoes)
        elif tipo == 'Zumba':
            treinos.write(f'{tipo};{duracao};{instrutor.nome};{cliente};{dancas};{ritmos}\n')
            treino = Zumba(tipo, duracao, instrutor, cliente, dancas, ritmos)
        elif tipo == 'Musculação':
            treinos.write(f'{tipo};{duracao};{instrutor.nome};{cliente};{qtd_aparelhos}\n')
            treino = Musculacao(tipo, duracao, instrutor, cliente, qtd_aparelhos)
        treinos.close()
        self.__treinos.append(treino)

    def buscar_funcionario(self, funcao, nome):
        for funcionario in self.__funcionarios:
            if funcionario.funcao == funcao.capitalize() and funcionario.nome == nome.capitalize():
                return funcionario
        
    def buscar_treino(self, cliente, instrutor):
        for treino in self.__treinos:
            if treino.cliente.capitalize() == cliente.capitalize() and treino.instrutor.capitalize() == instrutor.capitalize():
                return treino
    
    # Busca todos os treinos atribuídos a um determinado instrutor
    def busca_por_instrutor(self, instrutor):
        r = ''
        for treino in self.__treinos:
            if treino.instrutor.capitalize() == instrutor.capitalize():
                r += f'{treino}\n\n'
        return r

    # Lê os registros de funcionários guardados em cadastros.txt para instanciar os objetos na inicialização do programa
    @staticmethod
    def leitura_funcionarios(lista):
        if Path('cadastros.txt').is_file():    
            with open('cadastros.txt', encoding='utf-8') as arq:
                for linha in arq:
                    linha = linha.replace('\n', '').split(';')
                    if linha[len(linha)-1].lower() == 'instrutor':
                        funcioario = Instrutor(linha[0], linha[1], linha[2], 
                                                linha[3], linha[4], linha[5], linha[6])
                    elif linha[len(linha)-1].lower() == 'recepcionista':
                        funcioario = Recepcionista(linha[0], linha[1], linha[2], 
                                                    linha[3], linha[4], linha[5])
                    elif linha[len(linha)-1].lower() == 'auxiliar de limpeza':
                        funcioario = Auxiliar_de_limpeza(linha[0], linha[1], linha[2], 
                                                            linha[3], linha[4], linha[5])
                    lista.append(funcioario)
                arq.close()

    # Lê os registros de treinos guardados em treinos.txt para instanciar os objetos na inicialização do programa
    @staticmethod
    def leitura_treinos(lista):
        if Path('treinos.txt').is_file():    
            with open('treinos.txt', encoding='utf-8') as arq:
                for linha in arq:
                    linha = linha.replace('\n', '').split(';')
                    if linha[0].lower() == 'boxe':
                        treino = Boxe(linha[0], linha[1], linha[2], 
                                                linha[3], linha[4], linha[5])
                    elif linha[0].lower() == 'pilates':
                        treino = Pilates(linha[0], linha[1], linha[2], 
                                                    linha[3], linha[4], linha[5])
                    elif linha[0].lower() == 'zumba':
                        treino = Zumba(linha[0], linha[1], linha[2], 
                                                            linha[3], linha[4], linha[5])
                    elif linha[0].lower() == 'musculação':
                        treino = Musculacao(linha[0], linha[1], linha[2], 
                                                            linha[3], linha[4])
                    lista.append(treino)
                arq.close()
    