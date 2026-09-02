"""
08_buscar_empleado_prettytable.py
──────────────────────────────────
Búsqueda de empleado por ID con PrettyTable en Text widget
Tkinter + MySQL · GUI carpeta

Conceptos:
  - PrettyTable: formatea resultados de BD como tabla de texto
  - Botones Conectar / Desconectar visibles en la UI
  - Text widget para mostrar resultados tabulados
  - La conexión se verifica antes de cada operación

Requiere: pip install mysql-connector-python prettytable
SP usado: GetEmployeeByID
"""

import mysql.connector
from mysql.connector import Error
from prettytable import PrettyTable
import tkinter as tk
from tkinter import messagebox

# ── Configuración de conexión ─────────────────────────────────────────────────
DB_CONFIG = {
    "host":     "localhost",
    "user":     "root",
    "password": "",          # ← tu contraseña de MySQL
    "database": "northwind"
}


class DatabaseConnector:
    def __init__(self, config: dict):
        self.config     = config
        self.connection = None
        self.cursor     = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(**self.config)
            self.cursor     = self.connection.cursor()
            return True
        except Error as e:
            messagebox.showerror("Error de conexión", str(e))
            return False

    def disconnect(self):
        """Cierra el cursor y la conexión limpiamente."""
        if self.cursor:     self.cursor.close()
        if self.connection: self.connection.close()
        self.connection = None
        self.cursor     = None

    def execute_stored_procedure(self, procedure_name, *args):
        """
        Ejecuta un SP y retorna los resultados como string PrettyTable.
        Si no hay conexión, intenta reconectar primero.
        """
        if not self.connection or not self.connection.is_connected():
            if not self.connect():
                return "No se pudo conectar a la base de datos."
        try:
            self.cursor.callproc(procedure_name, args)
            for result in self.cursor.stored_results():
                rows = result.fetchall()
                if rows:
                    headers = [i[0] for i in result.description]
                    tabla   = PrettyTable(headers)
                    tabla.align = "l"
                    for row in rows:
                        tabla.add_row(row)
                    return tabla.get_string()
            return "Sin resultados para ese ID."
        except Error as e:
            return f"Error al ejecutar el SP: {e}"


class App(tk.Tk):
    """App de búsqueda de empleados con PrettyTable."""

    def __init__(self, db_connector):
        super().__init__()
        self.db = db_connector
        self.title("08 — Buscar Empleado con PrettyTable")
        self.geometry("720x520")
        self.resizable(False, False)
        self.crear_widgets()
        # Conectar automáticamente al iniciar
        self._actualizar_estado(self.db.connect())

    def crear_widgets(self):
        tk.Label(self, text="Búsqueda de Empleados",
                 font=("Arial", 14, "bold"), fg="#1F4E79").pack(pady=12)

        # ── Fila de búsqueda ──────────────────────────────────────────────────
        frame_top = tk.Frame(self)
        frame_top.pack(pady=5)

        tk.Label(frame_top, text="Employee ID:",
                 font=("Arial", 12)).pack(side=tk.LEFT)
        self.entry_id = tk.Entry(frame_top, width=10,
                                  font=("Arial", 12), relief="solid", bd=1)
        self.entry_id.pack(side=tk.LEFT, padx=8)

        tk.Button(frame_top, text="Buscar",
                  font=("Arial", 11, "bold"), bg="#2196F3", fg="white",
                  width=10, command=self.buscar).pack(side=tk.LEFT, padx=5)

        tk.Button(frame_top, text="Limpiar",
                  font=("Arial", 11, "bold"), bg="#FF9800", fg="white",
                  width=10, command=self.limpiar).pack(side=tk.LEFT, padx=5)

        # ── Área de resultados ────────────────────────────────────────────────
        self.result_text = tk.Text(self, height=16, width=80,
                                    font=("Courier New", 10))
        self.result_text.pack(pady=10, padx=20)

        # ── Botones de conexión ───────────────────────────────────────────────
        frame_conn = tk.Frame(self)
        frame_conn.pack(pady=5)

        self.btn_conectar = tk.Button(
            frame_conn, text="Conectar",
            font=("Arial", 10, "bold"), bg="#4CAF50", fg="white",
            width=12, command=self.conectar)
        self.btn_conectar.pack(side=tk.LEFT, padx=5)

        self.btn_desconectar = tk.Button(
            frame_conn, text="Desconectar",
            font=("Arial", 10, "bold"), bg="#f44336", fg="white",
            width=12, command=self.desconectar)
        self.btn_desconectar.pack(side=tk.LEFT, padx=5)

        self.lbl_estado = tk.Label(frame_conn, text="Estado: —",
                                    font=("Arial", 10))
        self.lbl_estado.pack(side=tk.LEFT, padx=10)

    def buscar(self):
        eid = self.entry_id.get().strip()
        if not eid:
            messagebox.showwarning("Advertencia", "Ingresa un Employee ID.")
            return
        resultado = self.db.execute_stored_procedure('GetEmployeeByID', eid)
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, resultado)

    def limpiar(self):
        self.entry_id.delete(0, tk.END)
        self.result_text.delete("1.0", tk.END)
        messagebox.showinfo("Limpiar", "Pantalla limpiada.")

    def conectar(self):
        self._actualizar_estado(self.db.connect())
        if self.db.connection:
            messagebox.showinfo("Conexión", "Conexión establecida correctamente.")

    def desconectar(self):
        self.db.disconnect()
        self._actualizar_estado(False)
        messagebox.showinfo("Desconectado", "Conexión cerrada correctamente.")

    def _actualizar_estado(self, conectado: bool):
        if conectado:
            self.lbl_estado.config(text="Estado: ✔ Conectado", fg="#4CAF50")
            self.btn_conectar.config(state="disabled")
            self.btn_desconectar.config(state="normal")
        else:
            self.lbl_estado.config(text="Estado: ✗ Desconectado", fg="#f44336")
            self.btn_conectar.config(state="normal")
            self.btn_desconectar.config(state="disabled")


# ── Punto de entrada ──────────────────────────────────────────────────────────
db  = DatabaseConnector(DB_CONFIG)
app = App(db)
app.protocol("WM_DELETE_WINDOW", lambda: [db.disconnect(), app.destroy()])
app.mainloop()
