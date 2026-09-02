"""
ej07_layout_grid.py
───────────────────
Ejercicio 7 — Layout profesional con grid()
POO Nivel 3 · Tkinter · Estilo Northwind
"""
import tkinter as tk
from tkinter import messagebox

class FormProducto(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ej07 — Layout con grid()")
        self.geometry("520x480")
        self.configure(bg="white")
        self.resizable(False, False)
        self.crear_widgets()

    def crear_widgets(self):
        tk.Label(self, text="FORMULARIO DE PRODUCTOS",
                 font=("Arial", 16, "bold"), fg="#4CAF50", bg="white").pack(pady=20)

        form_frame = tk.Frame(self, bg="white")
        form_frame.pack(pady=10, padx=50, anchor="w")

        campos = [("ProductID:", "product_id"), ("ProductName:", "product_name"),
                  ("SupplierID:", "supplier_id"), ("CategoryID:", "category_id"),
                  ("Unit:", "unit"), ("Price:", "price")]
        self.entries = {}

        for row, (label_text, key) in enumerate(campos):
            tk.Label(form_frame, text=label_text, font=("Arial", 12),
                     bg="white", anchor="e", width=14).grid(
                row=row, column=0, sticky="e", padx=(0, 10), pady=8)
            e = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
            e.grid(row=row, column=1, sticky="w", pady=8)
            self.entries[key] = e

        button_frame = tk.Frame(self, bg="white")
        button_frame.pack(pady=20)
        for txt, color, cmd in [
            ("Guardar",    "#4CAF50", self.guardar),
            ("Actualizar", "#2196F3", self.actualizar),
            ("Eliminar",   "#f44336", self.eliminar),
            ("Limpiar",    "#FF9800", self.limpiar),
        ]:
            tk.Button(button_frame, text=txt, font=("Arial", 12),
                      bg=color, fg="white", width=10,
                      command=cmd).pack(side=tk.LEFT, padx=5)

    def obtener_datos(self):
        return {k: e.get().strip() for k, e in self.entries.items()}

    def guardar(self):
        datos = self.obtener_datos()
        vacios = [k for k, v in datos.items() if not v]
        if vacios:
            messagebox.showerror("Error", f"Campos vacíos: {', '.join(vacios)}")
            return
        if not datos["price"].replace(".", "", 1).isdigit():
            messagebox.showerror("Error", "Price debe ser un valor numérico.")
            return
        messagebox.showinfo("Guardar",
            f"Producto '{datos['product_name']}' guardado.\nPrecio: ${datos['price']}")

    def actualizar(self):
        if not self.obtener_datos()["product_id"]:
            messagebox.showwarning("Advertencia", "Ingresa el ProductID para actualizar.")
            return
        messagebox.showinfo("Actualizar", "Producto actualizado correctamente.")

    def eliminar(self):
        pid = self.obtener_datos()["product_id"]
        if not pid:
            messagebox.showwarning("Advertencia", "Ingresa el ProductID para eliminar.")
            return
        if messagebox.askyesno("Eliminar", f"¿Eliminar producto ID {pid}?"):
            messagebox.showinfo("Eliminado", "Producto eliminado.")
            self.limpiar(silencioso=True)

    def limpiar(self, silencioso=False):
        for e in self.entries.values():
            e.delete(0, tk.END)
        if not silencioso:
            messagebox.showinfo("Limpiar", "Formulario limpiado.")

FormProducto().mainloop()
