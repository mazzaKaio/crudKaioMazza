# CRIAR MENU E BOTAO DIREITO MOUSE

from tkinter import *

class Janela:
    def __init__(self, tk):
        self.menu = Menu(tk, tearoff=0)
        self.menu.add_command(label="Ola 1", command=self.ola)
        self.menu.add_command(label="Ola 2", command=self.ola)

        frame = Frame(tk, width=200, height=200)
        frame.pack()
        frame.bind("<Button-3>", self.popup)

        mainloop()
    
    def ola(self): 
        print("Olá!")

    def popup(self, e): self.menu.post(e.x_root, e.y_root)

raiz = Tk()
Janela(raiz)
raiz.mainloop()