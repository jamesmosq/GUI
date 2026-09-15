"""
controllers/main_controller.py
─────────────────────────────────
CONTROLADOR principal: crea la conexión a BD, la ventana principal y
un controlador por cada pestaña/entidad (Products, Customers, Employees).
"""

from tkinter import messagebox

from models.database import DatabaseConnector
from views.main_view import MainView
from controllers.product_controller import ProductController
from controllers.customer_controller import CustomerController
from controllers.employee_controller import EmployeeController


class MainController:

    def __init__(self, db_config: dict):
        self.db = DatabaseConnector(db_config)
        self.view = MainView()

        ok, err = self.db.connect()
        if not ok:
            messagebox.showerror("Error de Conexión",
                                  f"No se pudo conectar a la base de datos:\n{err}")
            self.view.destroy()
            raise SystemExit(1)

        self.product_controller  = ProductController(self.view.tab_products, self.db)
        self.customer_controller = CustomerController(self.view.tab_customers, self.db)
        self.employee_controller = EmployeeController(self.view.tab_employees, self.db)

        self.view.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.db.disconnect()
        self.view.destroy()

    def run(self):
        self.view.mainloop()
