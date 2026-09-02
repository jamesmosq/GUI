"""
ej02_herencia_tk.py
───────────────────
Ejercicio 2 — Herencia de tk.Tk
POO Nivel 3 · Tkinter

Concepto: la clase HEREDA de tk.Tk — ella misma ES la ventana.
"""
import tkinter as tk
from tkinter import messagebox

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ej02 — Herencia de tk.Tk")
        self.geometry("400x350")
        self.configure(bg="white")
        self.resizable(False, False)
        self.crear_widgets()

    def crear_widgets(self):
        tk.Label(self, text="Herencia de tk.Tk",
                 font=("Arial", 16, "bold"), fg="#1F4E79", bg="white").pack(pady=20)

        self.entrada = tk.Entry(self, width=30, font=("Arial", 12),
                                relief="solid", bd=1)
        self.entrada.pack(pady=10)

        self.lbl_resultado = tk.Label(self, text="", font=("Arial", 12),
                                      fg="#2E74B5", bg="white")
        self.lbl_resultado.pack(pady=10)

        for txt, color, cmd in [
            ("Mostrar texto", "#2196F3", self.mostrar_texto),
            ("Limpiar",       "#FF9800", self.limpiar),
            ("Salir",         "#f44336", self.cerrar),
        ]:
            tk.Button(self, text=txt, font=("Arial", 12, "bold"),
                      bg=color, fg="white", width=15,
                      command=cmd).pack(pady=6)

    def mostrar_texto(self):
        texto = self.entrada.get().strip()
        if not texto:
            messagebox.showwarning("Advertencia", "El campo está vacío.")
            return
        self.lbl_resultado.config(text=f"Escribiste: {texto}")
        messagebox.showinfo("Texto recibido", f"Recibí: {texto}")

    def limpiar(self):
        self.entrada.delete(0, tk.END)
        self.lbl_resultado.config(text="")
        messagebox.showinfo("Limpiar", "Campos limpiados correctamente.")

    def cerrar(self):
        if messagebox.askyesno("Salir", "¿Deseas cerrar la aplicación?"):
            self.destroy()

App().mainloop()
