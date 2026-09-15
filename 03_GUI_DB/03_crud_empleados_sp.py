"""
03_crud_empleados_sp.py
───────────────────────
CRUD de Empleados usando Stored Procedures + tkcalendar
Tkinter + MySQL · GUI carpeta

Conceptos:
  - DatabaseConnector reutilizable con execute_procedure()
  - DateEntry (tkcalendar) para seleccionar fechas visualmente
  - tabulate para mostrar resultados en Text widget
  - CRUD completo: Buscar, Insertar, Actualizar, Borrar, Mostrar Todos

Requiere: pip install mysql-connector-python tabulate tkcalendar
SP usados: sp_GetEmployee, sp_InsertEmployee, sp_UpdateEmployee,
           sp_DeleteEmployee, sp_GetAllEmployees
"""

import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox
from tabulate import tabulate
from tkcalendar import DateEntry

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

    def execute_procedure(self, procedure_name, *args):
        """
        Ejecuta un SP con los argumentos dados.
        Retorna lista de (headers, rows) o None si hay error.
        """
        try:
            self.cursor.callproc(procedure_name, args)
            results = []
            for result in self.cursor.stored_results():
                rows = result.fetchall()
                if rows:
                    headers = [i[0] for i in result.description]
                    results.append((headers, rows))
            self.connection.commit()
            return results
        except mysql.connector.Error as e:
            self.connection.rollback()
            messagebox.showerror("Error", f"Error en '{procedure_name}':\n{e}")
            return None


class EmployeeApp(tk.Tk):
    """App CRUD de empleados con SP y DateEntry para fechas."""

    def __init__(self, db_connector):
        super().__init__()
        self.db = db_connector
        self.title("03 — CRUD Empleados con SP")
        self.geometry("820x620")
        self.resizable(False, False)
        self.crear_widgets()

    def crear_widgets(self):
        tk.Label(self, text="GESTIÓN DE EMPLEADOS",
                 font=("Arial", 14, "bold"), fg="#1F4E79").pack(pady=10)

        # ── Formulario ────────────────────────────────────────────────────────
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        self.fields = ['EmployeeID', 'LastName', 'FirstName',
                       'BirthDate', 'Photo', 'Notes']
        self.entries = {}

        for i, field in enumerate(self.fields):
            ttk.Label(main_frame, text=f"{field}:").grid(
                row=i, column=0, sticky=tk.W, padx=5, pady=4)

            if field == 'BirthDate':
                # DateEntry: selector de fecha visual
                entry = DateEntry(main_frame, width=14,
                                  background='darkblue', foreground='white',
                                  borderwidth=2, date_pattern='yyyy-mm-dd')
            else:
                entry = ttk.Entry(main_frame, width=50)

            entry.grid(row=i, column=1, sticky=tk.W, padx=5, pady=4)
            self.entries[field] = entry

        # ── Botones ───────────────────────────────────────────────────────────
        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(row=len(self.fields), column=0,
                       columnspan=2, pady=12)

        for txt, color, cmd in [
            ("Buscar",       "#FF9800", self.buscar),
            ("Insertar",     "#4CAF50", self.insertar),
            ("Actualizar",   "#2196F3", self.actualizar),
            ("Borrar",       "#f44336", self.borrar),
            ("Mostrar todos","#9C27B0", self.mostrar_todos),
            ("Limpiar",      "#607D8B", self.limpiar),
        ]:
            tk.Button(btn_frame, text=txt, font=("Arial", 9, "bold"),
                      bg=color, fg="white", width=11,
                      command=cmd).pack(side=tk.LEFT, padx=3)

        # ── Área de resultados ────────────────────────────────────────────────
        self.result_text = tk.Text(main_frame, height=16, width=90,
                                   font=("Courier New", 9))
        self.result_text.grid(row=len(self.fields)+1, column=0,
                               columnspan=2, pady=8)

    def buscar(self):
        eid = self.entries['EmployeeID'].get().strip()
        if not eid:
            messagebox.showwarning("Advertencia", "Ingresa un EmployeeID.")
            return
        results = self.db.execute_procedure('sp_GetEmployee', eid)
        if results:
            self.mostrar_en_text(results)
        else:
            messagebox.showinfo("No encontrado", "Empleado no encontrado.")

    def insertar(self):
        # Se excluye EmployeeID (lo asigna la BD automáticamente)
        values = [self.entries[f].get() for f in self.fields[1:]]
        if not values[0] or not values[1]:
            messagebox.showerror("Error", "LastName y FirstName son obligatorios.")
            return
        results = self.db.execute_procedure('sp_InsertEmployee', *values)
        if results is not None:
            messagebox.showinfo("Éxito", "Empleado insertado correctamente.")
            self.limpiar(silencioso=True)
            self.mostrar_todos()

    def actualizar(self):
        values = [self.entries[f].get() for f in self.fields]
        if not values[0]:
            messagebox.showwarning("Advertencia", "Ingresa el EmployeeID a actualizar.")
            return
        results = self.db.execute_procedure('sp_UpdateEmployee', *values)
        if results is not None:
            messagebox.showinfo("Éxito", "Empleado actualizado correctamente.")
            self.mostrar_todos()

    def borrar(self):
        eid = self.entries['EmployeeID'].get().strip()
        if not eid:
            messagebox.showwarning("Advertencia", "Ingresa el EmployeeID a borrar.")
            return
        if not messagebox.askyesno("Confirmar", f"¿Eliminar empleado ID {eid}?"):
            return
        results = self.db.execute_procedure('sp_DeleteEmployee', eid)
        if results is not None:
            messagebox.showinfo("Éxito", "Empleado eliminado correctamente.")
            self.limpiar(silencioso=True)
            self.mostrar_todos()

    def mostrar_todos(self):
        results = self.db.execute_procedure('sp_GetAllEmployees')
        if results:
            self.mostrar_en_text(results)
        else:
            messagebox.showinfo("Sin datos", "No hay empleados registrados.")

    def limpiar(self, silencioso=False):
        for entry in self.entries.values():
            if hasattr(entry, 'delete'):
                entry.delete(0, tk.END)
        self.result_text.delete("1.0", tk.END)
        if not silencioso:
            messagebox.showinfo("Limpiar", "Campos limpiados correctamente.")

    def mostrar_en_text(self, results):
        """Muestra los resultados del SP en el Text widget usando tabulate."""
        self.result_text.delete("1.0", tk.END)
        for headers, rows in results:
            tabla = tabulate(rows, headers=headers, tablefmt="grid")
            self.result_text.insert(tk.END, tabla + "\n\n")


# ── Punto de entrada ──────────────────────────────────────────────────────────
db = DatabaseConnector(DB_CONFIG)
db.connect()

app = EmployeeApp(db)
app.protocol("WM_DELETE_WINDOW", lambda: [db.disconnect(), app.destroy()])
app.mainloop()
