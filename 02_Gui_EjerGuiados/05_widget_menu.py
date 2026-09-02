"""
05_widget_menu.py
─────────────────
Widget: Menu (barra de menú con opciones desplegables)
Tkinter — Nivel básico

Conceptos:
  • Menu(root)              → crea el menú raíz
  • root.config(menu=...)  → asigna el menú a la ventana
  • add_cascade()           → agrega un menú desplegable
  • add_command()           → agrega una opción clickeable
  • add_separator()         → agrega una línea divisoria
  • tearoff=0               → evita la línea punteada superior
"""

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("05 — Widget Menu")
root.geometry("500x350")
root.configure(bg="white")
root.resizable(False, False)

# ── Barra de menú ─────────────────────────────────────────────────────────────
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
    command=lambda: root.destroy() if messagebox.askyesno("Salir", "¿Deseas salir?") else None)

# Menú Ver
menu_ver = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Ver", menu=menu_ver)
menu_ver.add_command(label="Acerca de",
    command=lambda: messagebox.showinfo("Acerca de",
        "05 — Widget Menu\nTkinter Básico\nPOO Nivel 3"))

# ── Cuerpo de la ventana ──────────────────────────────────────────────────────
tk.Label(root,
         text="Usa el menú superior para navegar",
         font=("Arial", 14), fg="#1F4E79", bg="white").pack(expand=True)

tk.Label(root,
         text="Menú > Archivo > Salir para cerrar",
         font=("Arial", 11), fg="gray", bg="white").pack(pady=10)

root.mainloop()
