"""
01_buscar_borrar_empleado.py
────────────────────────────
Buscar y borrar empleado por ID usando Stored Procedures
Tkinter + MySQL · GUI carpeta

Conceptos:
  - Clase DatabaseConnector con métodos de SP
  - simpledialog.askinteger() para pedir datos sin Entry
  - tabulate para mostrar resultados en messagebox
  - Separación: lógica BD vs lógica GUI

Requiere: pip install mysql-connector-python tabulate
SP usados: GetEmployeeByID, BorrarEmpleado
"""

import mysql.connector
import tkinter as tk
from tkinter import messagebox, simpledialog
from tabulate import tabulate

# ── Configuración de conexión ─────────────────────────────────────────────────
DB_CONFIG = {
    "host":     "localhost",
    "user":     "root",
    "password": "base1234",          # ← tu contraseña de MySQL
    "database": "Northwindx"
}


class DatabaseConnector:
    """Maneja la conexión y ejecución de Stored Procedures."""

    def __init__(self, config: dict):
        self.config     = config
        self.connection = None
        self.cursor     = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(**self.config)
            self.cursor = self.connection.cursor()
            messagebox.showinfo("Conexión", "Conexión establecida correctamente.")
        except mysql.connector.Error as e:
            messagebox.showerror("Error de conexión", str(e))

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def get_employee_by_id(self, employee_id):
        """Ejecuta SP GetEmployeeByID y retorna las filas."""
        try:
            self.cursor.callproc('GetEmployeeByID', [employee_id])
            for result in self.cursor.stored_results():
                rows = result.fetchall()
                return rows
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error al buscar empleado: {e}")
            return None

    def delete_employee(self, employee_id):
        """Ejecuta SP BorrarEmpleado y hace commit."""
        try:
            self.cursor.callproc('BorrarEmpleado', [employee_id])
            self.connection.commit()
            return True
        except mysql.connector.Error as e:
            self.connection.rollback()
            messagebox.showerror("Error", f"Error al borrar empleado: {e}")
            return False


# ── Lógica de la interfaz ─────────────────────────────────────────────────────
db = DatabaseConnector(DB_CONFIG)
db.connect()


def buscar_empleado():
    """Pide un ID y muestra los datos del empleado en un messagebox."""
    employee_id = simpledialog.askinteger("Buscar Empleado", "Ingrese el EmployeeID:")
    if not employee_id:
        return

    filas = db.get_employee_by_id(employee_id)
    if filas:
        headers = ["EmployeeID", "LastName", "FirstName", "BirthDate", "Photo", "Notes"]
        tabla   = tabulate(filas, headers=headers, tablefmt="pretty")
        messagebox.showinfo("Empleado encontrado", f"Datos del empleado:\n{tabla}")
    else:
        messagebox.showwarning("No encontrado", f"No existe empleado con ID {employee_id}.")


def borrar_empleado():
    """Pide un ID, confirma y borra el empleado."""
    employee_id = simpledialog.askinteger("Borrar Empleado", "Ingrese el EmployeeID a eliminar:")
    if not employee_id:
        return

    if not messagebox.askyesno("Confirmar", f"¿Eliminar al empleado ID {employee_id}?"):
        messagebox.showinfo("Cancelado", "Operación cancelada.")
        return

    if db.delete_employee(employee_id):
        messagebox.showinfo("Eliminado", f"Empleado ID {employee_id} eliminado correctamente.")
    else:
        messagebox.showerror("Error", "No se pudo eliminar el empleado.")


# ── Ventana principal ─────────────────────────────────────────────────────────
root = tk.Tk()
root.title("01 — Buscar y Borrar Empleado")
root.geometry("380x200")
root.configure(bg="white")
root.resizable(False, False)

tk.Label(root, text="Operaciones con Empleados",
         font=("Arial", 14, "bold"), fg="#1F4E79", bg="white").pack(pady=20)

frame_btn = tk.Frame(root, bg="white")
frame_btn.pack(pady=10)

tk.Button(frame_btn, text="Buscar Empleado",
          font=("Arial", 11, "bold"), bg="#2196F3", fg="white",
          width=18, command=buscar_empleado).pack(pady=8)

tk.Button(frame_btn, text="Borrar Empleado",
          font=("Arial", 11, "bold"), bg="#f44336", fg="white",
          width=18, command=borrar_empleado).pack(pady=8)

root.protocol("WM_DELETE_WINDOW", lambda: [db.disconnect(), root.destroy()])
root.mainloop()
