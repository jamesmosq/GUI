"""
models/customer_model.py
─────────────────────────
MODELO de Customers. Traduce operaciones de negocio a llamadas de
Stored Procedures (sp_InsertCustomer, sp_UpdateCustomer, sp_DeleteCustomer,
sp_GetCustomer, sp_GetAllCustomers).
"""

from models.database import DatabaseConnector


class CustomerModel:

    def __init__(self, db: DatabaseConnector):
        self.db = db

    def get_all(self):
        return self.db.call_procedure('sp_GetAllCustomers')

    def get_by_id(self, customer_id: int):
        return self.db.call_procedure('sp_GetCustomer', (customer_id,))

    def insert(self, name, contact_name, address, city, postal_code, country):
        return self.db.call_procedure(
            'sp_InsertCustomer',
            (name, contact_name, address, city, postal_code, country))

    def update(self, customer_id, name, contact_name, address, city, postal_code, country):
        return self.db.call_procedure(
            'sp_UpdateCustomer',
            (customer_id, name, contact_name, address, city, postal_code, country))

    def delete(self, customer_id: int):
        return self.db.call_procedure('sp_DeleteCustomer', (customer_id,))
