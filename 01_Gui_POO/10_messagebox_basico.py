"""
10_messagebox_basico.py
───────────────────────
Módulo: messagebox — Cuadros de diálogo de mensajes
Tkinter básico

Tipos de messagebox:
  showinfo()      → información (botón OK)
  showwarning()   → advertencia (botón OK)
  showerror()     → error (botón OK)
  askyesno()      → pregunta Sí/No → retorna True o False
  askokcancel()   → OK/Cancelar    → retorna True o False
  askyesnocancel()→ Sí/No/Cancelar → True, False o None
"""

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("10 — messagebox básico")
root.geometry("380x360")
root.configure(bg="white")
root.resizable(False, False)

tk.Label(root, text="Tipos de messagebox",
         font=("Arial", 14, "bold"), fg="#1F4E79", bg="white").pack(pady=15)

def demo_info():
    messagebox.showinfo("Información", "Este es un mensaje informativo.")

def demo_warning():
    messagebox.showwarning("Advertencia", "Este es un mensaje de advertencia.")

def demo_error():
    messagebox.showerror("Error", "Este es un mensaje de error.")

def demo_yesno():
    respuesta = messagebox.askyesno("Sí o No", "¿Deseas continuar?")
    messagebox.showinfo("Respuesta", f"Respondiste: {'Sí' if respuesta else 'No'}")

def demo_okcancel():
    respuesta = messagebox.askokcancel("Confirmar", "¿Aceptas los términos?")
    messagebox.showinfo("Respuesta", f"Respondiste: {'OK' if respuesta else 'Cancelar'}")

for txt, color, cmd in [
    ("showinfo()",     "#2196F3", demo_info),
    ("showwarning()",  "#FF9800", demo_warning),
    ("showerror()",    "#f44336", demo_error),
    ("askyesno()",     "#4CAF50", demo_yesno),
    ("askokcancel()",  "#9C27B0", demo_okcancel),
]:
    tk.Button(root, text=txt, font=("Arial", 11, "bold"),
              bg=color, fg="white", width=20,
              command=cmd).pack(pady=5)

root.mainloop()
