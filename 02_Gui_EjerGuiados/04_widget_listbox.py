"""
04_widget_listbox.py
────────────────────
Widget: Listbox (lista de elementos seleccionables)
Tkinter — Nivel básico

Métodos principales:
  listbox.insert(tk.END, "texto") → agrega al final
  listbox.delete(índice)          → elimina por posición
  listbox.get(índice)             → obtiene el texto de una posición
  listbox.curselection()          → retorna tupla con índices seleccionados
  listbox.size()                  → cantidad total de elementos
"""

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("04 — Widget Listbox")
root.geometry("380x360")
root.configure(bg="white")
root.resizable(False, False)

tk.Label(root, text="Lista de elementos:",
         font=("Arial", 12, "bold"), fg="#1F4E79", bg="white").pack(pady=10)

# Entry para ingresar elementos
frame_entrada = tk.Frame(root, bg="white")
frame_entrada.pack()
entry = tk.Entry(frame_entrada, width=22, font=("Arial", 12),
                 relief="solid", bd=1)
entry.pack(side=tk.LEFT, padx=5)

# Listbox con Scrollbar
frame_lista = tk.Frame(root, bg="white")
frame_lista.pack(pady=8)

listbox = tk.Listbox(frame_lista, width=30, height=7,
                     font=("Arial", 11),
                     selectbackground="#2196F3", selectforeground="white")
listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame_lista, command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)

# Datos de ejemplo
for item in ["Python", "Java", "JavaScript", "C++", "Kotlin"]:
    listbox.insert(tk.END, item)

def agregar():
    texto = entry.get().strip()
    if not texto:
        messagebox.showwarning("Vacío", "Escribe algo antes de agregar.")
        return
    listbox.insert(tk.END, texto)
    entry.delete(0, tk.END)

def eliminar():
    sel = listbox.curselection()
    if not sel:
        messagebox.showwarning("Sin selección", "Selecciona un elemento primero.")
        return
    nombre = listbox.get(sel[0])
    listbox.delete(sel[0])
    messagebox.showinfo("Eliminado", f"'{nombre}' eliminado.")

def ver_seleccion():
    sel = listbox.curselection()
    if not sel:
        messagebox.showwarning("Sin selección", "Selecciona un elemento primero.")
        return
    messagebox.showinfo("Seleccionado",
        f"Elemento: {listbox.get(sel[0])}\nTotal en lista: {listbox.size()}")

frame_btn = tk.Frame(root, bg="white")
frame_btn.pack(pady=8)
for txt, color, cmd in [
    ("Agregar",  "#4CAF50", agregar),
    ("Eliminar", "#f44336", eliminar),
    ("Ver info", "#2196F3", ver_seleccion),
]:
    tk.Button(frame_btn, text=txt, font=("Arial", 10, "bold"),
              bg=color, fg="white", width=9,
              command=cmd).pack(side=tk.LEFT, padx=4)

root.mainloop()
