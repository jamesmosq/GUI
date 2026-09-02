"""
26_grid_sticky.py
─────────────────
Demostración de grid() y sticky — alineación de widgets
Tkinter intermedio

Valores de sticky:
  tk.W  (west)   → alinea a la izquierda
  tk.E  (east)   → alinea a la derecha
  tk.EW          → se estira horizontalmente (izquierda Y derecha)
  tk.NS          → se estira verticalmente
  tk.NSEW        → se estira en todas direcciones

columnconfigure(col, weight=1) → permite que la columna se expanda
"""

import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("26 — grid() y sticky")
root.geometry("420x280")
root.resizable(True, True)  # Redimensionable para ver el efecto de sticky=EW

frame = ttk.Frame(root, padding="20")
frame.pack(fill=tk.BOTH, expand=True)

tk.Label(frame, text="Demostración de sticky en grid()",
         font=("Arial", 12, "bold"), fg="#1F4E79").grid(
    row=0, column=0, columnspan=2, pady=(0, 15))

campos = [
    ("Nombre:",    "nombre"),
    ("Email:",     "email"),
    ("Documento:", "documento"),
    ("Ciudad:",    "ciudad"),
]
entries = {}

for i, (lbl, key) in enumerate(campos, start=1):
    # Label alineado a la derecha (sticky=E)
    ttk.Label(frame, text=lbl).grid(
        row=i, column=0, sticky=tk.E, pady=6, padx=(0, 8))

    # Entry que se estira horizontalmente (sticky=EW)
    e = ttk.Entry(frame, font=("Arial", 11))
    e.grid(row=i, column=1, sticky=tk.EW, pady=6)
    entries[key] = e

# Hace que la columna 1 se expanda al redimensionar
frame.columnconfigure(1, weight=1)

def guardar():
    datos = {k: e.get().strip() for k, e in entries.items()}
    vacios = [k for k, v in datos.items() if not v]
    if vacios:
        messagebox.showerror("Error", f"Faltan campos: {', '.join(vacios)}")
        return
    messagebox.showinfo("Guardado",
        "\n".join(f"{k.capitalize()}: {v}" for k, v in datos.items()))

tk.Button(frame, text="Guardar",
          font=("Arial", 11, "bold"), bg="#4CAF50", fg="white",
          command=guardar).grid(
    row=len(campos)+1, column=0, columnspan=2, pady=15, sticky=tk.EW)

root.mainloop()
