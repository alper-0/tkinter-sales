import tkinter as tk
from tkinter import messagebox
from inserir_cliente import inserir_cliente  # DB

def create_cad_cliente(parent, go_back, show_screen):
    frame = tk.Frame(parent)

    tk.Label(frame, text="Nome:").pack(pady=5)
    entry_nome = tk.Entry(frame, width=40)
    entry_nome.pack()

    tk.Label(frame, text="Email:").pack(pady=5)
    entry_email = tk.Entry(frame, width=40)
    entry_email.pack()

    tk.Label(frame, text="Cidade:").pack(pady=5)
    entry_cidade = tk.Entry(frame, width=40)
    entry_cidade.pack()

    tk.Label(frame, text="Estado:").pack(pady=5)
    entry_estado = tk.Entry(frame, width=5)
    entry_estado.pack()

    def cadastrar_cliente():
        nome = entry_nome.get()
        email = entry_email.get()
        cidade = entry_cidade.get()
        estado = entry_estado.get()

        if nome == "" or email == "" or cidade == "" or estado == "":
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
            return

        try:
            inserir_cliente(nome, email, cidade, estado)
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
            entry_nome.delete(0, tk.END)
            entry_email.delete(0, tk.END)
            entry_cidade.delete(0, tk.END)
            entry_estado.delete(0, tk.END)
            entry_nome.focus_set()
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível cadastrar: {e}")

    tk.Button(frame, text="Cadastrar", command=cadastrar_cliente).pack(pady=15)
    tk.Button(frame, text="Voltar", width=12, command=go_back).pack(pady=5)

    return frame
