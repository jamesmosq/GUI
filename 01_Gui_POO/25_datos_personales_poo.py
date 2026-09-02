"""
25_datos_personales_poo.py
──────────────────────────
Formulario compacto de datos personales con LabelFrame y grid()
Tkinter intermedio · POO con clase que recibe root

Diferencia con 24: este es más pequeño y usa ttk.Entry + LabelFrame
con columnconfigure para que los campos se estiren correctamente.
Ideal como plantilla base para formularios simples.
"""

import tkinter as tk
from tkinter import ttk, messagebox


class AplicacionPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title("25 — Datos Personales (POO)")
        self.root.geometry("400x280")
        self.root.resizable(False, False)

        frame_principal = ttk.Frame(root, padding="20")
        frame_principal.pack(fill=tk.BOTH, expand=True)

        # LabelFrame con grid() interno
        frame_personal = ttk.LabelFrame(frame_principal,
                                         text="Datos Personales",
                                         padding="10")
        frame_personal.pack(fill=tk.X, pady=5)

        campos = [("Nombre:",   "nombre"),
                  ("Apellido:", "apellido"),
                  ("Edad:",     "edad")]
        self.entries = {}

        for i, (lbl, key) in enumerate(campos):
            ttk.Label(frame_personal, text=lbl).grid(
                row=i, column=0, sticky=tk.W, pady=6)
            e = ttk.Entry(frame_personal,
                          width=8 if key == "edad" else None)
            e.grid(row=i, column=1,
                   sticky=tk.W if key == "edad" else tk.EW,
                   padx=5, pady=6)
            self.entries[key] = e

        frame_personal.columnconfigure(1, weight=1)

        # Botones
        frame_btn = ttk.Frame(frame_principal)
        frame_btn.pack(fill=tk.X, pady=15)

        tk.Button(frame_btn, text="Guardar",
                  font=("Arial", 11, "bold"), bg="#4CAF50", fg="white",
                  width=12, command=self.guardar).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Limpiar",
                  font=("Arial", 11, "bold"), bg="#FF9800", fg="white",
                  width=12, command=self.limpiar).pack(side=tk.LEFT, padx=5)

    def guardar(self):
        nombre   = self.entries["nombre"].get().strip()
        apellido = self.entries["apellido"].get().strip()
        edad     = self.entries["edad"].get().strip()

        if not nombre or not apellido:
            messagebox.showerror("Error", "Nombre y Apellido son obligatorios.")
            return
        if edad and not edad.isdigit():
            messagebox.showerror("Error", "La edad debe ser un número.")
            return

        messagebox.showinfo("Guardado",
            f"Nombre: {nombre} {apellido}\n"
            f"Edad: {edad if edad else 'No indicada'}")

    def limpiar(self):
        for e in self.entries.values():
            e.delete(0, tk.END)
        messagebox.showinfo("Limpiar", "Formulario limpiado.")


if __name__ == "__main__":
    root = tk.Tk()
    app  = AplicacionPersonal(root)
    root.mainloop()
