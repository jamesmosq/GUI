"""
04_entry.py
───────────
Widget: Entry — Campo de texto de una línea
Tkinter básico

Métodos principales:
  entry.get()           → leer el contenido
  entry.delete(0, END)  → borrar todo
  entry.insert(0, txt)  → insertar texto
  entry.config(show="*")→ ocultar texto (contraseña)
"""

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("04 — Widget Entry")
root.geometry("380x300")
root.configure(bg="white")
root.resizable(False, False)

tk.Label(root, text="Ejemplos de Entry",
         font=("Arial", 14, "bold"), fg="#1F4E79", bg="white").pack(pady=10)

# Entry básico
tk.Label(root, text="Nombre:", font=("Arial", 12), bg="white").pack()
entry_nombre = tk.Entry(root, width=30, font=("Arial", 12), relief="solid", bd=1)
entry_nombre.pack(pady=5)

# Entry para contraseña
tk.Label(root, text="Contraseña:", font=("Arial", 12), bg="white").pack()
entry_pass = tk.Entry(root, width=30, font=("Arial", 12),
                      relief="solid", bd=1, show="*")  # show="*" oculta el texto
entry_pass.pack(pady=5)

def mostrar_datos():
    nombre = entry_nombre.get().strip()
    if not nombre:
        messagebox.showwarning("Advertencia", "El campo Nombre está vacío.")
        return
    messagebox.showinfo("Datos leídos",
                        f"Nombre: {nombre}\nContraseña: {'*' * len(entry_pass.get())}")

def limpiar():
    entry_nombre.delete(0, tk.END)
    entry_pass.delete(0, tk.END)
    messagebox.showinfo("Limpiar", "Campos limpiados.")

frame_btn = tk.Frame(root, bg="white")
frame_btn.pack(pady=15)

tk.Button(frame_btn, text="Leer datos",
          font=("Arial", 11, "bold"), bg="#4CAF50", fg="white",
          width=12, command=mostrar_datos).pack(side=tk.LEFT, padx=5)

tk.Button(frame_btn, text="Limpiar",
          font=("Arial", 11, "bold"), bg="#FF9800", fg="white",
          width=12, command=limpiar).pack(side=tk.LEFT, padx=5)

root.mainloop()
