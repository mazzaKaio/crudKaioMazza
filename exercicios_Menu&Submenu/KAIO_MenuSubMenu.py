# CRIAR MENU E SUB MENU

from tkinter import *

class Janela:
    def __init__(self, Tk):
        principal = Menu(Tk)
        arquivo = Menu(principal)
        arquivo.add_command(label="Abrir",command=self.abrir)
        arquivo.add_command(label="Salvar",command=self.salvar)
        principal.add_cascade(label="Arquivo",menu=arquivo)
        principal.add_command(label="Ajuda",command=self.ajuda)
        Tk.configure(menu = principal)
    
    def abrir(self): print ("abrir")
    def salvar(self): print ("salvar")
    def ajuda(self): print ("ajuda")

raiz = Tk()
Janela(raiz)
raiz.mainloop()