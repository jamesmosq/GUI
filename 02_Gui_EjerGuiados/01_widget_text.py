"""
01_widget_text.py
─────────────────
Widget: Text (caja de texto multilínea)
Tkinter — Nivel básico

Diferencia con Entry:
  • Entry  → una sola línea
  • Text   → múltiples líneas (ideal para notas, descripciones)

Métodos principales:
  text.get("1.0", END)        → leer todo el contenido
  text.insert(END, "hola")    → insertar texto al final
  text.delete("1.0", END)     → borrar todo el contenido
"""

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("01 — Widget Text")
root.geometry("400x320")
root.configure(bg="white")
root.resizable(False, False)

tk.Label(root, text="Caja de texto (Text):",
         font=("Arial", 12, "bold"), bg="white").pack(pady=10)

# Widget Text: height = líneas visibles, width = caracteres por línea
text_box = tk.Text(root, height=8, width=40,
                   font=("Arial", 11), relief="solid", bd=1)
text_box.pack(padx=20)

def leer():
    contenido = text_box.get("1.0", tk.END).strip()
    if not contenido:
        messagebox.showwarning("Vacío", "La caja de texto está vacía.")
        return
    messagebox.showinfo("Contenido", contenido)

def limpiar():
    text_box.delete("1.0", tk.END)
    messagebox.showinfo("Limpiar", "Caja de texto limpiada.")

frame_btn = tk.Frame(root, bg="white")
frame_btn.pack(pady=10)

tk.Button(frame_btn, text="Leer", font=("Arial", 11, "bold"),
          bg="#2196F3", fg="white", width=10,
          command=leer).pack(side=tk.LEFT, padx=5)

tk.Button(frame_btn, text="Limpiar", font=("Arial", 11, "bold"),
          bg="#FF9800", fg="white", width=10,
          command=limpiar).pack(side=tk.LEFT, padx=5)

root.mainloop()
