###### Integrantes do grupo #######
# João Vitor Moura | Mayara Alves Ferreira | Ramon Castro Barbosa | Victor Manoel S. F. Meira
################

# Login: admin | Senha: admin

from academia import Academia
from funcionario import Funcionario
import sys
from tkinter import *
from tkinter.ttk import Combobox
from tkinter.scrolledtext import ScrolledText

funcionarios = []
treinos = []
Academia.leitura_funcionarios(funcionarios)
Academia.leitura_treinos(treinos)
acad = Academia('Academia Bolinha', funcionarios, treinos)


global frame, frame_info, frame_cad_treino, tela


def login():
    frame.grid_forget()
    frame_login = Frame(tela)
    frame_login.grid()
    Label(frame_login, text='Usuário').grid(padx=270, pady=(100, 0))
    Label(frame_login, text='Senha').grid(row=2)
    entry_usuario = Entry(frame_login, width=20)
    entry_senha = Entry(frame_login, width=20)
    entry_usuario.grid(row=1)
    entry_senha.grid(row=3)
    msg = Label(frame_login, text='Usuário ou senha incorretos!')
    ver_button = Button(frame_login, text='Próximo', command=lambda:[menu_inicial(frame_login) if Funcionario.login(entry_usuario.get(), entry_senha.get()) else msg.grid(row=5, pady=(2,0))]).grid(row=4, pady=(2,0))
    frame_login.mainloop()


def cadastrar_treino():
    frame.grid_forget()
    frame_cad_treino = Frame(tela)
    frame_cad_treino.grid()
    
    button_home = Button(frame_cad_treino, text='Home', height=1, width=7, command=lambda:[menu_inicial(frame_cad_treino)]).grid(padx=5, pady=5)
    
    label = Label(frame_cad_treino, text='Cadastro de treino').grid(row=0, column=1, padx=100, pady=5)
    label_tipo = Label(frame_cad_treino, text='Tipo de treino:').grid(row=1, padx=(2,5), pady=5)
    
    cmb_tipo = Combobox(frame_cad_treino, width=37, values=['Boxe',
                                                               'Pilates',
                                                               'Zumba',
                                                               'Musculação'])
    

    cmb_tipo.grid(row=1, column=1)
    

    bttn_prox = Button(frame_cad_treino, text='Próximo', command=lambda:[cadastrar_boxe() if cmb_tipo.get() == 'Boxe'
                                                                        else (cadastrar_pilates if cmb_tipo.get() == 'Pilates'
                                                                        else (cadastrar_zumba() if cmb_tipo.get() == 'Zumba'
                                                                        else cadastrar_musculacao())), frame_cad_treino.destroy()])
    bttn_prox.grid(column=1)
    

def cadastrar_boxe():
    frame_cad_treino = Frame(tela)
    frame_cad_treino.grid()
    button_home = Button(frame_cad_treino, text='Home', height=1, width=7, command=lambda:[menu_inicial(frame_cad_treino)]).grid(padx=5, pady=5)

    Label(frame_cad_treino, text='Duração:', height=1, width=10, anchor=W).grid(row=1, padx=(2,5), pady=5)
    Label(frame_cad_treino, text='Instrutor:', height=1, width=10, anchor=W).grid(row=2, padx=(2,5), pady=5)
    Label(frame_cad_treino, text='Cliente:', height=1, width=10, anchor=W).grid(row=3, padx=(2,5), pady=5)
    Label(frame_cad_treino, text='Golpes:', height=1, width=10, anchor=W).grid(row=4, padx=(2,5), pady=5)
    Label(frame_cad_treino, text='Repetições:', height=1, width=10, anchor=W).grid(row=5, padx=(2,5), pady=5)

    entry_duracao = Entry(frame_cad_treino, width=40)
    cmb_instrutor = Combobox(frame_cad_treino, width=37, values=[x.nome for x in funcionarios if x.funcao == 'Instrutor'])
    entry_cliente = Entry(frame_cad_treino, width=40)
    entry_golpes = Entry(frame_cad_treino, width=40)
    entry_repeticoes = Entry(frame_cad_treino, width=40)

    entry_duracao.grid(row=1, column=1)
    cmb_instrutor.grid(row=2, column=1)
    entry_cliente.grid(row=3, column=1)
    entry_golpes.grid(row=4, column=1)
    entry_repeticoes.grid(row=5, column=1)

    bttn_prox = Button(frame_cad_treino, text='Próximo', command=lambda:[acad.cadastrar_treino('Boxe',
                                                                                                entry_duracao.get(),
                                                                                                acad.buscar_funcionario('Instrutor', cmb_instrutor.get()),
                                                                                                entry_cliente.get(),
                                                                                                golpes=entry_golpes.get(),
                                                                                                repeticoes=entry_repeticoes.get()), 
                                                                                                menu_inicial(frame_cad_treino)])
    bttn_prox.grid(column=1)


def cadastrar_pilates():
    frame_cad_treino = Frame(tela)
    frame_cad_treino.grid()
    button_home = Button(frame_cad_treino, text='Home', height=1, width=7, command=lambda:[menu_inicial(frame_cad_treino)]).grid(padx=5, pady=5)

    Label(frame_cad_treino, text='Duração:', height=1, width=10, anchor=W).grid(row=1, padx=(2,5), pady=5)
    Label(frame_cad_treino, text='Instrutor:', height=1, width=10, anchor=W).grid(row=2, padx=(2,5), pady=5)
    Label(frame_cad_treino, text='Cliente:', height=1, width=10, anchor=W).grid(row=3, padx=(2,5), pady=5)
    Label(frame_cad_treino, text='Exercícios:', height=1, width=10, anchor=W).grid(row=4, padx=(2,5), pady=5)
    Label(frame_cad_treino, text='Repetições:', height=1, width=10, anchor=W).grid(row=5, padx=(2,5), pady=5)

    entry_duracao = Entry(frame_cad_treino, width=40)
    cmb_instrutor = Combobox(frame_cad_treino, width=37, values=[x.nome for x in funcionarios if x.funcao == 'Instrutor'])
    entry_cliente = Entry(frame_cad_treino, width=40)
    entry_exercicios = Entry(frame_cad_treino, width=40)
    entry_repeticoes = Entry(frame_cad_treino, width=40)

    entry_duracao.grid(row=1, column=1)
    cmb_instrutor.grid(row=2, column=1)
    entry_cliente.grid(row=3, column=1)
    entry_exercicios.grid(row=4, column=1)
    entry_repeticoes.grid(row=5, column=1)

    bttn_prox = Button(frame_cad_treino, text='Próximo', command=lambda:[acad.cadastrar_treino('Pilates',
                                                                                                entry_duracao.get(),
                                                                                                acad.buscar_funcionario('Instrutor', cmb_instrutor.get()),
                                                                                                entry_cliente.get(),
                                                                                                exercicios=entry_exercicios.get(),
                                                                                                repeticoes=entry_repeticoes.get()), 
                                                                                                menu_inicial(frame_cad_treino)])
    bttn_prox.grid(column=1)


def cadastrar_zumba():
    frame_cad_treino = Frame(tela)
    frame_cad_treino.grid()
    button_home = Button(frame_cad_treino, text='Home', height=1, width=7, command=lambda:[menu_inicial(frame_cad_treino)]).grid(padx=5, pady=5)

    Label(frame_cad_treino, text='Duração:', height=1, width=10, anchor=W).grid(row=1, padx=(2,5), pady=5)
    Label(frame_cad_treino, text='Instrutor:', height=1, width=10, anchor=W).grid(row=2, padx=(2,5), pady=5)
    Label(frame_cad_treino, text='Cliente:', height=1, width=10, anchor=W).grid(row=3, padx=(2,5), pady=5)
    Label(frame_cad_treino, text='Danças:', height=1, width=10, anchor=W).grid(row=4, padx=(2,5), pady=5)
    Label(frame_cad_treino, text='Ritmos:', height=1, width=10, anchor=W).grid(row=5, padx=(2,5), pady=5)

    entry_duracao = Entry(frame_cad_treino, width=40)
    cmb_instrutor = Combobox(frame_cad_treino, width=37, values=[x.nome for x in funcionarios if x.funcao == 'Instrutor'])
    entry_cliente = Entry(frame_cad_treino, width=40)
    entry_dancas = Entry(frame_cad_treino, width=40)
    entry_ritmos = Entry(frame_cad_treino, width=40)

    entry_duracao.grid(row=1, column=1)
    cmb_instrutor.grid(row=2, column=1)
    entry_cliente.grid(row=3, column=1)
    entry_dancas.grid(row=4, column=1)
    entry_ritmos.grid(row=5, column=1)

    bttn_prox = Button(frame_cad_treino, text='Próximo', command=lambda:[acad.cadastrar_treino('Zumba',
                                                                                                entry_duracao.get(),
                                                                                                acad.buscar_funcionario('Instrutor', cmb_instrutor.get()),
                                                                                                entry_cliente.get(),
                                                                                                dancas=entry_dancas.get(),
                                                                                                ritmos=entry_ritmos.get()),
                                                                                                menu_inicial(frame_cad_treino)])
    bttn_prox.grid(column=1)


def cadastrar_musculacao():
    frame_cad_treino = Frame(tela)
    frame_cad_treino.grid()
    button_home = Button(frame_cad_treino, text='Home', height=1, width=7, command=lambda:[menu_inicial(frame_cad_treino)]).grid(padx=5, pady=5)

    Label(frame_cad_treino, text='Duração:', height=1, width=20, anchor=W).grid(row=1, padx=(2,5), pady=5)
    Label(frame_cad_treino, text='Instrutor:', height=1, width=20, anchor=W).grid(row=2, padx=(2,5), pady=5)
    Label(frame_cad_treino, text='Cliente:', height=1, width=20, anchor=W).grid(row=3, padx=(2,5), pady=5)
    Label(frame_cad_treino, text='Quantidade de aparelhos:', height=1, width=20, anchor=W).grid(row=4, padx=(2,5), pady=5)

    entry_duracao = Entry(frame_cad_treino, width=40)
    cmb_instrutor = Combobox(frame_cad_treino, width=37, values=[x.nome for x in funcionarios if x.funcao == 'Instrutor'])
    entry_cliente = Entry(frame_cad_treino, width=40)
    entry_qtd_aparelhos = Entry(frame_cad_treino, width=40)

    entry_duracao.grid(row=1, column=1)
    cmb_instrutor.grid(row=2, column=1)
    entry_cliente.grid(row=3, column=1)
    entry_qtd_aparelhos.grid(row=4, column=1)

    bttn_prox = Button(frame_cad_treino, text='Próximo', command=lambda:[acad.cadastrar_treino('Musculação',
                                                                                                entry_duracao.get(),
                                                                                                acad.buscar_funcionario('Instrutor', cmb_instrutor.get()),
                                                                                                entry_cliente.get(),
                                                                                                qtd_aparelhos=entry_qtd_aparelhos.get()),
                                                                                                menu_inicial(frame_cad_treino)])
                                                                                            
    bttn_prox.grid(column=1)

    
def tela_cadastro_funcionarios():

    frame.grid_forget()
    frame_cad_funcionario = Frame(tela)
    frame_cad_funcionario.grid()
    button_home = Button(frame_cad_funcionario, text='Home', command=lambda:[menu_inicial(frame_cad_funcionario)]).grid(padx=5, pady=5)
    
    label = Label(frame_cad_funcionario, text='Cadastro de funcionário').grid(row=0, column=1, padx=100, pady=5)
    Label(frame_cad_funcionario, text='Função:', width=20, anchor=W).grid(row=1, column=0)

    cmb_funcao = Combobox(frame_cad_funcionario, width=37, values=['Administrador',
                                                                    'Nutricionista',
                                                                    'Recepcionista',
                                                                    'Instrutor',
                                                                    'Auxiliar de limpeza'])
    
    Button(frame_cad_funcionario, text='Próximo', command=lambda:[cadastrar_instrutor() if cmb_funcao.get() == 'Instrutor'
                                                                                        else cadastrar_funcionario(), 
                                                                                        frame_cad_funcionario.destroy()]).grid(column=1)
    
    cmb_funcao.grid(row=1, column=1)


def cadastrar_instrutor():
    frame_cad_funcionario = Frame(tela)
    frame_cad_funcionario.grid()
    button_home = Button(frame_cad_funcionario, text='Home', command=lambda:[menu_inicial(frame_cad_funcionario)]).grid(padx=5, pady=5)
    
    Label(frame_cad_funcionario, text='Cadastro de funcionário').grid(row=0, column=1, padx=100, pady=5)
    Label(frame_cad_funcionario, text='Nome:', width=20, anchor=W).grid(row=1, column=0)
    Label(frame_cad_funcionario, text='Data de admissão:', width=20, anchor=W).grid(row=2, column=0)
    Label(frame_cad_funcionario, text='Turno:', width=20, anchor=W).grid(row=3, column=0)
    Label(frame_cad_funcionario, text='Área de treino:', width=20, anchor=W).grid(row=4, column=0)
    Label(frame_cad_funcionario, text='Usuário:', width=20, anchor=W).grid(row=5, column=0)
    Label(frame_cad_funcionario, text='Senha:', width=20, anchor=W).grid(row=6, column=0)

    entry_nome = Entry(frame_cad_funcionario, width=40)
    entry_data = Entry(frame_cad_funcionario, width=40)
    cmb_turno = Combobox(frame_cad_funcionario, width=37, values=['Diurno', 'Noturno'])
    entry_area = Entry(frame_cad_funcionario, width=40)
    entry_usuario = Entry(frame_cad_funcionario, width=40)
    entry_senha = Entry(frame_cad_funcionario, width=40)

    entry_nome.grid(row=1, column=1)
    entry_data.grid(row=2, column=1)
    cmb_turno.grid(row=3, column=1)
    entry_area.grid(row=4, column=1)
    entry_usuario.grid(row=5, column=1)
    entry_senha.grid(row=6, column=1)

    Button(frame_cad_funcionario, text='Próximo', command=lambda:[acad.cadastrar_instrutor(entry_nome.get(),
                                                                                            entry_data.get(),
                                                                                            cmb_turno.get(),
                                                                                            entry_usuario.get(),
                                                                                            entry_senha.get(),
                                                                                            entry_area.get(),
                                                                                            'Instrutor'),
                                                                                            menu_inicial(frame_cad_funcionario)]).grid(column=1)


def cadastrar_funcionario():
    frame_cad_funcionario = Frame(tela)
    frame_cad_funcionario.grid()
    button_home = Button(frame_cad_funcionario, text='Home', command=lambda:[menu_inicial(frame_cad_funcionario)]).grid(padx=5, pady=5)
    
    Label(frame_cad_funcionario, text='Cadastro de funcionário').grid(row=0, column=1, padx=100, pady=5)
    Label(frame_cad_funcionario, text='Nome:', width=20, anchor=W).grid(row=1, column=0)
    Label(frame_cad_funcionario, text='Data de admissão:', width=20, anchor=W).grid(row=2, column=0)
    Label(frame_cad_funcionario, text='Turno:', width=20, anchor=W).grid(row=3, column=0)
    Label(frame_cad_funcionario, text='Usuário:', width=20, anchor=W).grid(row=5, column=0)
    Label(frame_cad_funcionario, text='Senha:', width=20, anchor=W).grid(row=6, column=0)
    Label(frame_cad_funcionario, text='Função:', width=20, anchor=W).grid(row=7, column=0)

    

    entry_nome = Entry(frame_cad_funcionario, width=40)
    entry_data = Entry(frame_cad_funcionario, width=40)
    cmb_turno = Combobox(frame_cad_funcionario, width=37, values=['Diurno', 'Noturno'])
    entry_usuario = Entry(frame_cad_funcionario, width=40)
    entry_senha = Entry(frame_cad_funcionario, width=40)
    cmb_funcao = Combobox(frame_cad_funcionario, width=37, values=['Administrador',
                                                                    'Nutricionista',
                                                                    'Recepcionista',
                                                                    'Auxiliar de limpeza'])


    entry_nome.grid(row=1, column=1)
    entry_data.grid(row=2, column=1)
    cmb_turno.grid(row=3, column=1)
    entry_usuario.grid(row=5, column=1)
    entry_senha.grid(row=6, column=1)
    cmb_funcao.grid(row=7, column=1)

    Button(frame_cad_funcionario, text='Próximo', command=lambda:[acad.cadastrar_funcionario(entry_nome.get(),
                                                                                            entry_data.get(),
                                                                                            cmb_turno.get(),
                                                                                            entry_usuario.get(),
                                                                                            entry_senha.get(),
                                                                                            cmb_funcao.get()),
                                                                                            menu_inicial(frame_cad_funcionario)]).grid(column=1)

    
def menu_inicial(fr):
    fr.destroy()
    frame.grid()


def buscar_funcionario():
    frame.grid_forget()
    frame_info = Frame(tela)
    frame_info.grid()
    button_home = Button(frame_info, text='Home', command=lambda:[menu_inicial(frame_info)]).grid(padx=5, pady=5)
    Label(frame_info, text='Busca de funcionário').grid(row=0, column=1, padx=100, pady=5)
    Label(frame_info, text='Digite o nome do funcionário:').grid(row=1, column=0, pady=5)
    Label(frame_info, text='Digite a função do funcionário:').grid(row=2, column=0, pady=5)

    entry_nome = Entry(frame_info, width=40)
    entry_func = Entry(frame_info, width=40)

    entry_nome.grid(row=1, column=1)
    entry_func.grid(row=2, column=1)

    Button(frame_info, text='Próximo', command=lambda:[resultados_busca(acad.buscar_funcionario(entry_func.get(), entry_nome.get())),
                                                        frame_info.destroy()]).grid(column=1)


def resultados_busca(resultado):
    frame_info = Frame(tela)
    frame_info.grid()
    button_home = Button(frame_info, text='Home', command=lambda:[menu_inicial(frame_info)]).grid(padx=5, pady=5)
    Label(frame_info, text='Resultados da busca', font='helvetica 10 bold').grid(row=0, column=1, padx=100, pady=5)
    Label(frame_info, text='Resultado:').grid(row=1, column=0)

    txt_result = ScrolledText(frame_info, height=5, width=60)
    txt_result.grid(row=1, column=1)
    txt_result.insert(END, f'{resultado}')


def buscar_treino():
    frame.grid_forget()
    frame_info = Frame(tela)
    frame_info.grid()
    button_home = Button(frame_info, text='Home', command=lambda:[menu_inicial(frame_info)]).grid(padx=5, pady=5)
    Label(frame_info, text='Busca de treino').grid(row=0, column=1, padx=100, pady=5)
    Label(frame_info, text='Digite o nome do cliente:').grid(row=1, column=0, pady=5)
    Label(frame_info, text='Digite o nome do instrutor:').grid(row=2, column=0, pady=5)

    entry_cliente = Entry(frame_info, width=40)
    entry_instrutor = Entry(frame_info, width=40)

    entry_cliente.grid(row=1, column=1)
    entry_instrutor.grid(row=2, column=1)

    Button(frame_info, text='Próximo', command=lambda:[resultados_busca(acad.buscar_treino(entry_cliente.get(), entry_instrutor.get())),
                                                        frame_info.destroy()]).grid(column=1)


def busca_por_instrutor():
    frame.grid_forget()
    frame_info = Frame(tela)
    frame_info.grid()
    button_home = Button(frame_info, text='Home', command=lambda:[menu_inicial(frame_info)]).grid(padx=5, pady=5)
    Label(frame_info, text='Busca de treino').grid(row=0, column=1, padx=100, pady=5)
    Label(frame_info, text='Digite o nome do instrutor:').grid(row=1, column=0, pady=5)

    entry_instrutor = Entry(frame_info, width=40)

    entry_instrutor.grid(row=1, column=1)

    Button(frame_info, text='Próximo', command=lambda:[resultados_busca(acad.busca_por_instrutor(entry_instrutor.get())),
                                                        frame_info.destroy()]).grid(column=1)


tela = Tk()

tela.geometry('620x400+200+100')
tela.title('Academia Bolinha')
tela.iconbitmap('images/alter_icon0000.ico')
tela.resizable(0,0)

frame = Frame(tela)


button1 = Button(frame, text='Cadastrar treino', command=cadastrar_treino)
button2 = Button(frame, text='Cadastrar funcionário', command=tela_cadastro_funcionarios)
button3 = Button(frame, text='Buscar funcionário', command=buscar_funcionario)
button4 = Button(frame, text='Buscar treino', command=buscar_treino)
button5 = Button(frame, text='Treinos por instrutor', command=busca_por_instrutor)
frame.grid()
button1.grid(row=0, column=0, padx=(25,5), pady=20)
button2.grid(row=0, column=1, padx=5, pady=20)
button3.grid(row=0, column=2, padx=5, pady=20)
button4.grid(row=0, column=3, padx=5, pady=20)
button5.grid(row=0, column=4, padx=5, pady=20)

login()


tela.mainloop()