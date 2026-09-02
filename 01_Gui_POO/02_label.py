"""
02_label.py
───────────
Widget: Label — Etiqueta de texto
Tkinter básico

Propiedades principales:
  text=       → texto a mostrar
  font=       → fuente (familia, tamaño, estilo)
  fg=         → color del texto
  bg=         → color de fondo
  wraplength= → ancho máximo antes de hacer salto de línea
"""

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("02 — Widget Label")
root.geometry("420x320")
root.configure(bg="white")
root.resizable(False, False)

# Label básico
tk.Label(root,
         text="Label básico",
         font=("Arial", 12),
         bg="white").pack(pady=8)

# Label con color
tk.Label(root,
         text="Label con color de texto y fondo",
         font=("Arial", 12),
         fg="white",
         bg="#1F4E79",
         padx=10, pady=5).pack(pady=8)

# Label con fuente personalizada
tk.Label(root,
         text="Label con fuente Arial 16 bold",
         font=("Arial", 16, "bold"),
         fg="#2E74B5",
         bg="white").pack(pady=8)

# Label con wraplength (texto largo)
tk.Label(root,
         text="Este es un texto largo que se ajusta automáticamente al ancho definido en wraplength",
         font=("Arial", 11),
         bg="white",
         wraplength=300,
         justify="center").pack(pady=8)

# Label que se actualiza dinámicamente
lbl_contador = tk.Label(root,
                         text="Clics: 0",
                         font=("Arial", 12, "bold"),
                         fg="#4CAF50",
                         bg="white")
lbl_contador.pack(pady=5)

contador = [0]

def contar():
    contador[0] += 1
    lbl_contador.config(text=f"Clics: {contador[0]}")
    if contador[0] == 5:
        messagebox.showinfo("Meta", "¡Llegaste a 5 clics!")

tk.Button(root, text="Clic aquí",
          font=("Arial", 11, "bold"),
          bg="#4CAF50", fg="white",
          command=contar).pack(pady=5)

root.mainloop()
