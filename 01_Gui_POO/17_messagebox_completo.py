"""
17_messagebox_completo.py
─────────────────────────
Módulo: messagebox — Todos los tipos de cuadros de diálogo
Tkinter intermedio

Tipos y sus valores de retorno:
  showinfo()       → None
  showwarning()    → None
  showerror()      → None
  askyesno()       → True / False
  askokcancel()    → True / False
  askyesnocancel() → True / False / None (cancelar)
  askretrycancel() → True / False
  askquestion()    → 'yes' / 'no'
"""

import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("17 — messagebox completo")
root.geometry("400x440")
root.configure(bg="white")
root.resizable(False, False)

tk.Label(root, text="Todos los tipos de messagebox",
         font=("Arial", 13, "bold"), fg="#1F4E79", bg="white").pack(pady=12)

lbl_resultado = tk.Label(root, text="Resultado: —",
                          font=("Arial", 11), fg="#2E74B5", bg="white")
lbl_resultado.pack(pady=5)

def mostrar(tipo):
    r = None
    if tipo == "info":
        messagebox.showinfo("Información", "Este es un mensaje informativo.")
    elif tipo == "warning":
        messagebox.showwarning("Advertencia", "Este es un mensaje de advertencia.")
    elif tipo == "error":
        messagebox.showerror("Error", "Este es un mensaje de error.")
    elif tipo == "yesno":
        r = messagebox.askyesno("Sí o No", "¿Deseas guardar los cambios?")
        lbl_resultado.config(text=f"askyesno → {r}")
        return
    elif tipo == "okcancel":
        r = messagebox.askokcancel("OK/Cancelar", "¿Continuar la operación?")
        lbl_resultado.config(text=f"askokcancel → {r}")
        return
    elif tipo == "yesnocancel":
        r = messagebox.askyesnocancel("Sí/No/Cancelar", "¿Guardar antes de salir?")
        lbl_resultado.config(text=f"askyesnocancel → {r}")
        return
    elif tipo == "retrycancel":
        r = messagebox.askretrycancel("Reintentar", "Falló la operación. ¿Reintentar?")
        lbl_resultado.config(text=f"askretrycancel → {r}")
        return
    lbl_resultado.config(text=f"{tipo} → sin retorno")

for txt, color, tipo in [
    ("showinfo()",        "#2196F3", "info"),
    ("showwarning()",     "#FF9800", "warning"),
    ("showerror()",       "#f44336", "error"),
    ("askyesno()",        "#4CAF50", "yesno"),
    ("askokcancel()",     "#9C27B0", "okcancel"),
    ("askyesnocancel()",  "#795548", "yesnocancel"),
    ("askretrycancel()",  "#607D8B", "retrycancel"),
]:
    tk.Button(root, text=txt, font=("Arial", 10, "bold"),
              bg=color, fg="white", width=22,
              command=lambda t=tipo: mostrar(t)).pack(pady=3)

root.mainloop()
