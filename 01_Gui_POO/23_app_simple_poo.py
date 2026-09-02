"""
23_app_simple_poo.py
────────────────────
App simple con POO — nombre y edad con Label de resultado
Tkinter intermedio · clase que recibe root

Patrón básico de POO:
  - Clase que recibe root
  - Métodos separados para cada acción
  - Label de resultado que se actualiza dinámicamente
"""

import tkinter as tk
from tkinter import messagebox


class AplicacionSimple:
    def __init__(self, root):
        self.root = root
        self.root.title("23 — App Simple (POO)")
        self.root.geometry("320x400")
        self.root.configure(bg="white")
        self.root.resizable(False, False)

        tk.Label(root, text="Formulario de Saludo",
                 font=("Arial", 14, "bold"), fg="#1F4E79", bg="white").pack(pady=15)

        tk.Label(root, text="Escribe tu nombre:",
                 font=("Arial", 11), bg="white").pack()
        self.entry_nombre = tk.Entry(root, width=28,
                                     font=("Arial", 11), relief="solid", bd=1)
        self.entry_nombre.pack(pady=8)

        tk.Label(root, text="Escribe tu edad:",
                 font=("Arial", 11), bg="white").pack()
        self.entry_edad = tk.Entry(root, width=28,
                                   font=("Arial", 11), relief="solid", bd=1)
        self.entry_edad.pack(pady=8)

        frame_btn = tk.Frame(root, bg="white")
        frame_btn.pack(pady=15)

        tk.Button(frame_btn, text="Saludar",
                  font=("Arial", 11, "bold"), bg="#4CAF50", fg="white",
                  width=12, command=self.saludar).pack(side=tk.LEFT, padx=5)

        tk.Button(frame_btn, text="Limpiar",
                  font=("Arial", 11, "bold"), bg="#FF9800", fg="white",
                  width=12, command=self.limpiar_campos).pack(side=tk.LEFT, padx=5)

        # Label que se actualiza dinámicamente (no usa messagebox)
        self.lbl_resultado = tk.Label(root, text="",
                                       font=("Arial", 12, "bold"),
                                       fg="#2E74B5", bg="white",
                                       wraplength=280)
        self.lbl_resultado.pack(pady=10)

    def saludar(self):
        nombre = self.entry_nombre.get().strip()
        edad   = self.entry_edad.get().strip()

        if not nombre or not edad:
            messagebox.showwarning("Atención", "Completa todos los campos.")
            return

        if not edad.isdigit():
            messagebox.showerror("Error", "La edad debe ser un número.")
            return

        self.lbl_resultado.config(
            text=f"¡Hola, {nombre}! Tienes {edad} años.")
        messagebox.showinfo("Saludo",
            f"¡Hola {nombre}!\nTienes {edad} años.")

    def limpiar_campos(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)
        self.lbl_resultado.config(text="")
        messagebox.showinfo("Limpiar", "Campos limpiados.")


if __name__ == "__main__":
    root = tk.Tk()
    app  = AplicacionSimple(root)
    root.mainloop()
