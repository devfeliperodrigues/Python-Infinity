from tkinter import *

def saudacao():
    print(f"Seja Bem vindo {nome_entrada.get()}")
    nome_entrada.delete(0, END)


janela = Tk()

azul_claro = "#e9fdf4" 
azul_escuro = "#213261"

titulo = Label(text="Bem vindo",bg="red",foreground="white")
titulo.pack()

nome_texto = Label(text="Nome")
nome_texto.pack()

nome_entrada = Entry(bg=azul_escuro, fg=azul_claro, width=30)
nome_entrada.pack()



botao_enviar = Button(janela, text="Enviar", width=20, command=saudacao)
botao_enviar.pack()

janela.mainloop()