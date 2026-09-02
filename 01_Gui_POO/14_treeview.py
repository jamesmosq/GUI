"""
14_treeview.py
──────────────
Widget: Treeview (ttk) — Tabla de datos interactiva
Tkinter básico

Métodos principales:
  tree.heading("col", text="...")  → nombre de columna
  tree.column("col", width=...)   → ancho de columna
  tree.insert("", END, values=()) → insertar fila
  tree.selection()                → filas seleccionadas
  tree.item(item_id)['values']    → datos de la fila
  tree.delete(item_id)            → eliminar fila
  tree.get_children()             → todos los items
"""

import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("14 — Widget Treeview")
root.geometry("520x400")
root.resizable(False, False)

tk.Label(root, text="Tabla con Treeview",
         font=("Arial", 13, "bold"), fg="#1F4E79").pack(pady=10)

# ── Treeview ──────────────────────────────────────────────────────────────────
frame_tree = tk.Frame(root)
frame_tree.pack(padx=20, fill=tk.BOTH, expand=True)

columnas = ("ID", "Nombre", "Lenguaje", "Nivel")
tree = ttk.Treeview(frame_tree, columns=columnas, show="headings", height=8)

for col, w in zip(columnas, [50, 150, 120, 100]):
    tree.heading(col, text=col)
    tree.column(col, width=w, anchor="w")

sb = ttk.Scrollbar(frame_tree, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=sb.set)
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
sb.pack(side=tk.RIGHT, fill=tk.Y)

# Datos de ejemplo
datos = [
    (1, "Ana García",    "Python",     "Avanzado"),
    (2, "Luis Pérez",    "Java",       "Intermedio"),
    (3, "María López",   "JavaScript", "Básico"),
    (4, "Carlos Ruiz",   "Python",     "Intermedio"),
    (5, "Sandra Mora",   "SQL",        "Avanzado"),
]
for row in datos:
    tree.insert("", tk.END, values=row)

# Al seleccionar una fila, muestra detalle
def on_select(event):
    sel = tree.selection()
    if sel:
        valores = tree.item(sel[0])["values"]
        messagebox.showinfo("Detalle",
            f"ID: {valores[0]}\nNombre: {valores[1]}\n"
            f"Lenguaje: {valores[2]}\nNivel: {valores[3]}")

tree.bind("<<TreeviewSelect>>", on_select)

# Botón limpiar selección
tk.Button(root, text="Limpiar selección",
          font=("Arial", 10, "bold"), bg="#FF9800", fg="white",
          command=lambda: tree.selection_remove(tree.selection())
          ).pack(pady=8)

root.mainloop()
