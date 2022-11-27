import tkinter as tk
from tkinter import ttk
import datetime as dt
lista_tipos = ["FIN", "KO","TKO","DEC"]
lista_versus = ["vitor belfor","anderson silva","jacare"]
lista_round = ["1","2","3",]
lista_codigo = []

janela = tk.Tk()

#criação de função

def inserir_codigo():
    descricao= entry_descricao.get()
    tipo = combobox_selecionar_tipo.get()
    round = combobox_selecionar_round.get()
    versus = combobox_selecionar_versus.get()



    data_criacao = dt.datetime.now()
    data_criacao = data_criacao.strftime("%d/%m/%y %H:%M")
    codigo = len(lista_codigo)+1
    codigo_str = "COD-{}".format(codigo)
    lista_codigo.append((codigo_str, descricao, tipo, round, versus, data_criacao))


#titulo da janela

janela.title('CADASTRO DA ORGANIZAÇÃO FIGHT NIGHT')

label_descricao = tk.Label(text='EVENTO')
label_descricao.grid(row=1, column=0, padx= 10, pady=10, sticky= 'nswe', columnspan=4)
entry_descricao =tk.Entry()
entry_descricao.grid(row=2, column=0, padx=10, pady=10, sticky= 'nswe', columnspan= 4)

label_tipo = tk.Label(text='VENCEU POR')
label_tipo.grid(row=3, column=0, padx=10, pady=10, sticky= 'nswe', columnspan=1)
entry_tipo = tk.Entry()
entry_tipo.grid(row=3, column=1, padx=10, pady=10, sticky= 'nswe', columnspan=4)

label_versus = tk.Label(text='VERSUS')
label_versus.grid(row=4, column=0, padx=10, pady=10, sticky= 'nswe', columnspan=1)
entry_versus = tk.Entry()
entry_versus.grid(row=4, column=1, padx=10, pady=10, sticky= 'nswe', columnspan=4)

label_round = tk.Label(text='ROUND')
label_round.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
entry_round = tk.Entry()
entry_round.grid(row=5, column=2, padx=10, pady=10, sticky='nswe', columnspan=4)

combobox_selecionar_tipo = ttk.Combobox(values=lista_tipos)
combobox_selecionar_tipo.grid(row=3, column=3, padx=10, pady=10, sticky='nswe', columnspan=4)
combobox_selecionar_versus = ttk.Combobox(values=lista_versus)
combobox_selecionar_versus.grid(row=4, column=3, padx=10, pady=10, sticky='nswe', columnspan=4)
combobox_selecionar_round = ttk.Combobox(values=lista_round)
combobox_selecionar_round.grid(row=5, column=3, padx=10, pady=10, sticky='nswe', columnspan=4)




botao_criar_codigo = tk.Button(text='criar codigo', command=inserir_codigo)
botao_criar_codigo.grid(row=6, column=0, padx=10, pady=10, columnspan=4)



janela.mainloop()

print(lista_codigo)

