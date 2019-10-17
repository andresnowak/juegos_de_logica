from numpy.random import randint as rnd
from tkinter import *

lista = [1,2,3,5]
def randomizer(list_op):
    list_rnd = []
    list_new_op = []
        
    while len(list_rnd) < len(list_op):
        rnd_n = rnd(0, len(list_op)) #Porque tenemos 28 botones en total, nunca toca el 28

        if rnd_n in list_rnd:
            continue
        else:
            list_new_op.append(list_op[rnd_n])
            list_rnd.append(rnd_n)

    return list_new_op

def sum_substraction():
    a = 0
    b = 0
    suma = 0

    list_op = []

    for _ in range(14):
        a = rnd(1, 11)
        b = rnd(1, 11)
        suma = a + b

        list_op.append(f"{a} + {b}")
        list_op.append(str(suma))

    return list_op

dkm = sum_substraction()

def use_after():
    title.configure(text="hesknxkllo")


window = Tk()
window.geometry("400x300")
title = Label(window, text="0 s", font="Arial 30", width=10)
title.pack()
title.after(1000, use_after) #se pone sin parentesis ya que queremos una referencia no que se llame la funcion inmediatamente
window.mainloop()


        