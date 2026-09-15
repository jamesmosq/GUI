"""
models/employee_model.py
─────────────────────────
MODELO de Employees. Traduce operaciones de negocio a llamadas de
Stored Procedures (sp_InsertEmployee, sp_UpdateEmployee, sp_DeleteEmployee,
sp_GetEmployee, sp_GetAllEmployees).
"""

from models.database import DatabaseConnector


class EmployeeModel:

    def __init__(self, db: DatabaseConnector):
        self.db = db

    def get_all(self):
        return self.db.call_procedure('sp_GetAllEmployees')

    def get_by_id(self, employee_id: int):
        return self.db.call_procedure('sp_GetEmployee', (employee_id,))

    def insert(self, last_name, first_name, birth_date, photo, notes):
        return self.db.call_procedure(
            'sp_InsertEmployee', (last_name, first_name, birth_date, photo, notes))

    def update(self, employee_id, last_name, first_name, birth_date, photo, notes):
        return self.db.call_procedure(
            'sp_UpdateEmployee',
            (employee_id, last_name, first_name, birth_date, photo, notes))

    def delete(self, employee_id: int):
        return self.db.call_procedure('sp_DeleteEmployee', (employee_id,))
