"""
03_button.py
────────────
Widget: Button — Botón clickeable
Tkinter básico

Propiedades principales:
  text=     → texto del botón
  command=  → función que se ejecuta al hacer clic
  bg=       → color de fondo
  fg=       → color del texto
  width=    → ancho en caracteres
  state=    → 'normal' | 'disabled'
"""

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("03 — Widget Button")
root.geometry("380x320")
root.configure(bg="white")
root.resizable(False, False)

tk.Label(root, text="Ejemplos de Button",
         font=("Arial", 14, "bold"), fg="#1F4E79", bg="white").pack(pady=15)

# Botón básico con messagebox (mejor que print para apps GUI)
def saludar():
    messagebox.showinfo("Saludo", "¡Hola! Has presionado el botón.")

tk.Button(root,
          text="Saludar",
          font=("Arial", 11, "bold"),
          bg="#4CAF50", fg="white",
          width=15,
          command=saludar).pack(pady=8)

# Botón con confirmación
def eliminar():
    if messagebox.askyesno("Confirmar", "¿Seguro que deseas eliminar?"):
        messagebox.showinfo("Eliminado", "Elemento eliminado correctamente.")
    else:
        messagebox.showinfo("Cancelado", "Operación cancelada.")

tk.Button(root,
          text="Eliminar (con confirm)",
          font=("Arial", 11, "bold"),
          bg="#f44336", fg="white",
          width=20,
          command=eliminar).pack(pady=8)

# Botón que se deshabilita a sí mismo
btn_unico = None
def clic_unico():
    btn_unico.config(state="disabled", text="Ya fue presionado")
    messagebox.showinfo("Listo", "Este botón solo funciona una vez.")

btn_unico = tk.Button(root,
                       text="Solo un clic",
                       font=("Arial", 11, "bold"),
                       bg="#2196F3", fg="white",
                       width=15,
                       command=clic_unico)
btn_unico.pack(pady=8)

# Botón para cerrar
tk.Button(root,
          text="Cerrar",
          font=("Arial", 11, "bold"),
          bg="#FF9800", fg="white",
          width=15,
          command=lambda: root.destroy()
          if messagebox.askyesno("Salir", "¿Cerrar la aplicación?")
          else None).pack(pady=8)

root.mainloop()
