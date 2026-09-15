"""
models/product_model.py
────────────────────────
MODELO de Products. Traduce operaciones de negocio a llamadas de
Stored Procedures (sp_InsertProduct, sp_UpdateProduct, sp_DeleteProduct,
sp_GetProduct, sp_GetAllProducts).
"""

from models.database import DatabaseConnector


class ProductModel:

    def __init__(self, db: DatabaseConnector):
        self.db = db

    def get_all(self):
        return self.db.call_procedure('sp_GetAllProducts')

    def get_by_id(self, product_id: int):
        return self.db.call_procedure('sp_GetProduct', (product_id,))

    def insert(self, name, supplier_id, category_id, unit, price):
        return self.db.call_procedure(
            'sp_InsertProduct', (name, supplier_id, category_id, unit, price))

    def update(self, product_id, name, supplier_id, category_id, unit, price):
        return self.db.call_procedure(
            'sp_UpdateProduct',
            (product_id, name, supplier_id, category_id, unit, price))

    def delete(self, product_id: int):
        return self.db.call_procedure('sp_DeleteProduct', (product_id,))
