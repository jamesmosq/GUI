"""
ej03_formulario_validacion.py
─────────────────────────────
Ejercicio 3 — Formulario con validación
POO Nivel 3 · Tkinter

Conceptos: diccionario de entries, método validar(), messagebox.showerror.
"""
import tkinter as tk
from tkinter import messagebox

class FormularioRegistro(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ej03 — Formulario con Validación")
        self.geometry("420x480")
        self.configure(bg="white")
        self.resizable(False, False)
        self.crear_widgets()

    def crear_widgets(self):
        tk.Label(self, text="FORMULARIO DE REGISTRO",
                 font=("Arial", 16, "bold"), fg="#1F4E79", bg="white").pack(pady=20)

        campos = [("Nombre:", "nombre"), ("Apellido:", "apellido"),
                  ("Edad:",   "edad"),   ("Email:",   "email")]
        self.entries = {}

        for label_text, key in campos:
            frame = tk.Frame(self, bg="white")
            frame.pack(pady=5)
            tk.Label(frame, text=label_text, font=("Arial", 12),
                     bg="white", width=10, anchor="w").pack(side=tk.LEFT)
            e = tk.Entry(frame, width=25, font=("Arial", 12), relief="solid", bd=1)
            e.pack(side=tk.LEFT, padx=5)
            self.entries[key] = e

        frame_btn = tk.Frame(self, bg="white")
        frame_btn.pack(pady=20)
        for txt, color, cmd in [
            ("Guardar", "#4CAF50", self.guardar),
            ("Limpiar", "#FF9800", self.limpiar),
            ("Salir",   "#f44336", self.cerrar),
        ]:
            tk.Button(frame_btn, text=txt, font=("Arial", 12, "bold"),
                      bg=color, fg="white", width=10,
                      command=cmd).pack(side=tk.LEFT, padx=5)

    def validar(self):
        datos = {k: v.get().strip() for k, v in self.entries.items()}
        if not all(datos.values()):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return False
        if not datos["edad"].isdigit():
            messagebox.showerror("Error", "La edad debe ser un número entero.")
            return False
        if not (1 <= int(datos["edad"]) <= 120):
            messagebox.showerror("Error", "La edad debe estar entre 1 y 120.")
            return False
        if "@" not in datos["email"] or "." not in datos["email"]:
            messagebox.showerror("Error", "El email no tiene un formato válido.")
            return False
        return True

    def guardar(self):
        if not self.validar():
            return
        d = {k: v.get().strip() for k, v in self.entries.items()}
        messagebox.showinfo("Éxito",
            f"Datos guardados:\nNombre: {d['nombre']} {d['apellido']}\n"
            f"Edad: {d['edad']} años\nEmail: {d['email']}")
        self.limpiar(silencioso=True)

    def limpiar(self, silencioso=False):
        for e in self.entries.values():
            e.delete(0, tk.END)
        if not silencioso:
            messagebox.showinfo("Limpiar", "Campos limpiados.")

    def cerrar(self):
        if messagebox.askyesno("Salir", "¿Deseas cerrar?"):
            self.destroy()

FormularioRegistro().mainloop()
