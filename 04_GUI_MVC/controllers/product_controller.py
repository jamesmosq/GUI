"""
controllers/product_controller.py
───────────────────────────────────
CONTROLADOR de Products: valida la entrada, llama al ProductModel y
actualiza la ProductView con el resultado. Es el único punto que conoce
tanto a la vista como al modelo.
"""

from tkinter import messagebox

from models.product_model import ProductModel
from views.product_view import ProductView
from utils.validators import validate_required, validate_numeric

TREE_KEYS = ["ProductID", "ProductName", "SupplierID", "CategoryID", "Unit", "Price"]


class ProductController:

    def __init__(self, parent, db):
        self.model = ProductModel(db)
        self.view = ProductView(parent, self)
        self.view.pack(fill="both", expand=True)
        self.cargar_lista()

    def guardar(self):
        data = self.view.get_form_data()

        if not validate_required(data["ProductName"]):
            messagebox.showerror("Validación", "ProductName es obligatorio.")
            return

        ok, supplier_id = validate_numeric(data["SupplierID"])
        if not ok:
            messagebox.showerror("Validación", "SupplierID debe ser un número.")
            return

        ok, category_id = validate_numeric(data["CategoryID"])
        if not ok:
            messagebox.showerror("Validación", "CategoryID debe ser un número.")
            return

        ok, price = validate_numeric(data["Price"])
        if not ok:
            messagebox.showerror("Validación", "Price debe ser un número.")
            return

        success, result = self.model.insert(
            data["ProductName"], supplier_id, category_id,
            data["Unit"] or None, price)

        if success:
            messagebox.showinfo("Éxito", "Producto guardado correctamente.")
            self.limpiar()
            self.cargar_lista()
        else:
            messagebox.showerror("Error", f"Error al guardar: {result}")

    def actualizar(self):
        data = self.view.get_form_data()

        ok, product_id = validate_numeric(data["ProductID"])
        if not ok or product_id is None:
            messagebox.showerror("Error", "Ingresa un ProductID válido.")
            return

        if not validate_required(data["ProductName"]):
            messagebox.showerror("Validación", "ProductName es obligatorio.")
            return

        ok, supplier_id = validate_numeric(data["SupplierID"])
        if not ok:
            messagebox.showerror("Validación", "SupplierID debe ser un número.")
            return

        ok, category_id = validate_numeric(data["CategoryID"])
        if not ok:
            messagebox.showerror("Validación", "CategoryID debe ser un número.")
            return

        ok, price = validate_numeric(data["Price"])
        if not ok:
            messagebox.showerror("Validación", "Price debe ser un número.")
            return

        success, result = self.model.update(
            product_id, data["ProductName"], supplier_id, category_id,
            data["Unit"] or None, price)

        if success:
            messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
            self.cargar_lista()
        else:
            messagebox.showerror("Error", f"Error al actualizar: {result}")

    def eliminar(self):
        data = self.view.get_form_data()

        ok, product_id = validate_numeric(data["ProductID"])
        if not ok or product_id is None:
            messagebox.showerror("Error", "Ingresa un ProductID válido.")
            return

        if not messagebox.askyesno("Confirmar", "¿Eliminar este producto?"):
            return

        success, result = self.model.delete(product_id)
        if success:
            messagebox.showinfo("Éxito", "Producto eliminado.")
            self.limpiar()
            self.cargar_lista()
        else:
            messagebox.showerror("Error", f"Error al eliminar: {result}")

    def buscar(self):
        data = self.view.get_form_data()

        ok, product_id = validate_numeric(data["ProductID"])
        if not ok or product_id is None:
            messagebox.showerror("Error", "Ingresa un ProductID válido.")
            return

        success, result = self.model.get_by_id(product_id)
        if success and result:
            self.view.set_form_data(dict(zip(TREE_KEYS, result[0])))
        else:
            messagebox.showinfo("No encontrado", "Producto no encontrado.")

    def limpiar(self):
        self.view.clear_form()

    def cargar_lista(self):
        success, result = self.model.get_all()
        if success:
            self.view.set_tree_data(result)
        else:
            messagebox.showerror("Error", f"No se pudo cargar la lista: {result}")

    def on_select(self, event):
        values = self.view.get_selected_tree_values()
        if values:
            self.view.set_form_data(dict(zip(TREE_KEYS, values)))
