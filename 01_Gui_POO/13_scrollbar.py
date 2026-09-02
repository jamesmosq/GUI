"""
13_scrollbar.py
───────────────
Widget: Scrollbar — Barra de desplazamiento
Tkinter básico

La Scrollbar debe estar VINCULADA a otro widget.
No funciona sola. El enlace se hace en dos pasos:

  scrollbar = Scrollbar(frame, command=widget.yview)
  widget.config(yscrollcommand=scrollbar.set)
"""

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("13 — Scrollbar vinculada")
root.geometry("400x380")
root.configure(bg="white")
root.resizable(False, False)

tk.Label(root, text="Scrollbar + Listbox y Text",
         font=("Arial", 13, "bold"), fg="#1F4E79", bg="white").pack(pady=10)

# ── Scrollbar + Listbox ───────────────────────────────────────────────────────
tk.Label(root, text="Listbox con Scrollbar:",
         font=("Arial", 11), bg="white").pack(anchor="w", padx=20)

frame_lista = tk.Frame(root, bg="white")
frame_lista.pack(padx=20, pady=5, fill=tk.X)

listbox = tk.Listbox(frame_lista, width=40, height=6,
                     font=("Arial", 10),
                     selectbackground="#2196F3", selectforeground="white")
listbox.pack(side=tk.LEFT)

sb_lista = tk.Scrollbar(frame_lista, command=listbox.yview)
sb_lista.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=sb_lista.set)

for i in range(1, 21):
    listbox.insert(tk.END, f"Elemento {i:02d}")

# ── Scrollbar + Text ──────────────────────────────────────────────────────────
tk.Label(root, text="Text con Scrollbar:",
         font=("Arial", 11), bg="white").pack(anchor="w", padx=20, pady=(10, 0))

frame_text = tk.Frame(root, bg="white")
frame_text.pack(padx=20, pady=5, fill=tk.X)

text_box = tk.Text(frame_text, width=40, height=5,
                   font=("Arial", 10), relief="solid", bd=1)
text_box.pack(side=tk.LEFT)

sb_text = tk.Scrollbar(frame_text, command=text_box.yview)
sb_text.pack(side=tk.RIGHT, fill=tk.Y)
text_box.config(yscrollcommand=sb_text.set)

for i in range(1, 16):
    text_box.insert(tk.END, f"Línea {i} de contenido en el Text widget\n")

tk.Button(root, text="Ver selección del Listbox",
          font=("Arial", 10, "bold"), bg="#4CAF50", fg="white",
          command=lambda: messagebox.showinfo(
              "Seleccionado",
              listbox.get(listbox.curselection()[0])
              if listbox.curselection()
              else "Ninguno seleccionado")
          ).pack(pady=8)

root.mainloop()
