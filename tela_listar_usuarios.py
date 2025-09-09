import tkinter as tk
from tkinter import messagebox
from inserir_usuario import listar_usuarios, excluir_usuario

def create_exibir_usuarios(parent, go_back, show_screen):
    frame = tk.Frame(parent)

    usuarios = listar_usuarios()
    if not usuarios:
        messagebox.showinfo("Usuários", "Nenhum usuário cadastrado.")
        tk.Button(frame, text="Voltar", width=12, command=go_back).pack(pady=10)
        return frame

    tk.Label(frame, text="Usuários cadastrados:", font=("Arial", 12, "bold")).pack(pady=10)

    listbox = tk.Listbox(frame, width=60, height=10)
    listbox.pack(padx=10, pady=10, fill="both", expand=True)

    for nome, senha in usuarios:
        listbox.insert(tk.END, f"{nome} | {senha}")

    def atualizar_lista():
        listbox.delete(0, tk.END)
        for n, s in listar_usuarios():
            listbox.insert(tk.END, f"{n} | {s}")

    def excluir():
        sel = listbox.curselection()
        if not sel:
            messagebox.showwarning("Aviso", "Selecione um usuário para excluir.")
            return
        usuario = listbox.get(sel[0]).split(" | ")[0]
        if messagebox.askyesno("Confirmação", f"Deseja realmente excluir o usuário '{usuario}'?"):
            excluir_usuario(usuario)
            messagebox.showinfo("Sucesso", f"Usuário '{usuario}' excluído com sucesso.")
            atualizar_lista()

    tk.Button(frame, text="Excluir Usuário", width=20, command=excluir).pack(pady=5)
    tk.Button(frame, text="Voltar", width=12, command=go_back).pack(pady=5)
    return frame
