"""
views/main_view.py
────────────────────
VISTA principal: ventana raíz + Notebook con una pestaña por entidad.
Solo construye el "esqueleto" (root + tabs); cada controlador de entidad
instala su propia vista dentro de la pestaña correspondiente.
"""

import tkinter as tk
from tkinter import ttk


class MainView(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("04 — Northwind CRUD (MVC)")
        self.geometry('1200x700')
        self.resizable(True, True)

        self.notebook = ttk.Notebook(self)
        self.tab_products  = ttk.Frame(self.notebook)
        self.tab_customers = ttk.Frame(self.notebook)
        self.tab_employees = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_products,  text="  Products  ")
        self.notebook.add(self.tab_customers, text="  Customers ")
        self.notebook.add(self.tab_employees, text="  Employees ")
        self.notebook.pack(expand=True, fill="both")
