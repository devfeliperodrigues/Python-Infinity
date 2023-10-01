'''Faça um programa que recebe o nome de um aluno recebe 4 notas desse aluno e mostra na tela qual foi a média das notas e também mostre um texto da cor verde escrito "aprovado"
se a média for maior ou igual a 6 e um texto vermelho escrito "Reprovado" se a nota for abaixo de 6'''
from tkinter import *

janela = Tk()

def aprovacao():
    
    media = ((float(nota1_entry.get()) + float(nota2_entry.get()) + float(nota3_entry.get()) + float(nota4_entry.get()))/4)

    if media >= 6.0:
        resultado.config(text=f"{nome_entrada.get()}, sua média é {media}! Você foi APROVADO", bg="green")
    if media < 6.0:
        resultado.config(text=f"{nome_entrada.get()}, sua média é {media}... Você foi REPROVADO", bg="red")

titulo = Label(text="Sistema Escolar")
titulo.pack()

titulo_entrada_nome = Label(text="Insira o nome do aluno").pack()
nome_entrada = Entry()
nome_entrada.pack()

titulo_entrada_nota1 = Label(text="A primeira nota do aluno.").pack()
nota1_entry = Entry()
nota1_entry.pack()

titulo_entrada_nota2 = Label(text="A segunda nota do aluno.").pack()
nota2_entry = Entry()
nota2_entry.pack()

titulo_entrada_nota3 = Label(text="A terceira nota do aluno.").pack()
nota3_entry = Entry()
nota3_entry.pack()

titulo_entrada_nota4 = Label(text="A quarta nota do aluno.").pack()
nota4_entry = Entry()
nota4_entry.pack()

resultado = Label(text="").pack()

botao_enviar = Button(janela, text="Enviar", width=20, command=aprovacao)
botao_enviar.pack()

janela.mainloop()
