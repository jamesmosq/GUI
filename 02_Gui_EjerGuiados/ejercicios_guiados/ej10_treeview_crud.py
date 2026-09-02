"""
ej10_treeview_crud.py
─────────────────────
Ejercicio 10 — ttk.Treeview + Formulario CRUD visual
POO Nivel 3 · Tkinter · Puerta de entrada a BD
"""
import tkinter as tk
from tkinter import ttk, messagebox

class AppTreeview(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ej10 — Gestión con Treeview")
        self.geometry("700x550")
        self.configure(bg="white")
        self.resizable(False, False)
        self.datos = []
        self.id_seleccionado = None
        self.crear_widgets()

    def crear_widgets(self):
        tk.Label(self, text="GESTIÓN DE EMPLEADOS",
                 font=("Arial", 14, "bold"), fg="#1F4E79", bg="white").pack(pady=15)

        form = tk.Frame(self, bg="white")
        form.pack(pady=5)
        campos = [("ID:", "eid"), ("Apellido:", "apellido"),
                  ("Nombre:", "nombre"), ("Notas:", "notas")]
        self.entries = {}
        for col, (lbl, key) in enumerate(campos):
            tk.Label(form, text=lbl, font=("Arial", 11),
                     bg="white").grid(row=0, column=col*2, padx=5)
            e = tk.Entry(form, width=12, font=("Arial", 11), relief="solid", bd=1)
            e.grid(row=0, column=col*2+1, padx=3)
            self.entries[key] = e

        fb = tk.Frame(self, bg="white")
        fb.pack(pady=10)
        for txt, color, cmd in [
            ("Agregar",    "#4CAF50", self.agregar),
            ("Actualizar", "#2196F3", self.actualizar),
            ("Eliminar",   "#f44336", self.eliminar),
            ("Limpiar",    "#FF9800", self.limpiar),
            ("Ver detalle","#9C27B0", self.ver_detalle),
        ]:
            tk.Button(fb, text=txt, font=("Arial", 10, "bold"),
                      bg=color, fg="white", width=10,
                      command=cmd).pack(side=tk.LEFT, padx=3)

        ft = tk.Frame(self)
        ft.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        cols = ("ID", "Apellido", "Nombre", "Notas")
        self.tree = ttk.Treeview(ft, columns=cols, show="headings", height=10)
        for col, w in zip(cols, [60, 150, 150, 250]):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=w, anchor="w")
        sy = ttk.Scrollbar(ft, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=sy.set)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        sy.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.bind("<<TreeviewSelect>>", self.cargar_seleccion)

    def refrescar_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for d in self.datos:
            self.tree.insert("", tk.END,
                values=(d["eid"], d["apellido"], d["nombre"], d["notas"]))

    def cargar_seleccion(self, event):
        sel = self.tree.selection()
        if not sel:
            return
        valores = self.tree.item(sel[0])["values"]
        for key, val in zip(["eid", "apellido", "nombre", "notas"], valores):
            self.entries[key].delete(0, tk.END)
            self.entries[key].insert(0, str(val))
        self.id_seleccionado = int(valores[0]) - 1

    def agregar(self):
        datos = {k: e.get().strip() for k, e in self.entries.items()}
        if not all([datos["apellido"], datos["nombre"]]):
            messagebox.showerror("Error", "Apellido y Nombre son obligatorios.")
            return
        datos["eid"] = len(self.datos) + 1
        self.datos.append(datos)
        self.refrescar_tree()
        self.limpiar(silencioso=True)
        messagebox.showinfo("Agregado",
            f"{datos['nombre']} {datos['apellido']} agregado (ID: {datos['eid']}).")

    def actualizar(self):
        if self.id_seleccionado is None:
            messagebox.showwarning("Advertencia", "Selecciona un registro del Treeview.")
            return
        datos = {k: e.get().strip() for k, e in self.entries.items()}
        if not all([datos["apellido"], datos["nombre"]]):
            messagebox.showerror("Error", "Apellido y Nombre son obligatorios.")
            return
        datos["eid"] = self.id_seleccionado + 1
        self.datos[self.id_seleccionado] = datos
        self.refrescar_tree()
        messagebox.showinfo("Actualizado", "Registro actualizado correctamente.")

    def eliminar(self):
        if self.id_seleccionado is None:
            messagebox.showwarning("Advertencia", "Selecciona un registro del Treeview.")
            return
        nombre = self.datos[self.id_seleccionado]["nombre"]
        if messagebox.askyesno("Eliminar", f"¿Eliminar a '{nombre}'?"):
            self.datos.pop(self.id_seleccionado)
            for i, d in enumerate(self.datos):
                d["eid"] = i + 1
            self.id_seleccionado = None
            self.refrescar_tree()
            self.limpiar(silencioso=True)
            messagebox.showinfo("Eliminado", f"'{nombre}' eliminado.")

    def ver_detalle(self):
        if self.id_seleccionado is None:
            messagebox.showwarning("Advertencia", "Selecciona un registro primero.")
            return
        d = self.datos[self.id_seleccionado]
        messagebox.showinfo("Detalle",
            f"ID:       {d['eid']}\nApellido: {d['apellido']}\n"
            f"Nombre:   {d['nombre']}\nNotas:    {d['notas']}")

    def limpiar(self, silencioso=False):
        for e in self.entries.values():
            e.delete(0, tk.END)
        self.id_seleccionado = None
        if not silencioso:
            messagebox.showinfo("Limpiar", "Formulario limpiado.")

AppTreeview().mainloop()
