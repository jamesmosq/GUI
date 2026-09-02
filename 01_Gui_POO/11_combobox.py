"""
11_combobox.py
──────────────
Widget: Combobox (ttk) — Lista desplegable
Tkinter básico

Métodos principales:
  combo.get()           → leer el elemento seleccionado
  combo.set("texto")    → seleccionar un elemento por código
  combo['values'] = [...] → cambiar las opciones
  combo.current(0)      → seleccionar por índice
"""

import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("11 — Widget Combobox")
root.geometry("380x280")
root.configure(bg="white")
root.resizable(False, False)

tk.Label(root, text="Selección con Combobox",
         font=("Arial", 13, "bold"), fg="#1F4E79", bg="white").pack(pady=15)

tk.Label(root, text="Elige tu lenguaje favorito:",
         font=("Arial", 12), bg="white").pack()

combo = ttk.Combobox(root,
                     values=["Python", "Java", "JavaScript", "C#", "Kotlin", "Go"],
                     width=25,
                     font=("Arial", 11),
                     state="readonly")  # readonly: solo permite elegir de la lista
combo.pack(pady=8)
combo.set("Selecciona una opción")

tk.Label(root, text="Elige tu nivel:",
         font=("Arial", 12), bg="white").pack(pady=(10, 0))

combo_nivel = ttk.Combobox(root,
                            values=["Básico", "Intermedio", "Avanzado"],
                            width=25,
                            font=("Arial", 11),
                            state="readonly")
combo_nivel.pack(pady=8)
combo_nivel.current(0)  # selecciona el primer elemento por defecto

def ver_seleccion():
    lenguaje = combo.get()
    nivel    = combo_nivel.get()
    if lenguaje == "Selecciona una opción":
        messagebox.showwarning("Advertencia", "Selecciona un lenguaje.")
        return
    messagebox.showinfo("Tu selección",
                        f"Lenguaje: {lenguaje}\nNivel: {nivel}")

tk.Button(root, text="Ver selección",
          font=("Arial", 11, "bold"), bg="#4CAF50", fg="white",
          width=15, command=ver_seleccion).pack(pady=12)

root.mainloop()
