"""
09_menu.py
──────────
Widget: Menu — Barra de menú con opciones desplegables
Tkinter básico

Conceptos clave:
  Menu(root)              → crea el menú raíz
  root.config(menu=...)   → asigna el menú a la ventana
  add_cascade()           → agrega un menú desplegable
  add_command()           → agrega una opción clickeable
  add_separator()         → agrega una línea divisoria
  tearoff=0               → evita la línea punteada superior
"""

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("09 — Widget Menu")
root.geometry("500x350")
root.configure(bg="white")
root.resizable(False, False)

# ── Barra de menú ────────────────────────────────────────────────────────────
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Menú Archivo
menu_archivo = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Nuevo",
    command=lambda: messagebox.showinfo("Archivo", "Nuevo archivo creado."))
menu_archivo.add_command(label="Abrir",
    command=lambda: messagebox.showinfo("Archivo", "Abrir archivo..."))
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir",
    command=lambda: root.destroy()
    if messagebox.askyesno("Salir", "¿Deseas cerrar?") else None)

# Menú Editar
menu_editar = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Editar", menu=menu_editar)
menu_editar.add_command(label="Copiar",
    command=lambda: messagebox.showinfo("Editar", "Copiar"))
menu_editar.add_command(label="Pegar",
    command=lambda: messagebox.showinfo("Editar", "Pegar"))

# Menú Ayuda
menu_ayuda = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Ayuda", menu=menu_ayuda)
menu_ayuda.add_command(label="Acerca de",
    command=lambda: messagebox.showinfo("Acerca de",
        "09 — Widget Menu\nTkinter Básico\nPOO Nivel 3"))

# ── Cuerpo ───────────────────────────────────────────────────────────────────
tk.Label(root,
         text="Usa el menú superior para navegar",
         font=("Arial", 14), fg="#1F4E79", bg="white").pack(expand=True)

tk.Label(root,
         text="Archivo → Salir para cerrar con confirmación",
         font=("Arial", 11), fg="gray", bg="white").pack(pady=10)

root.mainloop()
