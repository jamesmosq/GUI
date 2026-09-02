"""
07_navegacion_empleados.py
──────────────────────────
Navegación de empleados con botones Anterior / Siguiente
Tkinter + MySQL · GUI carpeta

Conceptos:
  - DatabaseConnector con SP DetalleEmpleados
  - Cargar todos los registros en memoria (self.rows)
  - Navegar con índice self.current_row
  - Crear campos Entry dinámicamente desde los headers del SP
  - Label de posición: "Registro X de Y"

Requiere: pip install mysql-connector-python
SP usado: DetalleEmpleados
"""

import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox

# ── Configuración de conexión ─────────────────────────────────────────────────
DB_CONFIG = {
    "host":     "localhost",
    "user":     "root",
    "password": "",          # ← tu contraseña de MySQL
    "database": "Northwind"
}


class DatabaseConnector:
    def __init__(self, config: dict):
        self.config     = config
        self.connection = None
        self.cursor     = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(**self.config)
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as e:
            messagebox.showerror("Error de conexión", str(e))

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def execute_stored_procedure(self, procedure_name):
        """Ejecuta un SP sin parámetros y retorna (headers, rows)."""
        try:
            self.cursor.callproc(procedure_name)
            for result in self.cursor.stored_results():
                rows = result.fetchall()
                if rows:
                    headers = [i[0] for i in result.description]
                    return headers, rows
            return None, None
        except mysql.connector.Error as e:
            messagebox.showerror("Error", str(e))
            return None, None


class EmployeeDetailsApp(tk.Tk):
    """App de navegación de empleados — Anterior / Siguiente."""

    def __init__(self, db_connector):
        super().__init__()
        self.db          = db_connector
        self.headers     = []
        self.rows        = []
        self.current_row = 0
        self.total_rows  = 0
        self.entries     = {}

        self.title("07 — Navegación de Empleados")
        self.geometry("700x520")
        self.resizable(False, False)

        self.crear_widgets()
        self.cargar_datos()

    def crear_widgets(self):
        tk.Label(self, text="Detalles de Empleados",
                 font=("Arial", 14, "bold"), fg="#1F4E79").pack(pady=10)

        # ── Barra de navegación ───────────────────────────────────────────────
        nav_frame = ttk.Frame(self)
        nav_frame.pack(pady=8)

        tk.Button(nav_frame, text="◀ Anterior",
                  font=("Arial", 11, "bold"), bg="#2196F3", fg="white",
                  width=12, command=self.anterior).pack(side=tk.LEFT, padx=8)

        self.lbl_posicion = tk.Label(nav_frame, text="— / —",
                                      font=("Arial", 11), width=14)
        self.lbl_posicion.pack(side=tk.LEFT)

        tk.Button(nav_frame, text="Siguiente ▶",
                  font=("Arial", 11, "bold"), bg="#2196F3", fg="white",
                  width=12, command=self.siguiente).pack(side=tk.LEFT, padx=8)

        # ── Frame de detalles (se llena dinámicamente) ────────────────────────
        self.details_frame = ttk.Frame(self, padding="15")
        self.details_frame.pack(pady=5, padx=20, fill=tk.BOTH, expand=True)

    def cargar_datos(self):
        """Ejecuta el SP y carga todos los registros en memoria."""
        headers, rows = self.db.execute_stored_procedure('DetalleEmpleados')
        if headers and rows:
            self.headers    = headers
            self.rows       = rows
            self.total_rows = len(rows)
            self.crear_campos()
            self.mostrar(0)
        else:
            messagebox.showinfo("Sin datos",
                                "No se encontraron empleados en la BD.")

    def crear_campos(self):
        """Crea Label + Entry por cada columna del SP."""
        for i, header in enumerate(self.headers):
            ttk.Label(self.details_frame, text=f"{header}:",
                      font=("Arial", 11)).grid(
                row=i, column=0, sticky=tk.W, padx=8, pady=5)
            e = ttk.Entry(self.details_frame, width=50,
                          font=("Arial", 11))
            e.grid(row=i, column=1, sticky=tk.W, padx=8, pady=5)
            self.entries[header] = e

    def mostrar(self, idx):
        """Muestra el empleado en la posición idx."""
        if not (0 <= idx < self.total_rows):
            return
        for header, val in zip(self.headers, self.rows[idx]):
            self.entries[header].delete(0, tk.END)
            self.entries[header].insert(0, str(val) if val else "")
        self.current_row = idx
        self.lbl_posicion.config(
            text=f"Registro {idx + 1} de {self.total_rows}")

    def siguiente(self):
        if self.current_row < self.total_rows - 1:
            self.mostrar(self.current_row + 1)
        else:
            messagebox.showinfo("Fin", "Ya estás en el último registro.")

    def anterior(self):
        if self.current_row > 0:
            self.mostrar(self.current_row - 1)
        else:
            messagebox.showinfo("Inicio", "Ya estás en el primer registro.")


# ── Punto de entrada ──────────────────────────────────────────────────────────
db  = DatabaseConnector(DB_CONFIG)
db.connect()

app = EmployeeDetailsApp(db)
app.protocol("WM_DELETE_WINDOW", lambda: [db.disconnect(), app.destroy()])
app.mainloop()
