"""
12_frame.py
───────────
Widget: Frame — Contenedor para organizar otros widgets
Tkinter básico

Un Frame es como una "caja invisible" que agrupa widgets.
Sirve para organizar el layout dividiendo la ventana en zonas.

Regla importante:
  NUNCA mezcles pack() y grid() en el MISMO contenedor.
  Puedes usar pack() en la ventana principal y grid()
  dentro de un Frame hijo — eso sí está permitido.
"""

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("12 — Widget Frame")
root.geometry("480x380")
root.configure(bg="#F0F4F8")
root.resizable(False, False)

tk.Label(root, text="Organización con Frames",
         font=("Arial", 14, "bold"), fg="#1F4E79", bg="#F0F4F8").pack(pady=10)

# ── Frame izquierdo ───────────────────────────────────────────────────────────
frame_izq = tk.LabelFrame(root, text="Formulario",
                           font=("Arial", 11, "bold"),
                           bg="#F0F4F8", padx=10, pady=10)
frame_izq.pack(side=tk.LEFT, padx=15, pady=10, fill=tk.Y)

tk.Label(frame_izq, text="Nombre:", font=("Arial", 11), bg="#F0F4F8").grid(
    row=0, column=0, sticky="e", pady=8)
entry_nombre = tk.Entry(frame_izq, width=18, font=("Arial", 11), relief="solid", bd=1)
entry_nombre.grid(row=0, column=1, pady=8, padx=5)

tk.Label(frame_izq, text="Email:", font=("Arial", 11), bg="#F0F4F8").grid(
    row=1, column=0, sticky="e", pady=8)
entry_email = tk.Entry(frame_izq, width=18, font=("Arial", 11), relief="solid", bd=1)
entry_email.grid(row=1, column=1, pady=8, padx=5)

def guardar():
    nombre = entry_nombre.get().strip()
    email  = entry_email.get().strip()
    if not nombre or not email:
        messagebox.showerror("Error", "Completa todos los campos.")
        return
    texto_area.insert(tk.END, f"• {nombre} — {email}\n")
    entry_nombre.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    messagebox.showinfo("Guardado", f"'{nombre}' agregado a la lista.")

tk.Button(frame_izq, text="Guardar",
          font=("Arial", 11, "bold"), bg="#4CAF50", fg="white",
          command=guardar).grid(row=2, column=0, columnspan=2, pady=10)

# ── Frame derecho ─────────────────────────────────────────────────────────────
frame_der = tk.LabelFrame(root, text="Registros",
                           font=("Arial", 11, "bold"),
                           bg="#F0F4F8", padx=10, pady=10)
frame_der.pack(side=tk.RIGHT, padx=15, pady=10, fill=tk.BOTH, expand=True)

texto_area = tk.Text(frame_der, width=22, height=12,
                     font=("Arial", 10), relief="solid", bd=1)
texto_area.pack()

root.mainloop()
