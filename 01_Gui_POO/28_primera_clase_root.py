"""
28_primera_clase_root.py
────────────────────────
Primera clase que recibe root — patrón base de POO con Tkinter
Tkinter POO — nivel inicial

Patrón: la clase RECIBE root desde afuera.
  self.root = root
  self.root.title(...)
  Todos los widgets usan self.root o self como padre.

Este es el punto de entrada a la POO en Tkinter.
El siguiente paso (29) muestra funciones sueltas,
y el (32) muestra herencia directa de tk.Tk.
"""

import tkinter as tk
from tkinter import messagebox


class VentanaSimple:
    """Clase que encapsula la ventana y sus comportamientos."""

    def __init__(self, root):
        self.root = root
        self.root.title("28 — Primera Clase con Root")
        self.root.geometry("340x260")
        self.root.configure(bg="white")
        self.root.resizable(False, False)

        self.contador = 0  # Atributo de estado de la clase

        # Botón que muestra un mensaje
        self.btn_mensaje = tk.Button(
            root,
            text="Mostrar mensaje",
            font=("Arial", 11, "bold"),
            bg="#4CAF50", fg="white", width=20,
            command=self.mostrar_mensaje)
        self.btn_mensaje.pack(pady=15)

        # Botón que cambia su propio texto
        self.btn_cambiar = tk.Button(
            root,
            text="Clic para cambiar texto",
            font=("Arial", 11, "bold"),
            bg="#2196F3", fg="white", width=20,
            command=self.cambiar_texto)
        self.btn_cambiar.pack(pady=8)

        # Entry + botón para leer texto
        self.entrada = tk.Entry(root, width=26,
                                font=("Arial", 11), relief="solid", bd=1)
        self.entrada.pack(pady=8)

        tk.Button(root,
                  text="Leer texto",
                  font=("Arial", 11, "bold"),
                  bg="#FF9800", fg="white", width=20,
                  command=self.leer_texto).pack(pady=5)

        # Label de estado
        self.lbl_estado = tk.Label(root, text="",
                                    font=("Arial", 10), fg="gray", bg="white")
        self.lbl_estado.pack(pady=5)

    def mostrar_mensaje(self):
        """Se ejecuta al hacer clic en 'Mostrar mensaje'."""
        self.contador += 1
        self.lbl_estado.config(text=f"Presionaste el botón {self.contador} vez/veces")
        messagebox.showinfo("Mensaje",
            f"¡Hola! Has presionado el botón {self.contador} vez/veces.")

    def cambiar_texto(self):
        """Alterna el texto del botón entre dos opciones."""
        actual = self.btn_cambiar["text"]
        nuevo  = "Clic para cambiar texto" \
                 if actual == "¡Texto cambiado!" \
                 else "¡Texto cambiado!"
        self.btn_cambiar["text"] = nuevo

    def leer_texto(self):
        """Lee el contenido del Entry y lo muestra."""
        texto = self.entrada.get().strip()
        if not texto:
            messagebox.showwarning("Vacío", "El campo está vacío.")
            return
        messagebox.showinfo("Texto ingresado", f"Escribiste: {texto}")
        self.lbl_estado.config(text=f"Leído: '{texto}'")


# Punto de entrada: root se crea FUERA de la clase
root = tk.Tk()
app  = VentanaSimple(root)
root.mainloop()
