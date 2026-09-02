"""
ej08_calculadora.py
───────────────────
Ejercicio 8 — Calculadora
POO Nivel 3 · Tkinter · Estado interno + lambda en botones
"""
import tkinter as tk
from tkinter import messagebox

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ej08 — Calculadora")
        self.geometry("320x420")
        self.configure(bg="#1E1E1E")
        self.resizable(False, False)
        self.expresion = ""
        self.crear_widgets()

    def crear_widgets(self):
        self.pantalla = tk.Label(self, text="0",
            font=("Arial", 24, "bold"), fg="white", bg="#2D2D2D",
            anchor="e", padx=15, width=18, relief="flat")
        self.pantalla.grid(row=0, column=0, columnspan=4, pady=(15, 5), padx=10)

        botones = [
            ("C",  1,0,"#E74C3C","white"), ("±", 1,1,"#555","white"),
            ("%",  1,2,"#555","white"),    ("/", 1,3,"#FF9800","white"),
            ("7",  2,0,"#3D3D3D","white"), ("8", 2,1,"#3D3D3D","white"),
            ("9",  2,2,"#3D3D3D","white"), ("×", 2,3,"#FF9800","white"),
            ("4",  3,0,"#3D3D3D","white"), ("5", 3,1,"#3D3D3D","white"),
            ("6",  3,2,"#3D3D3D","white"), ("-", 3,3,"#FF9800","white"),
            ("1",  4,0,"#3D3D3D","white"), ("2", 4,1,"#3D3D3D","white"),
            ("3",  4,2,"#3D3D3D","white"), ("+", 4,3,"#FF9800","white"),
            ("0",  5,0,"#3D3D3D","white"), (".", 5,1,"#3D3D3D","white"),
            ("⌫",  5,2,"#555","white"),    ("=", 5,3,"#4CAF50","white"),
        ]
        for texto, fila, col, bg, fg in botones:
            tk.Button(self, text=texto, font=("Arial", 16, "bold"),
                      bg=bg, fg=fg, width=5, height=2, relief="flat",
                      command=lambda t=texto: self.presionar(t)
                      ).grid(row=fila, column=col, padx=3, pady=3)

    def presionar(self, tecla):
        if tecla == "C":
            self.expresion = ""
            self.pantalla.config(text="0")
        elif tecla == "=":
            self.calcular()
        elif tecla == "⌫":
            self.expresion = self.expresion[:-1]
            self.pantalla.config(text=self.expresion or "0")
        elif tecla == "±":
            if self.expresion:
                self.expresion = self.expresion[1:] if self.expresion[0] == "-" \
                                 else "-" + self.expresion
            self.pantalla.config(text=self.expresion or "0")
        elif tecla == "%":
            try:
                self.expresion = str(float(self.expresion) / 100)
                self.pantalla.config(text=self.expresion)
            except:
                messagebox.showerror("Error", "Operación inválida.")
        elif tecla == "×":
            self.expresion += "*"
            self.pantalla.config(text=self.expresion)
        else:
            self.expresion += tecla
            self.pantalla.config(text=self.expresion)

    def calcular(self):
        try:
            resultado = eval(self.expresion)
            if resultado == int(resultado):
                self.pantalla.config(text=str(int(resultado)))
                self.expresion = str(int(resultado))
            else:
                self.pantalla.config(text=str(round(resultado, 8)))
                self.expresion = str(round(resultado, 8))
        except ZeroDivisionError:
            messagebox.showerror("Error", "No se puede dividir entre cero.")
            self.expresion = ""
            self.pantalla.config(text="0")
        except:
            messagebox.showerror("Error", "Expresión inválida.")
            self.expresion = ""
            self.pantalla.config(text="0")

Calculadora().mainloop()
