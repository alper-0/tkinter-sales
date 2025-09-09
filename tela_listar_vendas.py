import tkinter as tk
from tkinter import messagebox
from lista_vendas import listar_vendas, excluir_venda

def create_exibir_vendas(parent, go_back, show_screen):
    frame = tk.Frame(parent)

    vendas = listar_vendas()
    if not vendas:
        messagebox.showinfo("Vendas", "Nenhum venda cadastrado.")
        tk.Button(frame, text="Voltar", width=12, command=go_back).pack(pady=10)
        return frame

    tk.Label(frame, text="Vendas cadastradas:", font=("Arial", 12, "bold")).pack(pady=10)

    listbox = tk.Listbox(frame, width=80, height=12)
    listbox.pack(padx=10, pady=10, fill="both", expand=True)

    for idv, id_cliente, id_funcionario, id_produto, valor_total, data_venda in vendas:
        listbox.insert(tk.END, f"{idv} | {id_cliente} | {id_funcionario} | {id_produto} | {valor_total} | {data_venda}")

    def atualizar_lista():
        listbox.delete(0, tk.END)
        for idv, id_cliente, id_funcionario, id_produto, valor_total, data_venda in listar_vendas():
            listbox.insert(tk.END, f"{idv} | {id_cliente} | {id_funcionario} | {id_produto} | {valor_total} | {data_venda}")

    def excluir():
        sel = listbox.curselection()
        if not sel:
            messagebox.showwarning("Aviso", "Selecione uma venda para excluir.")
            return
        venda_id = listbox.get(sel[0]).split(" | ")[0]
        if messagebox.askyesno("Confirmação", f"Deseja realmente excluir a venda '{venda_id}'?"):
            excluir_venda(venda_id)
            messagebox.showinfo("Sucesso", f"Venda '{venda_id}' excluída com sucesso.")
            atualizar_lista()

    tk.Button(frame, text="Excluir Venda", width=20, command=excluir).pack(pady=5)
    tk.Button(frame, text="Voltar", width=12, command=go_back).pack(pady=5)
    return frame
    