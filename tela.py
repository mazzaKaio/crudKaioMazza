import tkinter as tk
from tkinter import messagebox
from crud import create_user, read_users, update_user, delete_user

class CRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CRUD USUARIOS")

        # criacao de widgets
        self.create_widgets()
    
    def create_widgets(self):
        # LABELS
        tk.Label(self.root, text="Nome:").grid(row=0,column=0)
        tk.Label(self.root, text="Telefone:").grid(row=1,column=0)
        tk.Label(self.root, text="Email:").grid(row=2,column=0)
        tk.Label(self.root, text="Usuario:").grid(row=3,column=0)
        tk.Label(self.root, text="Senha:").grid(row=4,column=0)

        tk.Label(self.root, text="User ID(for update/delete):").grid(row=5,column=0)

        # CRIAR E POSICIONAR AS CAIXAS PARA DIGITAR OS VALORES
        self.nome_entry = tk.Entry(self.root) 
        self.telefone_entry = tk.Entry(self.root)
        self.email_entry = tk.Entry(self.root)
        self.usuario_entry = tk.Entry(self.root)
        self.senha_entry = tk.Entry(self.root)

        self.userId_entry = tk.Entry(self.root)

        self.nome_entry.grid(row=0, column=1)
        self.telefone_entry.grid(row=1, column=1)
        self.email_entry.grid(row=2, column=1)
        self.usuario_entry.grid(row=3, column=1)
        self.senha_entry.grid(row=4, column=1)

        self.userId_entry.grid(row=5, column=1)

        # BOTOES DO CURD
        tk.Button(self.root, text="Criar usuario", command=self.create_user).grid(row=6,column=0,columnspan=1)
        tk.Button(self.root, text="Listar usuarios", command=self.read_users).grid(row=6,column=1,columnspan=1)
        tk.Button(self.root, text="Alterar usuario", command=self.uptade_user).grid(row=7,column=0,columnspan=1)
        tk.Button(self.root, text="Excluir usuario", command=self.delete_user).grid(row=7,column=1,columnspan=1)
    
    def create_user(self):
        nome = self.nome_entry.get()
        telefone = self.telefone_entry.get()
        email = self.email_entry.get()
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()

        if nome and telefone and email and usuario and senha:
            create_user(nome, telefone, email, usuario, senha)

            self.nome_entry.delete(0, tk.END)
            self.telefone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.usuario_entry.delete(0, tk.END)
            self.senha_entry.delete(0, tk.END)

            messagebox.showinfo("Success", "Usuario criado com sucesso!")
        else:
            messagebox.showerror("Error", "Todos os campos são obrigatórios!")

    def read_users(self):
        users = read_users()
        self.text_area.delete(1.0,tk.END)

        for user in users:
            self.text_area.insert(tk.END, f"ID:{user[0]}, Nome:{user[1]}, Telefone:{user[2]}, Email:{user[3]}\n")
    
    def uptade_user(self):
        user_id = self.userId_entry.get()
        nome = self.nome_entry.get()
        telefone = self.telefone_entry.get()
        email = self.email_entry.get()
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()

        if user_id and nome and telefone and email and usuario and senha:
            update_user(user_id, nome, telefone, email, usuario, senha)

            self.nome_entry.delete(0, tk.END)
            self.telefone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.usuario_entry.delete(0, tk.END)
            self.senha_entry.delete(0, tk.END)

            messagebox.showinfo("Success", "Usuario alterado com sucesso!")
        else:
            messagebox.showerror("Error", "Todos os campos são obrigatórios!")

    def delete_user(self):
        user_id = self.userId_entry.get()
        if user_id:
            delete_user(user_id)
            self.userId_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Usuario excluido com sucess!")
        else:
            messagebox.showerror("Error", "ID do usuario é obrigatorio!")
    
if __name__ == "__main__":
    root = tk.Tk()
    app = CRUDApp(root)
    root.mainloop()