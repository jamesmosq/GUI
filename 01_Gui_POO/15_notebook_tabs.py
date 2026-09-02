"""
15_notebook_tabs.py
───────────────────
Widget: ttk.Notebook — Pestañas de navegación
Tkinter intermedio

Conceptos clave:
  notebook = ttk.Notebook(root)   → crea el contenedor de pestañas
  tab = ttk.Frame(notebook)       → cada pestaña es un Frame
  notebook.add(tab, text="...")   → agrega la pestaña con su etiqueta
  notebook.pack(expand=True, fill="both") → ocupa todo el espacio
"""

import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.geometry('500x350')
root.title("15 — Notebook con Pestañas")
root.resizable(False, False)

notebook = ttk.Notebook(root)

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

notebook.add(tab1, text="  Inicio  ")
notebook.add(tab2, text="  Datos   ")
notebook.add(tab3, text="  Ajustes ")
notebook.pack(expand=True, fill="both")

# ── Pestaña 1: Inicio ─────────────────────────────────────────────────────────
tk.Label(tab1, text="Bienvenido",
         font=("Arial", 18, "bold"), fg="#1F4E79").pack(pady=30)
tk.Label(tab1, text="Navega por las pestañas usando las etiquetas superiores.",
         font=("Arial", 11), wraplength=350).pack()
tk.Button(tab1, text="Ir a Datos",
          font=("Arial", 11, "bold"), bg="#2196F3", fg="white",
          command=lambda: notebook.select(tab2)).pack(pady=20)

# ── Pestaña 2: Datos ──────────────────────────────────────────────────────────
tk.Label(tab2, text="Formulario de Datos",
         font=("Arial", 14, "bold"), fg="#2E74B5").pack(pady=15)
frame_form = tk.Frame(tab2)
frame_form.pack()
tk.Label(frame_form, text="Nombre:", font=("Arial", 12)).grid(
    row=0, column=0, sticky="e", pady=8, padx=5)
entry_nombre = tk.Entry(frame_form, width=25, font=("Arial", 12), relief="solid", bd=1)
entry_nombre.grid(row=0, column=1, pady=8)

tk.Button(tab2, text="Guardar",
          font=("Arial", 11, "bold"), bg="#4CAF50", fg="white",
          command=lambda: messagebox.showinfo("Guardado",
              f"Nombre guardado: {entry_nombre.get()}" if entry_nombre.get()
              else "El campo está vacío")).pack(pady=10)

# ── Pestaña 3: Ajustes ────────────────────────────────────────────────────────
tk.Label(tab3, text="Ajustes de la Aplicación",
         font=("Arial", 14, "bold"), fg="#375623").pack(pady=20)
var_notif = tk.IntVar(value=1)
tk.Checkbutton(tab3, text="Activar notificaciones",
               variable=var_notif, font=("Arial", 12)).pack(pady=5)
tk.Checkbutton(tab3, text="Modo oscuro",
               font=("Arial", 12)).pack(pady=5)
tk.Button(tab3, text="Aplicar ajustes",
          font=("Arial", 11, "bold"), bg="#375623", fg="white",
          command=lambda: messagebox.showinfo("Ajustes",
              "Ajustes guardados correctamente.")).pack(pady=15)

root.mainloop()
