"""
07_radiobutton.py
─────────────────
Widget: Radiobutton — Botón de opción (selección única)
Tkinter básico

Diferencia con Checkbutton:
  Checkbutton → varios pueden marcarse a la vez (IntVar por cada uno)
  Radiobutton → solo UNO puede estar marcado (StringVar compartido)

Conceptos clave:
  StringVar()    → variable compartida por todos los Radiobutton
  value=         → valor que toma el StringVar al seleccionar ese botón
  variable.get() → retorna el value del botón seleccionado
"""

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("07 — Widget Radiobutton")
root.geometry("360x320")
root.configure(bg="white")
root.resizable(False, False)

tk.Label(root, text="¿Cuál es tu nivel de programación?",
         font=("Arial", 13, "bold"), fg="#1F4E79", bg="white").pack(pady=15)

# UN solo StringVar compartido por todos los Radiobutton
var_nivel = tk.StringVar(value="Básico")  # valor por defecto

for nivel in ["Básico", "Intermedio", "Avanzado", "Experto"]:
    tk.Radiobutton(root,
                   text=nivel,
                   variable=var_nivel,   # todos usan la misma variable
                   value=nivel,          # valor que se asigna al seleccionar
                   font=("Arial", 12),
                   bg="white").pack(anchor="w", padx=60, pady=2)

def ver_nivel():
    nivel = var_nivel.get()
    messagebox.showinfo("Tu nivel", f"Seleccionaste: {nivel}")

def reiniciar():
    var_nivel.set("Básico")
    messagebox.showinfo("Reiniciar", "Nivel restablecido a Básico.")

frame_btn = tk.Frame(root, bg="white")
frame_btn.pack(pady=20)

tk.Button(frame_btn, text="Ver nivel",
          font=("Arial", 11, "bold"), bg="#4CAF50", fg="white",
          width=12, command=ver_nivel).pack(side=tk.LEFT, padx=5)

tk.Button(frame_btn, text="Reiniciar",
          font=("Arial", 11, "bold"), bg="#FF9800", fg="white",
          width=12, command=reiniciar).pack(side=tk.LEFT, padx=5)

root.mainloop()
