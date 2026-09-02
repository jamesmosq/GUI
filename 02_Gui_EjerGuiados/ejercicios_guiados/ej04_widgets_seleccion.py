"""
ej04_widgets_seleccion.py
─────────────────────────
Ejercicio 4 — Checkbutton, Radiobutton, IntVar, StringVar
POO Nivel 3 · Tkinter
"""
import tkinter as tk
from tkinter import messagebox

class FormSeleccion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ej04 — Widgets de Selección")
        self.geometry("420x480")
        self.configure(bg="white")
        self.resizable(False, False)
        self.var_python = tk.IntVar()
        self.var_java   = tk.IntVar()
        self.var_js     = tk.IntVar()
        self.var_nivel  = tk.StringVar(value="Básico")
        self.crear_widgets()

    def crear_widgets(self):
        tk.Label(self, text="ENCUESTA DE PROGRAMACIÓN",
                 font=("Arial", 14, "bold"), fg="#1F4E79", bg="white").pack(pady=15)

        tk.Label(self, text="¿Qué lenguajes conoces?",
                 font=("Arial", 12, "bold"), bg="white", fg="#2E74B5").pack(anchor="w", padx=30)
        for texto, var in [("Python", self.var_python), ("Java", self.var_java), ("JavaScript", self.var_js)]:
            tk.Checkbutton(self, text=texto, variable=var,
                           font=("Arial", 11), bg="white").pack(anchor="w", padx=50)

        tk.Label(self, text="\n¿Cuál es tu nivel?",
                 font=("Arial", 12, "bold"), bg="white", fg="#2E74B5").pack(anchor="w", padx=30)
        for nivel in ["Básico", "Intermedio", "Avanzado"]:
            tk.Radiobutton(self, text=nivel, variable=self.var_nivel,
                           value=nivel, font=("Arial", 11), bg="white").pack(anchor="w", padx=50)

        frame_btn = tk.Frame(self, bg="white")
        frame_btn.pack(pady=20)
        tk.Button(frame_btn, text="Ver selección", font=("Arial", 12, "bold"),
                  bg="#4CAF50", fg="white", width=14,
                  command=self.ver_seleccion).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Limpiar", font=("Arial", 12, "bold"),
                  bg="#FF9800", fg="white", width=10,
                  command=self.limpiar).pack(side=tk.LEFT, padx=5)

    def ver_seleccion(self):
        lenguajes = [l for l, v in [("Python", self.var_python), ("Java", self.var_java),
                                     ("JavaScript", self.var_js)] if v.get()]
        if not lenguajes:
            messagebox.showwarning("Advertencia", "No seleccionaste ningún lenguaje.")
            return
        messagebox.showinfo("Tu selección",
            f"Lenguajes: {', '.join(lenguajes)}\nNivel: {self.var_nivel.get()}")

    def limpiar(self):
        for v in [self.var_python, self.var_java, self.var_js]:
            v.set(0)
        self.var_nivel.set("Básico")
        messagebox.showinfo("Limpiar", "Selección reiniciada.")

FormSeleccion().mainloop()
