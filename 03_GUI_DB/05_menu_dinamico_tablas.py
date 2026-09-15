"""
05_menu_dinamico_tablas.py
──────────────────────────
Menú dinámico que abre formularios por tabla de la BD
Tkinter + MySQL · GUI carpeta

Conceptos:
  - Menu dinámico generado desde una lista
  - Toplevel: ventanas secundarias independientes
  - DESCRIBE <tabla>: obtener columnas de una tabla en MySQL
  - INSERT dinámico construido con f-strings + parámetros seguros (%s)

Nota pedagógica sobre SQL dinámico:
  El nombre de la tabla en DESCRIBE y en el INSERT viene de una lista
  controlada (tables = [...]) — NO de input del usuario.
  Esto evita SQL injection. Nunca pongas el input del usuario
  directamente en una consulta SQL.

Requiere: pip install mysql-connector-python
"""

import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# ── Configuración de conexión ─────────────────────────────────────────────────
DB_CONFIG = {
    "host":     "localhost",
    "user":     "root",
    "password": "base1234",          # ← tu contraseña de MySQL
    "database": "Northwind"
}

# Lista controlada de tablas — NUNCA uses input del usuario aquí
TABLES = ["Categories", "Customers", "Employees",
          "OrderDetails", "Orders", "Products", "Shippers", "Suppliers"]


class NorthwindGUI:
    """App con menú dinámico que genera formularios por tabla."""

    def __init__(self, master):
        self.master = master
        master.title("05 — Menú Dinámico por Tablas")
        master.geometry("700x420")
        master.resizable(False, False)

        self.db_config = DB_CONFIG
        self.crear_menu()
        self.crear_cuerpo()

    def crear_menu(self):
        """Crea la barra de menú con una opción por tabla de la BD."""
        menu_bar  = tk.Menu(self.master)
        self.master.config(menu=menu_bar)

        tabla_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Tablas", menu=tabla_menu)

        # Genera dinámicamente un comando por cada tabla
        for table in TABLES:
            tabla_menu.add_command(
                label=table,
                command=lambda t=table: self.abrir_ventana_tabla(t))

        menu_bar.add_command(label="Salir",
            command=lambda: self.master.destroy()
            if messagebox.askyesno("Salir", "¿Cerrar la aplicación?") else None)

    def crear_cuerpo(self):
        """Crea el contenido de la ventana principal."""
        frame = tk.Frame(self.master, bg="white")
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        tk.Label(frame,
                 text="Northwind Database Manager",
                 font=("Arial", 18, "bold"), fg="#1F4E79", bg="white").pack(pady=20)

        tk.Label(frame,
                 text="Selecciona una tabla desde el menú 'Tablas'\n"
                      "para abrir su formulario de inserción.",
                 font=("Arial", 12), fg="gray", bg="white",
                 justify="center").pack(pady=10)

        tk.Label(frame,
                 text=f"Tablas disponibles: {', '.join(TABLES)}",
                 font=("Arial", 10), fg="#2E74B5", bg="white",
                 wraplength=500).pack(pady=10)

    def _get_connection(self):
        return mysql.connector.connect(**self.db_config)

    def obtener_columnas(self, table_name):
        """
        Obtiene las columnas de una tabla usando DESCRIBE.
        table_name viene de la lista TABLES — no de input del usuario.
        """
        try:
            conn   = self._get_connection()
            cursor = conn.cursor()
            cursor.execute(f"DESCRIBE `{table_name}`")
            columnas = [col[0] for col in cursor.fetchall()]
            return columnas
        except mysql.connector.Error as e:
            messagebox.showerror("Error",
                f"No se pudo obtener la estructura de '{table_name}':\n{e}")
            return []
        finally:
            if conn.is_connected():
                cursor.close(); conn.close()

    def abrir_ventana_tabla(self, table_name):
        """Abre una ventana Toplevel con el formulario de la tabla."""
        ventana = tk.Toplevel(self.master)
        ventana.title(f"Insertar en {table_name}")
        ventana.geometry("580x420")
        ventana.resizable(False, False)
        ventana.grab_set()  # Bloquea la ventana principal mientras está abierta

        frame = tk.Frame(ventana, padx=15, pady=15)
        frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(frame, text=f"Tabla: {table_name}",
                 font=("Arial", 13, "bold"), fg="#1F4E79").grid(
            row=0, column=0, columnspan=2, pady=(0, 15))

        columnas = self.obtener_columnas(table_name)
        entries  = []

        for i, col in enumerate(columnas, start=1):
            tk.Label(frame, text=f"{col}:",
                     font=("Arial", 11), anchor="e", width=18).grid(
                row=i, column=0, sticky="e", padx=5, pady=6)
            e = tk.Entry(frame, width=35, font=("Arial", 11),
                         relief="solid", bd=1)
            e.grid(row=i, column=1, padx=5, pady=6)
            entries.append(e)

        frame_btn = tk.Frame(frame)
        frame_btn.grid(row=len(columnas)+1, column=0,
                       columnspan=2, pady=15)

        def insertar():
            valores = [e.get() for e in entries]
            # Construye la query con %s — parámetros seguros
            placeholders = ", ".join(["%s"] * len(columnas))
            cols_str     = ", ".join(columnas)
            query = f"INSERT INTO `{table_name}` ({cols_str}) VALUES ({placeholders})"
            try:
                conn   = self._get_connection()
                cursor = conn.cursor()
                cursor.execute(query, valores)
                conn.commit()
                messagebox.showinfo("Éxito", "Datos insertados correctamente.")
                for e in entries:
                    e.delete(0, tk.END)
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Error al insertar:\n{e}")
            finally:
                if conn.is_connected():
                    cursor.close(); conn.close()

        tk.Button(frame_btn, text="Insertar",
                  font=("Arial", 11, "bold"), bg="#4CAF50", fg="white",
                  width=12, command=insertar).pack(side=tk.LEFT, padx=5)

        tk.Button(frame_btn, text="Limpiar",
                  font=("Arial", 11, "bold"), bg="#FF9800", fg="white",
                  width=12,
                  command=lambda: [e.delete(0, tk.END) for e in entries]
                  ).pack(side=tk.LEFT, padx=5)

        tk.Button(frame_btn, text="Cerrar",
                  font=("Arial", 11, "bold"), bg="#f44336", fg="white",
                  width=12, command=ventana.destroy).pack(side=tk.LEFT, padx=5)


root = tk.Tk()
app  = NorthwindGUI(root)
root.mainloop()
