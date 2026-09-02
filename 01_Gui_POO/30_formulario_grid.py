"""
30_formulario_grid.py
─────────────────────
Formulario con grid() — layout profesional estilo Northwind
Tkinter POO — nivel de transición

Muestra cómo usar grid() directamente en la ventana principal
con múltiples campos alineados y botones en un Frame separado.

Regla: el título usa columnspan=2 para ocupar las dos columnas.
cursor="hand2" → cambia el cursor al pasar sobre el botón.
"""

import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("30 — Formulario con grid()")
ventana.geometry("500x380")
ventana.configure(bg='white', padx=20, pady=20)
ventana.resizable(False, False)

# ── Título ────────────────────────────────────────────────────────────────────
tk.Label(ventana,
         text="FORMULARIO DE REGISTRO",
         font=("Arial", 16, "bold"),
         fg="#1F4E79",
         bg="white").grid(row=0, column=0, columnspan=2, pady=(0, 20))

# ── Campos con grid() ─────────────────────────────────────────────────────────
# sticky="e" → alinea el Label a la derecha
# La columna 1 recibe el Entry alineado a la izquierda (sticky="w" por defecto)
campos = [
    ("Nombre:",   "nombre"),
    ("Apellido:", "apellido"),
    ("Edad:",     "edad"),
    ("Email:",    "email"),
    ("Teléfono:", "telefono"),
]
entries = {}

for i, (lbl, key) in enumerate(campos, start=1):
    tk.Label(ventana, text=lbl,
             font=("Arial", 12), bg="white").grid(
        row=i, column=0, sticky="e", padx=(0, 10), pady=8)

    e = tk.Entry(ventana, width=25, font=("Arial", 12),
                 relief="solid", bd=1)
    e.grid(row=i, column=1, pady=8)
    entries[key] = e

# ── Botones en Frame ──────────────────────────────────────────────────────────
# Se usa un Frame para agrupar botones y luego usar columnspan=2
frame_botones = tk.Frame(ventana, bg="white")
frame_botones.grid(row=len(campos)+1, column=0,
                   columnspan=2, pady=(20, 0))

def guardar_datos():
    datos = {k: e.get().strip() for k, e in entries.items()}
    vacios = [k for k, v in datos.items() if not v]
    if vacios:
        messagebox.showerror("Error",
            f"Completa estos campos: {', '.join(vacios)}")
        return
    mensaje = "DATOS GUARDADOS:\n\n"
    for campo, valor in datos.items():
        mensaje += f"{campo.capitalize()}: {valor}\n"
    messagebox.showinfo("Éxito", mensaje)

def limpiar_campos():
    for e in entries.values():
        e.delete(0, tk.END)
    messagebox.showinfo("Limpiar", "Formulario limpiado.")

tk.Button(frame_botones, text="GUARDAR",
          font=("Arial", 12, "bold"),
          bg="#4CAF50", fg="white", width=12,
          cursor="hand2",
          command=guardar_datos).pack(side="left", padx=10)

tk.Button(frame_botones, text="LIMPIAR",
          font=("Arial", 12, "bold"),
          bg="#FF9800", fg="white", width=12,
          cursor="hand2",
          command=limpiar_campos).pack(side="left", padx=10)

# ── Notas sobre grid() ────────────────────────────────────────────────────────
# grid(row=, column=)  → posición en la cuadrícula
# columnspan=N         → ocupa N columnas
# sticky="e"           → alinea al Este (derecha)
# sticky="w"           → alinea al Oeste (izquierda)
# padx, pady           → espacio horizontal y vertical

ventana.mainloop()
