"""
03_widget_radiobutton.py
────────────────────────
Widget: Radiobutton (botón de opción — selección única)
Tkinter — Nivel básico

Diferencia con Checkbutton:
  • Checkbutton → varios pueden estar marcados (IntVar por cada uno)
  • Radiobutton → solo UNO puede estar marcado a la vez (StringVar compartido)

Conceptos:
  • StringVar()    → variable compartida entre todos los Radiobutton
  • value=         → valor que se asigna al StringVar al seleccionar ese botón
  • variable.get() → retorna el value del botón seleccionado
"""

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("03 — Widget Radiobutton")
root.geometry("350x300")
root.configure(bg="white")
root.resizable(False, False)

tk.Label(root, text="¿Cuál es tu nivel de Python?",
         font=("Arial", 13, "bold"), fg="#1F4E79", bg="white").pack(pady=15)

# UN solo StringVar compartido por todos los Radiobutton
var_nivel = tk.StringVar(value="Básico")  # valor seleccionado por defecto

for nivel in ["Básico", "Intermedio", "Avanzado"]:
    tk.Radiobutton(root,
                   text=nivel,
                   variable=var_nivel,  # todos apuntan a la misma variable
                   value=nivel,         # valor que toma la variable al seleccionar
                   font=("Arial", 12),
                   bg="white").pack(anchor="w", padx=60)

def ver_nivel():
    nivel = var_nivel.get()
    messagebox.showinfo("Tu nivel", f"Seleccionaste: {nivel}")

def reiniciar():
    var_nivel.set("Básico")
    messagebox.showinfo("Reiniciar", "Nivel restablecido a Básico.")

frame_btn = tk.Frame(root, bg="white")
frame_btn.pack(pady=20)

tk.Button(frame_btn, text="Ver nivel", font=("Arial", 11, "bold"),
          bg="#4CAF50", fg="white", width=12,
          command=ver_nivel).pack(side=tk.LEFT, padx=5)

tk.Button(frame_btn, text="Reiniciar", font=("Arial", 11, "bold"),
          bg="#FF9800", fg="white", width=12,
          command=reiniciar).pack(side=tk.LEFT, padx=5)

root.mainloop()
