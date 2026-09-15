"""
config.py
─────────
Configuración de conexión a MySQL — misma BD que 03_GUI_DB (Northwindx),
creada por 03_GUI_DB/northwind_stored_procedures.sql.
"""

DB_CONFIG = {
    "host":       "localhost",
    "user":       "root",
    "password":   "base1234",          # ← tu contraseña de MySQL
    "database":   "Northwindx",
    "autocommit": False,
}
