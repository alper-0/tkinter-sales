import tkinter as tk
from tkinter import messagebox
from inserir_funcionario import inserir_funcionario  # DB

def create_cad_funcionario(parent, go_back, show_screen):
    frame = tk.Frame(parent)

    tk.Label(frame, text="Nome:").pack(pady=5)
    entry_nome = tk.Entry(frame, width=40)
    entry_nome.pack()

    tk.Label(frame, text="Idade:").pack(pady=5)
    entry_idade = tk.Entry(frame, width=40)
    entry_idade.pack()

    tk.Label(frame, text="Setor:").pack(pady=5)
    entry_setor = tk.Entry(frame, width=40)
    entry_setor.pack()

    def cadastrar_funcionario():
        nome = entry_nome.get()
        idade = entry_idade.get()
        setor = entry_setor.get()

        if nome == "" or idade == "" or setor == "":
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
            return

        try:
            inserir_funcionario(nome, idade, setor)
            messagebox.showinfo("Sucesso", "Funcionario cadastrado com sucesso!")
            entry_nome.delete(0, tk.END)
            entry_idade.delete(0, tk.END)
            entry_setor.delete(0, tk.END)
            entry_nome.focus_set()
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível cadastrar: {e}")

    tk.Button(frame, text="Cadastrar", command=cadastrar_funcionario).pack(pady=15)
    tk.Button(frame, text="Voltar", width=12, command=go_back).pack(pady=5)

    return frame
