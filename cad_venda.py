import tkinter as tk
from tkinter import ttk, messagebox
from inserir_venda import inserir_vendas, listar_produtos, listar_clientes, listar_funcionarios

def create_cad_venda(parent, go_back, show_screen):
    frame = tk.Frame(parent)

    produtos = listar_produtos()       # [(id, nome, preco), ...]
    clientes = listar_clientes()       # [(id, nome), ...]
    funcionarios = listar_funcionarios()  # [(id, nome), ...]

    tk.Label(frame, text="Produto:").pack(pady=5)
    combo_produto = ttk.Combobox(frame, values=[p[1] for p in produtos], state="readonly", width=37)
    combo_produto.pack()

    tk.Label(frame, text="Quantidade:").pack(pady=5)
    entry_quantidade = tk.Entry(frame, width=40)
    entry_quantidade.pack()

    tk.Label(frame, text="Preço:").pack(pady=5)
    entry_preco = tk.Entry(frame, width=40)
    entry_preco.pack()

    tk.Label(frame, text="Funcionario:").pack(pady=5)
    combo_funcionario = ttk.Combobox(frame, values=[f[1] for f in funcionarios], state="readonly", width=37)
    combo_funcionario.pack()

    tk.Label(frame, text="Cliente:").pack(pady=5)
    combo_cliente = ttk.Combobox(frame, values=[c[1] for c in clientes], state="readonly", width=37)
    combo_cliente.pack()

    def atualizar_preco(event=None):
        produto = combo_produto.get()
        for p in produtos:
            if p[1] == produto:
                entry_preco.delete(0, tk.END)
                entry_preco.insert(0, str(p[2]))
                break

    combo_produto.bind("<<ComboboxSelected>>", atualizar_preco)

    def cadastrar_venda():
        produto_nome = combo_produto.get()
        quantidade = entry_quantidade.get()
        preco = entry_preco.get()
        cliente_nome = combo_cliente.get()
        funcionario_nome = combo_funcionario.get()

        if produto_nome == "" or quantidade == "" or preco == "" or cliente_nome == "":
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
            return

        try:
            idx_p = combo_produto.current()
            idx_f = combo_funcionario.current()
            idx_c = combo_cliente.current()

            product_id = produtos[idx_p][0]
            funcionario_id = funcionarios[idx_f][0]
            cliente_id = clientes[idx_c][0]

            inserir_vendas(product_id, quantidade, preco, funcionario_id, cliente_id)
            messagebox.showinfo("Sucesso", "Venda cadastrada com sucesso!")
            entry_quantidade.delete(0, tk.END)
            entry_preco.delete(0, tk.END)
            combo_produto.set("")
            if clientes:
                combo_cliente.set(clientes[0][1])
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível cadastrar: {e}")

    tk.Button(frame, text="Cadastrar", command=cadastrar_venda).pack(pady=5)
    tk.Button(frame, text="Exibir Vendas", width=20,
              command=lambda: show_screen("listar_vendas")).pack(pady=15, padx=15)
    tk.Button(frame, text="Voltar", width=12, command=go_back).pack(pady=5)

    return frame
