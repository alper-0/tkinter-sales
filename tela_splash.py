import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import subprocess

def abrir_janela_principal():
    splash.destroy()
    # abre o principal após o splash
    subprocess.Popen(["python", "principal.py"])

# Splash
splash = tk.Tk()
splash.overrideredirect(True)
W, H = 500, 350
sw, sh = splash.winfo_screenwidth(), splash.winfo_screenheight()
x, y = (sw - W) // 2, (sh - H) // 2
splash.geometry(f"{W}x{H}+{x}+{y}")
splash.config(bg="white")

# conteúdo centralizado
wrap = tk.Frame(splash, bg="white")
wrap.place(relx=0.5, rely=0.5, anchor="center")

logo_path = "image.png"
if os.path.exists(logo_path):
    from PIL import Image
    img = Image.open(logo_path).resize((220, 200), Image.Resampling.LANCZOS)
    logo = ImageTk.PhotoImage(img)
    tk.Label(wrap, image=logo, bg="white").pack()
else:
    messagebox.showwarning("Aviso", f"Arquivo de logo não encontrado:\n{logo_path}")
    tk.Label(wrap, text="Seu Sistema", font=("Arial", 22), bg="white").pack()

tk.Label(wrap, text="Carregando...", bg="white", font=("Arial", 15)).pack(pady=10)

splash.after(2500, abrir_janela_principal)
splash.mainloop()
