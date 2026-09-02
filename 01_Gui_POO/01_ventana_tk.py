"""
01_ventana_tk.py
────────────────
Widget: Tk — Ventana principal
Tkinter básico — punto de entrada de cualquier app

Métodos importantes de la ventana:
  root.geometry('600x400')         → tamaño ancho x alto
  root.title('...')                → título de la barra
  root.configure(bg='#color')      → color de fondo
  root.resizable(False, False)     → bloquea redimensión (ancho, alto)
"""

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

# Configuración básica — siempre al inicio
root.geometry('600x400')
root.title('01 — Mi primera ventana')
root.configure(bg='#1F4E79')
root.resizable(False, False)

# Label de bienvenida
tk.Label(
    root,
    text="¡Bienvenido a Tkinter!",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#1F4E79"
).pack(expand=True)

tk.Label(
    root,
    text="Esta es la ventana principal (Tk)",
    font=("Arial", 12),
    fg="#BDD7EE",
    bg="#1F4E79"
).pack()

# Botón para cerrar con confirmación
def cerrar():
    if messagebox.askyesno("Salir", "¿Deseas cerrar la ventana?"):
        root.destroy()

tk.Button(
    root,
    text="Cerrar",
    font=("Arial", 11, "bold"),
    bg="#f44336",
    fg="white",
    width=12,
    command=cerrar
).pack(pady=30)

root.mainloop()
# NOTA: Nada debe ir después de mainloop() — no se ejecutará.
