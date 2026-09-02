"""
02_widget_checkbutton.py
────────────────────────
Widget: Checkbutton (casilla de verificación)
Tkinter — Nivel básico

Conceptos:
  • IntVar()       → variable de control: 0 = desmarcado, 1 = marcado
  • variable.get() → lee el estado actual
  • variable.set() → cambia el estado por código
"""

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("02 — Widget Checkbutton")
root.geometry("350x280")
root.configure(bg="white")
root.resizable(False, False)

tk.Label(root, text="¿Qué tecnologías conoces?",
         font=("Arial", 13, "bold"), fg="#1F4E79", bg="white").pack(pady=15)

# Cada Checkbutton necesita su propia IntVar
var_python = tk.IntVar()
var_html   = tk.IntVar()
var_sql    = tk.IntVar()

for texto, variable in [
    ("Python",  var_python),
    ("HTML/CSS", var_html),
    ("SQL",     var_sql),
]:
    tk.Checkbutton(root, text=texto, variable=variable,
                   font=("Arial", 12), bg="white").pack(anchor="w", padx=60)

def ver_seleccion():
    seleccionadas = []
    if var_python.get(): seleccionadas.append("Python")
    if var_html.get():   seleccionadas.append("HTML/CSS")
    if var_sql.get():    seleccionadas.append("SQL")

    if not seleccionadas:
        messagebox.showwarning("Sin selección", "No marcaste ninguna opción.")
        return
    messagebox.showinfo("Tu selección", "Conoces: " + ", ".join(seleccionadas))

def limpiar():
    var_python.set(0)
    var_html.set(0)
    var_sql.set(0)
    messagebox.showinfo("Limpiar", "Selección reiniciada.")

frame_btn = tk.Frame(root, bg="white")
frame_btn.pack(pady=15)

tk.Button(frame_btn, text="Ver selección", font=("Arial", 11, "bold"),
          bg="#4CAF50", fg="white", width=13,
          command=ver_seleccion).pack(side=tk.LEFT, padx=5)

tk.Button(frame_btn, text="Limpiar", font=("Arial", 11, "bold"),
          bg="#FF9800", fg="white", width=10,
          command=limpiar).pack(side=tk.LEFT, padx=5)

root.mainloop()
