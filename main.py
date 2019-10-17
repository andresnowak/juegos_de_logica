#\!/usr/bin/env python
'''
|| Name: Andres Nowak
|| Date: Wed Oct  9 09:19:51 CDT 2019
'''
from tkinter import *
from memorama import memorama

def main():
    window = Tk()
    window.title("Juegos de logica")

    memorama(window)
    window.mainloop()

if __name__ == "__main__":
    main()