import tkinter as tk
from tkinter import messagebox
from inserir_produto import inserir_produto  # DB

def create_cad_produto(parent, go_back, show_screen):
    frame = tk.Frame(parent)

    tk.Label(frame, text="Nome:").pack(pady=5)
    entry_nome = tk.Entry(frame, width=40)
    entry_nome.pack()

    tk.Label(frame, text="Descrição:").pack(pady=5)
    entry_descricao = tk.Entry(frame, width=40)
    entry_descricao.pack()

    tk.Label(frame, text="Valor:").pack(pady=5)
    entry_valor = tk.Entry(frame, width=40)
    entry_valor.pack()

    def cadastrar_produto():
        nome = entry_nome.get()
        descricao = entry_descricao.get()
        valor = entry_valor.get()

        if nome == "" or descricao == "" or valor == "":
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
            return

        try:
            inserir_produto(nome, descricao, valor)
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
            entry_nome.delete(0, tk.END)
            entry_descricao.delete(0, tk.END)
            entry_valor.delete(0, tk.END)
            entry_nome.focus_set()
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível cadastrar: {e}")

    tk.Button(frame, text="Cadastrar", command=cadastrar_produto).pack(pady=15)
    tk.Button(frame, text="Voltar", width=12, command=go_back).pack(pady=5)

    return frame
