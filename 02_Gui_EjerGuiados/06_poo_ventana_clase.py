"""
06_poo_ventana_clase.py
───────────────────────
POO + Tkinter: clase que recibe root como parámetro
Nivel: introducción a POO con GUI

Patrón:
  • La clase RECIBE root desde afuera
  • self.root guarda la referencia a la ventana
  • Los widgets se crean en crear_widgets()
  • Los eventos son métodos de la clase

Basado en: 28.bo.py (versión mejorada)
"""

import tkinter as tk
from tkinter import messagebox


class VentanaSimple:
    """Clase que encapsula la ventana y sus comportamientos."""

    def __init__(self, root):
        self.root = root
        self.root.title("06 — POO: Ventana con Clase")
        self.root.geometry("360x280")
        self.root.configure(bg="white")
        self.root.resizable(False, False)

        self.contador = 0  # Atributo de estado

        self.crear_widgets()

    def crear_widgets(self):
        tk.Label(self.root,
                 text="Ventana con Clase POO",
                 font=("Arial", 14, "bold"),
                 fg="#1F4E79", bg="white").pack(pady=20)

        self.btn_mensaje = tk.Button(
            self.root, text="Mostrar mensaje",
            font=("Arial", 11, "bold"),
            bg="#4CAF50", fg="white", width=18,
            command=self.mostrar_mensaje)
        self.btn_mensaje.pack(pady=8)

        self.btn_cambiar = tk.Button(
            self.root, text="Clic para cambiar texto",
            font=("Arial", 11, "bold"),
            bg="#2196F3", fg="white", width=18,
            command=self.cambiar_texto)
        self.btn_cambiar.pack(pady=8)

        self.entrada = tk.Entry(
            self.root, width=28,
            font=("Arial", 11), relief="solid", bd=1)
        self.entrada.pack(pady=8)

        tk.Button(self.root, text="Leer texto",
                  font=("Arial", 11, "bold"),
                  bg="#FF9800", fg="white", width=18,
                  command=self.leer_texto).pack(pady=4)

    def mostrar_mensaje(self):
        self.contador += 1
        messagebox.showinfo("Mensaje",
            f"¡Hola! Has presionado este botón {self.contador} vez/veces.")

    def cambiar_texto(self):
        actual = self.btn_cambiar["text"]
        nuevo  = "¡Texto cambiado!" if actual == "Clic para cambiar texto" \
                 else "Clic para cambiar texto"
        self.btn_cambiar["text"] = nuevo

    def leer_texto(self):
        texto = self.entrada.get().strip()
        if not texto:
            messagebox.showwarning("Vacío", "El campo está vacío.")
            return
        messagebox.showinfo("Texto ingresado", f"Escribiste: {texto}")


root = tk.Tk()
app  = VentanaSimple(root)
root.mainloop()
