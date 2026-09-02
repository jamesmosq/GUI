"""
ej09_notebook_poo.py
────────────────────
Ejercicio 9 — ttk.Notebook con clases por pestaña
POO Nivel 3 · Tkinter · Herencia de ttk.Frame
"""
import tkinter as tk
from tkinter import ttk, messagebox

class PestanaProductos(ttk.Frame):
    def __init__(self, padre):
        super().__init__(padre)
        self.crear_widgets()

    def crear_widgets(self):
        tk.Label(self, text="FORM PRODUCTS",
                 font=("Arial", 14, "bold"), fg="green").pack(pady=15)
        form = tk.Frame(self)
        form.pack(pady=10, padx=50, anchor="w")
        campos = [("ProductID:", "pid"), ("ProductName:", "pname"),
                  ("CategoryID:", "cat"), ("Price:", "price")]
        self.entries = {}
        for i, (lbl, key) in enumerate(campos):
            tk.Label(form, text=lbl, font=("Arial", 11),
                     width=12, anchor="e").grid(row=i, column=0, padx=5, pady=8)
            e = tk.Entry(form, width=25, font=("Arial", 11), relief="solid", bd=1)
            e.grid(row=i, column=1, pady=8)
            self.entries[key] = e
        fb = tk.Frame(self)
        fb.pack(pady=15)
        for txt, color, cmd in [
            ("Guardar",  "#4CAF50", self.guardar),
            ("Eliminar", "#f44336", self.eliminar),
            ("Limpiar",  "#FF9800", self.limpiar),
        ]:
            tk.Button(fb, text=txt, font=("Arial", 11, "bold"),
                      bg=color, fg="white", width=10,
                      command=cmd).pack(side=tk.LEFT, padx=5)

    def guardar(self):
        datos = {k: e.get().strip() for k, e in self.entries.items()}
        if not all(datos.values()):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        messagebox.showinfo("Guardar",
            f"Producto '{datos['pname']}' guardado.\nPrecio: ${datos['price']}")

    def eliminar(self):
        pid = self.entries["pid"].get().strip()
        if not pid:
            messagebox.showwarning("Advertencia", "Ingresa el ProductID.")
            return
        if messagebox.askyesno("Eliminar", f"¿Eliminar producto ID {pid}?"):
            messagebox.showinfo("Eliminado", "Producto eliminado.")
            self.limpiar(silencioso=True)

    def limpiar(self, silencioso=False):
        for e in self.entries.values():
            e.delete(0, tk.END)
        if not silencioso:
            messagebox.showinfo("Limpiar", "Formulario limpiado.")


class PestanaClientes(ttk.Frame):
    def __init__(self, padre):
        super().__init__(padre)
        self.crear_widgets()

    def crear_widgets(self):
        tk.Label(self, text="GESTIÓN DE CLIENTES",
                 font=("Arial", 14, "bold"), fg="#2196F3").pack(pady=15)
        form = tk.Frame(self)
        form.pack(pady=10, padx=50, anchor="w")
        campos = [("CustomerID:", "cid"), ("CustomerName:", "cname"),
                  ("ContactName:", "contact"), ("Address:", "addr")]
        self.entries = {}
        for i, (lbl, key) in enumerate(campos):
            tk.Label(form, text=lbl, font=("Arial", 11),
                     width=14, anchor="e").grid(row=i, column=0, padx=5, pady=8)
            e = tk.Entry(form, width=25, font=("Arial", 11), relief="solid", bd=1)
            e.grid(row=i, column=1, pady=8)
            self.entries[key] = e
        fb = tk.Frame(self)
        fb.pack(pady=15)
        for txt, color, cmd in [
            ("Guardar",    "#4CAF50", self.guardar),
            ("Actualizar", "#2196F3", self.actualizar),
            ("Limpiar",    "#FF9800", self.limpiar),
        ]:
            tk.Button(fb, text=txt, font=("Arial", 11, "bold"),
                      bg=color, fg="white", width=10,
                      command=cmd).pack(side=tk.LEFT, padx=5)

    def guardar(self):
        datos = {k: e.get().strip() for k, e in self.entries.items()}
        if not all(datos.values()):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        messagebox.showinfo("Guardar", f"Cliente '{datos['cname']}' guardado.")

    def actualizar(self):
        if not self.entries["cid"].get().strip():
            messagebox.showwarning("Advertencia", "Ingresa el CustomerID.")
            return
        messagebox.showinfo("Actualizar", "Cliente actualizado.")

    def limpiar(self, silencioso=False):
        for e in self.entries.values():
            e.delete(0, tk.END)
        if not silencioso:
            messagebox.showinfo("Limpiar", "Formulario limpiado.")


class AppNorthwind(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ej09 — Northwind POO con Pestañas")
        self.geometry("600x420")
        self.resizable(False, False)
        nb = ttk.Notebook(self)
        nb.add(PestanaProductos(nb), text="  Products  ")
        nb.add(PestanaClientes(nb),  text="  Customers ")
        nb.pack(expand=True, fill="both")

AppNorthwind().mainloop()
