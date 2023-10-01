from tkinter import *

janela.Tk()

def maior(n1,n2):

    numero1 = int(numero1_entry.get())
    numero2 = int(numero2_entry.get())

    if numero1 > numero2:
        print(f"{n1} é maior que {n2}.")
    elif numero1 == numero2:
        print(f"{n1} e {n2} são iguais.")
    else:
        print(f"{n2} é maior que {n1}.")

maior()
        