"""
19_treeview_notebook.py
───────────────────────
Treeview dentro de Notebook
Tkinter intermedio — combinación de widgets

Muestra cómo colocar un Treeview dentro de una pestaña
y cómo cargar datos iniciales en la tabla.
"""

import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("19 — Treeview dentro de Notebook")
root.geometry("560x380")
root.resizable(False, False)

notebook = ttk.Notebook(root)

tab_tabla  = ttk.Frame(notebook)
tab_info   = ttk.Frame(notebook)

notebook.add(tab_tabla, text="  Tabla de Datos  ")
notebook.add(tab_info,  text="  Información     ")
notebook.pack(expand=True, fill="both")

# ── Pestaña 1: Treeview ───────────────────────────────────────────────────────
tk.Label(tab_tabla, text="Estudiantes",
         font=("Arial", 12, "bold"), fg="#1F4E79").pack(pady=8)

frame_tree = tk.Frame(tab_tabla)
frame_tree.pack(padx=15, fill=tk.BOTH, expand=True)

cols = ("ID", "Nombre", "Edad", "Ciudad")
tree = ttk.Treeview(tab_tabla, columns=cols, show="headings", height=8)

for col, w in zip(cols, [50, 160, 60, 120]):
    tree.heading(col, text=col)
    tree.column(col, width=w, anchor="w")

sb = ttk.Scrollbar(tab_tabla, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=sb.set)
tree.pack(side=tk.LEFT, padx=15, fill=tk.BOTH, expand=True)
sb.pack(side=tk.RIGHT, fill=tk.Y, pady=5)

for row in [
    (1, "Juan García",    25, "Medellín"),
    (2, "María López",    30, "Bogotá"),
    (3, "Pedro Ramírez",  22, "Cali"),
    (4, "Ana Martínez",   28, "Barranquilla"),
    (5, "Carlos Torres",  35, "Bucaramanga"),
]:
    tree.insert("", tk.END, values=row)

def ver_detalle(event):
    sel = tree.selection()
    if sel:
        v = tree.item(sel[0])["values"]
        messagebox.showinfo("Detalle",
            f"ID: {v[0]}\nNombre: {v[1]}\nEdad: {v[2]}\nCiudad: {v[3]}")

tree.bind("<<TreeviewSelect>>", ver_detalle)

# ── Pestaña 2: Información ────────────────────────────────────────────────────
tk.Label(tab_info, text="¿Cómo funciona?",
         font=("Arial", 13, "bold"), fg="#1F4E79").pack(pady=20)
tk.Label(tab_info,
         text="El Treeview muestra datos en formato de tabla.\n"
              "Haz clic en una fila para ver su detalle.\n\n"
              "Está vinculado a un Scrollbar para navegar\n"
              "cuando hay muchas filas.",
         font=("Arial", 11), justify="center", wraplength=350).pack(pady=10)

root.mainloop()
