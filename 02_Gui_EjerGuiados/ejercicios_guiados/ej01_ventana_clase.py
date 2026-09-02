"""
ej01_ventana_clase.py
─────────────────────
Ejercicio 1 — Primera ventana con clase
POO Nivel 3 · Tkinter

Concepto: clase que RECIBE root como parámetro.
"""
import tkinter as tk
from tkinter import messagebox

class MiVentana:
    def __init__(self, root):
        self.root = root
        self.root.title("Ej01 — Primera ventana con clase")
        self.root.geometry("400x300")
        self.root.configure(bg="white")
        self.root.resizable(False, False)
        self.crear_widgets()

    def crear_widgets(self):
        self.titulo = tk.Label(self.root,
            text="¡Bienvenido a Tkinter con POO!",
            font=("Arial", 14, "bold"), fg="#1F4E79", bg="white")
        self.titulo.pack(pady=30)

        tk.Button(self.root, text="Saludar",
                  font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",
                  width=15, command=self.saludar).pack(pady=10)

        tk.Button(self.root, text="Salir",
                  font=("Arial", 12, "bold"), bg="#f44336", fg="white",
                  width=15, command=self.salir).pack(pady=10)

    def saludar(self):
        messagebox.showinfo("Saludo", "¡Hola! Este mensaje viene de un método de clase.")

    def salir(self):
        if messagebox.askyesno("Salir", "¿Deseas cerrar la aplicación?"):
            self.root.destroy()

root = tk.Tk()
app  = MiVentana(root)
root.mainloop()
