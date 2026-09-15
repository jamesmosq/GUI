"""
controllers/customer_controller.py
─────────────────────────────────────
CONTROLADOR de Customers: valida la entrada, llama al CustomerModel y
actualiza la CustomerView con el resultado.
"""

from tkinter import messagebox

from models.customer_model import CustomerModel
from views.customer_view import CustomerView
from utils.validators import validate_required, validate_numeric

TREE_KEYS = ["CustomerID", "CustomerName", "ContactName", "Address",
             "City", "PostalCode", "Country"]


class CustomerController:

    def __init__(self, parent, db):
        self.model = CustomerModel(db)
        self.view = CustomerView(parent, self)
        self.view.pack(fill="both", expand=True)
        self.cargar_lista()

    def guardar(self):
        data = self.view.get_form_data()

        if not validate_required(data["CustomerName"]):
            messagebox.showerror("Validación", "CustomerName es obligatorio.")
            return

        success, result = self.model.insert(
            data["CustomerName"], data["ContactName"] or None,
            data["Address"] or None, data["City"] or None,
            data["PostalCode"] or None, data["Country"] or None)

        if success:
            messagebox.showinfo("Éxito", "Cliente guardado correctamente.")
            self.limpiar()
            self.cargar_lista()
        else:
            messagebox.showerror("Error", f"Error al guardar: {result}")

    def actualizar(self):
        data = self.view.get_form_data()

        ok, customer_id = validate_numeric(data["CustomerID"])
        if not ok or customer_id is None:
            messagebox.showerror("Error", "Ingresa un CustomerID válido.")
            return

        if not validate_required(data["CustomerName"]):
            messagebox.showerror("Validación", "CustomerName es obligatorio.")
            return

        success, result = self.model.update(
            customer_id, data["CustomerName"], data["ContactName"] or None,
            data["Address"] or None, data["City"] or None,
            data["PostalCode"] or None, data["Country"] or None)

        if success:
            messagebox.showinfo("Éxito", "Cliente actualizado.")
            self.cargar_lista()
        else:
            messagebox.showerror("Error", f"Error al actualizar: {result}")

    def eliminar(self):
        data = self.view.get_form_data()

        ok, customer_id = validate_numeric(data["CustomerID"])
        if not ok or customer_id is None:
            messagebox.showerror("Error", "Ingresa un CustomerID válido.")
            return

        if not messagebox.askyesno("Confirmar", "¿Eliminar este cliente?"):
            return

        success, result = self.model.delete(customer_id)
        if success:
            messagebox.showinfo("Éxito", "Cliente eliminado.")
            self.limpiar()
            self.cargar_lista()
        else:
            messagebox.showerror("Error", f"Error al eliminar: {result}")

    def buscar(self):
        data = self.view.get_form_data()

        ok, customer_id = validate_numeric(data["CustomerID"])
        if not ok or customer_id is None:
            messagebox.showerror("Error", "Ingresa un CustomerID válido.")
            return

        success, result = self.model.get_by_id(customer_id)
        if success and result:
            self.view.set_form_data(dict(zip(TREE_KEYS, result[0])))
        else:
            messagebox.showinfo("No encontrado", "Cliente no encontrado.")

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
