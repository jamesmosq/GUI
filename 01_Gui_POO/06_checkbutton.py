"""
06_checkbutton.py
─────────────────
Widget: Checkbutton — Casilla de verificación (selección múltiple)
Tkinter básico

Conceptos clave:
  IntVar()       → variable de control: 0=desmarcado, 1=marcado
  variable=      → vincula el Checkbutton a su IntVar
  variable.get() → lee el estado (0 o 1)
  variable.set() → cambia el estado por código
"""

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("06 — Widget Checkbutton")
root.geometry("360x300")
root.configure(bg="white")
root.resizable(False, False)

tk.Label(root, text="¿Qué tecnologías conoces?",
         font=("Arial", 13, "bold"), fg="#1F4E79", bg="white").pack(pady=15)

# Cada Checkbutton necesita su propio IntVar
var_python = tk.IntVar()
var_java   = tk.IntVar()
var_sql    = tk.IntVar()
var_web    = tk.IntVar()

for texto, variable in [
    ("Python",   var_python),
    ("Java",     var_java),
    ("SQL",      var_sql),
    ("HTML/CSS", var_web),
]:
    tk.Checkbutton(root, text=texto, variable=variable,
                   font=("Arial", 12), bg="white").pack(anchor="w", padx=60)

def ver_seleccion():
    seleccionadas = []
    if var_python.get(): seleccionadas.append("Python")
    if var_java.get():   seleccionadas.append("Java")
    if var_sql.get():    seleccionadas.append("SQL")
    if var_web.get():    seleccionadas.append("HTML/CSS")

    if not seleccionadas:
        messagebox.showwarning("Sin selección", "No marcaste ninguna opción.")
        return
    messagebox.showinfo("Tu selección", "Conoces: " + ", ".join(seleccionadas))

def limpiar():
    for v in [var_python, var_java, var_sql, var_web]:
        v.set(0)
    messagebox.showinfo("Limpiar", "Selección reiniciada.")

frame_btn = tk.Frame(root, bg="white")
frame_btn.pack(pady=15)

tk.Button(frame_btn, text="Ver selección",
          font=("Arial", 11, "bold"), bg="#4CAF50", fg="white",
          width=13, command=ver_seleccion).pack(side=tk.LEFT, padx=5)

tk.Button(frame_btn, text="Limpiar",
          font=("Arial", 11, "bold"), bg="#FF9800", fg="white",
          width=10, command=limpiar).pack(side=tk.LEFT, padx=5)

root.mainloop()
