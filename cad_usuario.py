import tkinter as tk
from tkinter import messagebox
from inserir_usuario import inserir_usuario  # DB

def create_cad_usuario(parent, go_back, show_screen):
    frame = tk.Frame(parent)

    tk.Label(frame, text="Nome:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entry_nome = tk.Entry(frame, width=30)
    entry_nome.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(frame, text="Senha:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    entry_senha = tk.Entry(frame, width=30, show="*")
    entry_senha.grid(row=1, column=1, padx=10, pady=10)

    def limpar():
        entry_nome.delete(0, tk.END)
        entry_senha.delete(0, tk.END)
        entry_nome.focus()

    def salvar():
        nome = entry_nome.get()
        senha = entry_senha.get()
        if not (nome and senha):
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return
        inserir_usuario(nome, senha)
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        limpar()

    tk.Button(frame, text="Salvar", width=12, command=salvar).grid(row=2, column=0, padx=10, pady=15)
    tk.Button(frame, text="Limpar", width=12, command=limpar).grid(row=2, column=1, padx=10, pady=15, sticky="e")

    # open users list inside same window
    tk.Button(frame, text="Exibir Usuários", width=20,
              command=lambda: show_screen("listar_usuarios")).grid(row=3, column=0, columnspan=2, pady=10)

    # enter key behavior
    entry_nome.bind("<Return>", lambda e: entry_senha.focus())
    entry_senha.bind("<Return>", lambda e: salvar())

    tk.Button(frame, text="Voltar", width=12, command=go_back).grid(row=4, column=0, columnspan=2, pady=5)

    entry_nome.focus()
    return frame
