"""
20_treeview_notebook_poo.py
───────────────────────────
Treeview + Notebook con POO — clase que recibe root
Tkinter intermedio

Patrón: clase que RECIBE root (no hereda de tk.Tk)
  self.root = root
  self.notebook = ttk.Notebook(root)

Incluye: agregar elemento dinámicamente al Treeview.
"""

import tkinter as tk
from tkinter import ttk, messagebox


class AplicacionEjemplo:
    def __init__(self, root):
        self.root = root
        self.root.title("20 — Treeview + Notebook (POO)")
        self.root.geometry("620x430")
        self.root.resizable(False, False)

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill="both")

        # Pestaña 1: Treeview
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="  Datos  ")
        self.crear_treeview()

        # Pestaña 2: Botones
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="  Acciones  ")
        self.crear_botones()

    def crear_treeview(self):
        tk.Label(self.tab1, text="Lista de Usuarios",
                 font=("Arial", 12, "bold"), fg="#1F4E79").pack(pady=8)

        frame_tree = tk.Frame(self.tab1)
        frame_tree.pack(padx=15, fill=tk.BOTH, expand=True)

        cols = ("Nombre", "Edad", "Ciudad")
        self.tree = ttk.Treeview(frame_tree, columns=cols,
                                  show="headings", height=8)
        for col, w in zip(cols, [180, 80, 150]):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=w, anchor="w")

        sb = ttk.Scrollbar(frame_tree, orient=tk.VERTICAL,
                            command=self.tree.yview)
        self.tree.configure(yscrollcommand=sb.set)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        sb.pack(side=tk.RIGHT, fill=tk.Y)

        for row in [
            ("Ana García",      28, "Madrid"),
            ("Juan López",      35, "Barcelona"),
            ("María Rodríguez", 42, "Valencia"),
        ]:
            self.tree.insert("", tk.END, values=row)

        tk.Button(self.tab1, text="Ver detalle del seleccionado",
                  font=("Arial", 10, "bold"), bg="#2196F3", fg="white",
                  command=self.ver_detalle).pack(pady=8)

    def crear_botones(self):
        tk.Label(self.tab2, text="Agregar nuevo usuario",
                 font=("Arial", 12, "bold"), fg="#1F4E79").pack(pady=15)

        form = tk.Frame(self.tab2)
        form.pack()
        self.entries = {}
        for i, (lbl, key) in enumerate([("Nombre:", "nombre"),
                                          ("Edad:", "edad"),
                                          ("Ciudad:", "ciudad")]):
            tk.Label(form, text=lbl, font=("Arial", 11),
                     width=8, anchor="e").grid(row=i, column=0, pady=8, padx=5)
            e = tk.Entry(form, width=22, font=("Arial", 11),
                         relief="solid", bd=1)
            e.grid(row=i, column=1, pady=8)
            self.entries[key] = e

        frame_btn = tk.Frame(self.tab2)
        frame_btn.pack(pady=12)
        tk.Button(frame_btn, text="Agregar al Treeview",
                  font=("Arial", 10, "bold"), bg="#4CAF50", fg="white",
                  width=18, command=self.agregar_elemento).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Limpiar",
                  font=("Arial", 10, "bold"), bg="#FF9800", fg="white",
                  width=10, command=self.limpiar_form).pack(side=tk.LEFT, padx=5)

    def agregar_elemento(self):
        nombre = self.entries["nombre"].get().strip()
        edad   = self.entries["edad"].get().strip()
        ciudad = self.entries["ciudad"].get().strip()
        if not all([nombre, edad, ciudad]):
            messagebox.showerror("Error", "Completa todos los campos.")
            return
        self.tree.insert("", tk.END, values=(nombre, edad, ciudad))
        self.limpiar_form(silencioso=True)
        self.notebook.select(self.tab1)
        messagebox.showinfo("Agregado", f"'{nombre}' agregado a la tabla.")

    def ver_detalle(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Sin selección", "Selecciona una fila.")
            return
        v = self.tree.item(sel[0])["values"]
        messagebox.showinfo("Detalle",
            f"Nombre: {v[0]}\nEdad:   {v[1]}\nCiudad: {v[2]}")

    def limpiar_form(self, silencioso=False):
        for e in self.entries.values():
            e.delete(0, tk.END)
        if not silencioso:
            messagebox.showinfo("Limpiar", "Formulario limpiado.")

    def mostrar_mensaje(self, boton):
        messagebox.showinfo("Mensaje", f"Has presionado el {boton}")


if __name__ == "__main__":
    root = tk.Tk()
    app  = AplicacionEjemplo(root)
    root.mainloop()
