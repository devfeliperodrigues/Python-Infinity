from tkinter import *
from maior import *

janela = Tk()

resposta = StringVar()

titulo = Label(text="maior dos dois")
titulo.pack()

numero1_label = Label(text="Digite o primeiro número: ")
numero1_label.pack()

numero1_entry = Entry()
numero1_entry.pack()

numero2_label = Label(text="Digite o segundo número: ")
numero2_label.pack()

numero2_entry = Entry()
numero2_entry.pack()

resultado = Label(textvariable=resposta)
resultado.pack()

botao_checar = Button(janela, text="Checando", command=maior(n1,n2))
botao_checar.pack()

janela.mainloop()




