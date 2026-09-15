"""
controllers/employee_controller.py
─────────────────────────────────────
CONTROLADOR de Employees: valida la entrada, llama al EmployeeModel y
actualiza la EmployeeView con el resultado.
"""

from tkinter import messagebox

from models.employee_model import EmployeeModel
from views.employee_view import EmployeeView
from utils.validators import validate_required, validate_numeric, validate_date

TREE_KEYS = ["EmployeeID", "LastName", "FirstName", "BirthDate", "Photo", "Notes"]


def _format_date(value):
    return value.strftime("%Y-%m-%d") if hasattr(value, "strftime") else (value or "")


def _row_for_tree(row):
    employee_id, last_name, first_name, birth_date, photo, notes = row
    notes_short = (notes[:50] + "...") if notes and len(notes) > 50 else notes
    return (employee_id, last_name, first_name, _format_date(birth_date), photo, notes_short)


class EmployeeController:

    def __init__(self, parent, db):
        self.model = EmployeeModel(db)
        self.view = EmployeeView(parent, self)
        self.view.pack(fill="both", expand=True)
        self.cargar_lista()

    def guardar(self):
        data = self.view.get_form_data()

        if not validate_required(data["LastName"]):
            messagebox.showerror("Validación", "LastName es obligatorio.")
            return
        if not validate_required(data["FirstName"]):
            messagebox.showerror("Validación", "FirstName es obligatorio.")
            return

        ok, birth_date = validate_date(data["BirthDate"])
        if not ok:
            messagebox.showerror("Validación", "BirthDate debe tener formato YYYY-MM-DD.")
            return

        success, result = self.model.insert(
            data["LastName"], data["FirstName"], birth_date,
            data["Photo"] or None, data["Notes"] or None)

        if success:
            messagebox.showinfo("Éxito", "Empleado guardado correctamente.")
            self.limpiar()
            self.cargar_lista()
        else:
            messagebox.showerror("Error", f"Error al guardar: {result}")

    def actualizar(self):
        data = self.view.get_form_data()

        ok, employee_id = validate_numeric(data["EmployeeID"])
        if not ok or employee_id is None:
            messagebox.showerror("Error", "Ingresa un EmployeeID válido.")
            return

        if not validate_required(data["LastName"]):
            messagebox.showerror("Validación", "LastName es obligatorio.")
            return
        if not validate_required(data["FirstName"]):
            messagebox.showerror("Validación", "FirstName es obligatorio.")
            return

        ok, birth_date = validate_date(data["BirthDate"])
        if not ok:
            messagebox.showerror("Validación", "BirthDate debe tener formato YYYY-MM-DD.")
            return

        success, result = self.model.update(
            employee_id, data["LastName"], data["FirstName"], birth_date,
            data["Photo"] or None, data["Notes"] or None)

        if success:
            messagebox.showinfo("Éxito", "Empleado actualizado.")
            self.cargar_lista()
        else:
            messagebox.showerror("Error", f"Error al actualizar: {result}")

    def eliminar(self):
        data = self.view.get_form_data()

        ok, employee_id = validate_numeric(data["EmployeeID"])
        if not ok or employee_id is None:
            messagebox.showerror("Error", "Ingresa un EmployeeID válido.")
            return

        if not messagebox.askyesno("Confirmar", "¿Eliminar este empleado?"):
            return

        success, result = self.model.delete(employee_id)
        if success:
            messagebox.showinfo("Éxito", "Empleado eliminado.")
            self.limpiar()
            self.cargar_lista()
        else:
            messagebox.showerror("Error", f"Error al eliminar: {result}")

    def buscar(self):
        data = self.view.get_form_data()

        ok, employee_id = validate_numeric(data["EmployeeID"])
        if not ok or employee_id is None:
            messagebox.showerror("Error", "Ingresa un EmployeeID válido.")
            return

        success, result = self.model.get_by_id(employee_id)
        if success and result:
            employee_id, last_name, first_name, birth_date, photo, notes = result[0]
            self.view.set_form_data({
                "EmployeeID": employee_id, "LastName": last_name,
                "FirstName": first_name, "BirthDate": _format_date(birth_date),
                "Photo": photo, "Notes": notes,
            })
        else:
            messagebox.showinfo("No encontrado", "Empleado no encontrado.")

    def limpiar(self):
        self.view.clear_form()

    def cargar_lista(self):
        success, result = self.model.get_all()
        if success:
            self.view.set_tree_data(_row_for_tree(row) for row in result)
        else:
            messagebox.showerror("Error", f"No se pudo cargar la lista: {result}")

    def on_select(self, event):
        values = self.view.get_selected_tree_values()
        if values:
            self.view.set_form_data(dict(zip(TREE_KEYS, values)))
