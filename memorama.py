#!/usr/bin/env python
'''
|| Name: Andres Nowak
|| Date: Wed Oct  9 09:17:43 CDT 2019
'''
from tkinter import * 
from platform import system
from time import sleep
from threading import Thread
from numpy.random import randint as rnd

#_thread.start_new_thread(update,())

class memorama(Thread):
    def __init__(self, window):
        self.window = window

        self.window.geometry("400x300")
        spacer = Label(self.window, text="", padx=50)
        spacer.grid(column=0, row=0)
        self.title = Label(self.window, text="Memorama", pady=20)
        self.title.grid(column=1, row=0) #comienza desde cero la col y row
        self.start_game = False
        self.count_obj = 0

        if system() == "Darwin":
            self.system ="mac"
        else:
            self.system = "windows_linux"
        
        self.list_btn_clicked = []
        self.dict_btn = {}
        self.correct_buttons = []

        self.start()

    def start(self):
        """this function starts the game with option that 
        was chosen for the game"""
        sum_sub = Button(self.window, width = 20, height = 2, text="sum and substraction", command=lambda: self.option_chosen(1))
        mul_div = Button(self.window, width = 20, height = 2, text="division and multiplication", command=lambda: self.option_chosen(2))
        self.list_objs_canvas = [sum_sub, mul_div]

        sum_sub.grid(column=1, row=1)
        mul_div.grid(column=1, row=2)

        #self.create_butons(list_op)

    def restart_clicked(self):
        if self.start_game == True:
            if self.option == 1:
                self.list_op = self.sum_substraction()
            elif self.option == 2:
                self.list_op = self.mul_div()

            self.start_game = False
            self.destroy_objs_start()

    def start_clicked(self):
        if self.start_game == False:
            self.btns_blank(self.dict_btn)
            self.start_game = True

    def option_chosen(self, option):
        self.option = option

        if option == 1:
            self.list_op = self.sum_substraction()
        elif option == 2:
            self.list_op = self.mul_div()
        
        self.window.after(500, self.destroy_objs_start)

    def destroy_objs_start(self):
        if self.count_obj < len(self.list_objs_canvas):
            self.list_objs_canvas[self.count_obj].destroy()

            self.count_obj += 1
            self.window.after(100, self.destroy_objs_start)
        else:
            self.dict_btn = {}
            self.count_obj = 0
            self.list_objs_canvas = []
            self.start_game_func()

    def start_game_func(self):
            self.window.geometry("600x500")

            self.title.grid(column=2, row=0)

            self.start_btn = Button(self.window, width = 5, height = 2, text="start", command=lambda: self.start_clicked()) #Tienes que hacerlo lambda para que el comando no se active automaticamente
            self.start_btn.grid(column=0, row=0)

            self.restart_btn = Button(self.window, width = 5, height = 2, text="restart", command=lambda: self.restart_clicked()) #Tienes que hacerlo lambda para que el comando no se active automaticamente
            self.restart_btn.grid(column=4, row=0)
            self.list_objs_canvas = [self.start_btn, self.restart_btn]

            self.list_op = self.randomizer(self.list_op)

            self.create_butons(self.list_op)


    def btns_blank(self, list_btn):
        for btn in list_btn:
            btn.configure(text="", highlightbackground="white", bg="white")

    def btn_clicked(self, btn_name):
        if self.start_game == True:
            if btn_name not in self.correct_buttons:
                btn_name.configure(text=self.dict_btn[btn_name], highlightbackground="blue")

                self.list_btn_clicked.append(btn_name)

                if len(self.list_btn_clicked) == 2:
                    self.start_game = False
                    self.correct_incorrect()

    def correct_incorrect(self):
        """
        this function changes the color of the buttons depending 
        if the two buttons were the same or not
        """
        verify = self.verifier()

        for btn in self.list_btn_clicked:
            if self.system == "mac":
                if verify == True:
                    self.correct_buttons.append(btn)
                    btn.configure(text=self.dict_btn[btn], highlightbackground="green")
                else:
                    btn.configure(text=self.dict_btn[btn], highlightbackground="red")
            else:
                if verify == True:
                    self.correct_buttons.append(btn)
                    btn.configure(text=self.dict_btn[btn], bg="green")
                else:
                    btn.configure(text=self.dict_btn[btn], bg="red")

        if verify == False:
            self.window.after(1500, self.incorrect_answer)
        else:
            self.start_game = True
            self.list_btn_clicked = [] 

    def incorrect_answer(self):
        """ 

        """
        for btn in self.list_btn_clicked:
            btn.configure(text="")
            if self.system == "mac":
                btn.configure(highlightbackground="white")
            else:
                btn.configure(highlightbackground="white", bg="white")

        self.list_btn_clicked = [] 
        self.start_game = True

    def create_butons(self, list_op):
        """
        this function creates the buttons for the memorama
        """
        i = 0
        for row in range(1, 5):
            for col in range(5):
                btn = Button(self.window, width=10, height=5, text=str(list_op[i]))
                btn.grid(column = col, row = row)

                if self.system == "mac":
                    btn.configure(highlightbackground="white", fg="black", highlightthickness=13)
                else:
                    btn.configure(highlightbackground="white", fg="black", highlightthickness=5, bg="white")

                btn.configure(command=lambda button=btn: self.btn_clicked(button))

                self.dict_btn[btn] = btn["text"]
                self.list_objs_canvas.append(btn)

                i += 1

    def sum_substraction(self, n_op=10):
        """
        This function creates a list of sum and substractions operations
        """
        a = 0
        b = 0
        total = 0

        list_op = []

        for _ in range(n_op):
            a = rnd(1, 11)
            b = rnd(1, 11)
            sum_or_sub = rnd(0,2)

            if sum_or_sub == 0:
                total = a + b
                list_op.append(f"{a} + {b}")
            else:
                total = a - b
                list_op.append(f"{a} - {b}")

            list_op.append(str(total))

        return list_op

    def mul_div(self, n_op = 10):
        """
        This function creates a list of sum and substractions operations
        """
        a = 0
        b = 0
        total = 0
        n = 0

        list_op = []

        while n < n_op:
            a = rnd(1, 11)
            b = rnd(1, 11)
            mul_or_div = rnd(0,2)

            if mul_or_div == 0:
                total = a * b
                list_op.append(f"{a} X {b}")
                n += 1
            else:
                if a % b == 0:
                    total = a / b
                    list_op.append(f"{a} / {b}")
                    n += 1
                else:
                    continue


            list_op.append(str(int(total)))

        return list_op
        
    def randomizer(self, list_op):
        """
        this function randomizes the list it is passed
        """
        list_rnd = []
        list_new_op = []
        
        while len(list_rnd) < len(list_op):
            rnd_n = rnd(0, len(list_op)) #nunca toca el ultimo numero

            if rnd_n in list_rnd:
                continue
            else:
                list_new_op.append(list_op[rnd_n])
                list_rnd.append(rnd_n)

        return list_new_op

    def verifier(self):
        """
        this function verifies that the two buttons that are
        clicked are correct
        """
        op, result_op = self.sanitizer()

        op = op.split(" ")
        total = 0

        if len(op) == 1:
            return False
        elif result_op == 0:
            return False
        elif op[1] == "+":
            total = int(op[0]) + int(op[2])
        elif op[1] == "-":
            total = int(op[0]) - int(op[2])
        elif op[1] == "X":
            total = int(op[0]) * int(op[2])
        elif op[1] == "/":
            total = int(op[0]) / int(op[2])

        if total == int(result_op):
            return True
        else:
            return False
        
    def sanitizer(self):
        result_op  = 0
        op = ""

        for btn in self.list_btn_clicked:
            if len(self.dict_btn[btn]) <= 2:
                result_op = self.dict_btn[btn]
            else:
                op = self.dict_btn[btn]

        return op, result_op


"""Que hace lambda, porque parece que logra pasar lo que no era un objeto como un objeto, los botones ahora tienen numeros, ahora si tienen un puntero."""
        