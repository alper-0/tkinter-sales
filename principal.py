import tkinter as tk
from tkinter import messagebox

# import page factories
from cad_cliente import create_cad_cliente
from cad_funcionario import create_cad_funcionario
from cad_produto import create_cad_produto
from cad_usuario import create_cad_usuario
from cad_venda import create_cad_venda
from tela_listar_usuarios import create_exibir_usuarios
from tela_listar_vendas import create_exibir_vendas

# -------- Screen manager --------
root = tk.Tk()
root.title("Sistema Principal")
root.resizable(False, False)

# center window on screen
W, H = 500, 450
sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
x, y = (sw - W) // 2, (sh - H) // 2
root.geometry(f"{W}x{H}+{x}+{y}")

# container that will hold pages
container = tk.Frame(root)
container.pack(fill="both", expand=True)

current_frame = None

def go_back():
    show_screen("menu")

def show_screen(name):
    """Destroy current page and show the requested one centered."""
    global current_frame
    if current_frame is not None:
        current_frame.destroy()

    # maps names to factories (each factory builds a Frame)
    pages = {
        "menu": create_menu,
        "clientes":      lambda p: create_cad_cliente(p, go_back, show_screen),
        "funcionarios":  lambda p: create_cad_funcionario(p, go_back, show_screen),
        "produtos":      lambda p: create_cad_produto(p, go_back, show_screen),
        "usuarios":      lambda p: create_cad_usuario(p, go_back, show_screen),
        "vendas":        lambda p: create_cad_venda(p, go_back, show_screen),
        "listar_usuarios": lambda p: create_exibir_usuarios(p, go_back, show_screen),
        "listar_vendas":   lambda p: create_exibir_vendas(p, go_back, show_screen),
    }

    factory = pages[name]
    # page is created as a child of container
    current_frame = factory(container)
    # place it perfectly centered
    current_frame.place(relx=0.5, rely=0.5, anchor="center")

def sair():
    if messagebox.askyesno("Sair", "Deseja encerrar o sistema?"):
        root.destroy()

# -------- Menu screen (no "Exibir/Listar" buttons here) --------
def create_menu(parent):
    frame = tk.Frame(parent)

    title = tk.Label(frame, text="Menu Principal", font=("Arial", 16, "bold"))
    title.pack(pady=15)

    btns = [
        ("Clientes",       lambda: show_screen("clientes")),
        ("Funcionários",   lambda: show_screen("funcionarios")),
        ("Produtos",       lambda: show_screen("produtos")),
        ("Usuários",       lambda: show_screen("usuarios")),
        ("Vendas",         lambda: show_screen("vendas")),
    ]

    # buttons block (centered)
    btn_block = tk.Frame(frame)
    btn_block.pack(pady=10)
    for text, cmd in btns:
        tk.Button(btn_block, text=text, width=22, command=cmd).pack(pady=6)

    tk.Button(frame, text="Encerrar Sistema", width=22, command=sair, bg="red", fg="white").pack(pady=18)
    return frame

# start on menu
show_screen("menu")
root.mainloop()
