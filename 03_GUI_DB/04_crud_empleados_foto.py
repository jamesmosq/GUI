"""
04_crud_empleados_foto.py
─────────────────────────
CRUD de Empleados con foto usando PIL y Treeview
Tkinter + MySQL · GUI carpeta

Conceptos nuevos respecto a 03:
  - PIL (Pillow) para cargar y mostrar imágenes en Tkinter
  - filedialog.askopenfilename() para seleccionar imagen
  - shutil.copy() para copiar imagen a carpeta local img/
  - Treeview para mostrar la lista de empleados
  - tree.bind("<<TreeviewSelect>>") para cargar fila seleccionada

Requiere: pip install mysql-connector-python pillow
Nota: usa SQL directo (no SPs) para mostrar contraste pedagógico
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import mysql.connector
import os
import shutil
from PIL import Image, ImageTk

# ── Configuración de conexión ─────────────────────────────────────────────────
DB_CONFIG = {
    "host":     "localhost",
    "user":     "root",
    "password": "",          # ← tu contraseña de MySQL
    "database": "northwind"
}


class EmployeeGUI:
    """CRUD de empleados con foto — clase que recibe master (root)."""

    def __init__(self, master):
        self.master = master
        master.title("04 — CRUD Empleados con Foto")
        master.geometry("900x650")
        master.resizable(True, True)

        self.image_path = ""    # ruta de la imagen seleccionada
        self.crear_widgets()
        self.cargar_empleados()

    def crear_widgets(self):
        main_frame = tk.Frame(self.master, padx=10, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # ── Panel de información ──────────────────────────────────────────────
        info_frame = tk.LabelFrame(main_frame, text="Información del Empleado",
                                    padx=10, pady=10)
        info_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        labels = ["ID:", "Apellido:", "Nombre:",
                  "Fecha de Nacimiento (YYYY-MM-DD):", "Notas:"]
        self.entries = []

        for i, label in enumerate(labels):
            tk.Label(info_frame, text=label,
                     font=("Arial", 11)).grid(
                row=i, column=0, sticky="e", padx=5, pady=6)
            e = tk.Entry(info_frame, width=30, font=("Arial", 11),
                         relief="solid", bd=1)
            e.grid(row=i, column=1, padx=5, pady=6, sticky="ew")
            self.entries.append(e)

        tk.Button(info_frame, text="Buscar por ID",
                  font=("Arial", 10, "bold"), bg="#FF9800", fg="white",
                  command=self.buscar_por_id).grid(
            row=len(labels), column=0, columnspan=2, pady=10, sticky="ew")

        # ── Panel de foto ─────────────────────────────────────────────────────
        photo_frame = tk.LabelFrame(main_frame, text="Foto del Empleado",
                                     padx=10, pady=10)
        photo_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        tk.Button(photo_frame, text="Seleccionar Foto",
                  font=("Arial", 10, "bold"), bg="#2196F3", fg="white",
                  command=self.seleccionar_imagen).pack(pady=5)

        self.image_label = tk.Label(photo_frame, text="Sin imagen",
                                     width=15, height=8,
                                     relief="solid", bd=1)
        self.image_label.pack(pady=5)

        # ── Botones CRUD ──────────────────────────────────────────────────────
        btn_frame = tk.Frame(main_frame)
        btn_frame.grid(row=1, column=0, columnspan=2, pady=10)

        for txt, color, cmd in [
            ("Crear",     "#4CAF50", self.crear_empleado),
            ("Leer",      "#2196F3", self.leer_empleado),
            ("Actualizar","#FF9800", self.actualizar_empleado),
            ("Eliminar",  "#f44336", self.eliminar_empleado),
            ("Limpiar",   "#607D8B", self.limpiar_campos),
        ]:
            tk.Button(btn_frame, text=txt,
                      font=("Arial", 11, "bold"),
                      bg=color, fg="white", width=11,
                      command=cmd).pack(side=tk.LEFT, padx=5)

        # ── Treeview ──────────────────────────────────────────────────────────
        tree_frame = tk.Frame(main_frame)
        tree_frame.grid(row=2, column=0, columnspan=2,
                        sticky="nsew", pady=10)

        cols = ("ID", "Apellido", "Nombre", "Fecha Nac.", "Foto", "Notas")
        self.tree = ttk.Treeview(tree_frame, columns=cols,
                                  show="headings", height=8)
        for col, w in zip(cols, [50, 120, 120, 110, 100, 200]):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=w, anchor="w")

        # Scrollbar correctamente posicionada
        sb = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL,
                            command=self.tree.yview)
        self.tree.configure(yscrollcommand=sb.set)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        sb.pack(side=tk.RIGHT, fill=tk.Y)

        # Al seleccionar fila, carga datos en el formulario
        self.tree.bind("<<TreeviewSelect>>", self.leer_empleado)

        # Configurar expansión
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)

    def _get_connection(self):
        """Crea y retorna una nueva conexión MySQL."""
        return mysql.connector.connect(**DB_CONFIG)

    def buscar_por_id(self):
        eid = self.entries[0].get().strip()
        if not eid:
            messagebox.showwarning("Advertencia", "Ingresa un ID para buscar.")
            return
        try:
            conn   = self._get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Employees WHERE EmployeeID = %s", (eid,))
            emp = cursor.fetchone()
            if emp:
                self.poblar_campos(emp)
            else:
                messagebox.showinfo("No encontrado",
                                    f"No existe empleado con ID {eid}.")
        except mysql.connector.Error as e:
            messagebox.showerror("Error", str(e))
        finally:
            if conn.is_connected():
                cursor.close(); conn.close()

    def poblar_campos(self, emp):
        """Llena el formulario con los datos de un empleado."""
        valores = [emp[0], emp[1], emp[2],
                   emp[3].strftime('%Y-%m-%d') if emp[3] else '', emp[5]]
        for entry, val in zip(self.entries, valores):
            entry.delete(0, tk.END)
            entry.insert(0, str(val) if val else "")

        # Mostrar imagen si existe
        self.image_path = emp[4] or ""
        if self.image_path and os.path.exists(self.image_path):
            self._mostrar_imagen(self.image_path)
        else:
            self.image_label.config(image="", text="Sin imagen")

    def _mostrar_imagen(self, ruta):
        """Carga y muestra una imagen en el Label de foto."""
        try:
            img   = Image.open(ruta)
            img.thumbnail((120, 120))
            photo = ImageTk.PhotoImage(img)
            self.image_label.config(image=photo, text="")
            self.image_label.image = photo  # referencia para evitar GC
        except Exception as e:
            messagebox.showwarning("Imagen", f"No se pudo cargar la imagen:\n{e}")
            self.image_label.config(image="", text="Error imagen")

    def seleccionar_imagen(self):
        ruta = filedialog.askopenfilename(
            filetypes=[("Imágenes", "*.jpg *.jpeg *.png *.gif *.bmp")])
        if ruta:
            self.image_path = ruta
            self._mostrar_imagen(ruta)

    def _copiar_imagen(self):
        """Copia la imagen seleccionada a la carpeta img/ local."""
        if not self.image_path:
            return None
        os.makedirs("img", exist_ok=True)
        nombre   = os.path.basename(self.image_path)
        destino  = os.path.join("img", nombre)
        shutil.copy(self.image_path, destino)
        return destino

    def crear_empleado(self):
        _, apellido, nombre, fecha, notas = [e.get().strip() for e in self.entries]
        if not apellido or not nombre:
            messagebox.showerror("Error", "Apellido y Nombre son obligatorios.")
            return
        if not self.image_path:
            messagebox.showwarning("Advertencia", "Selecciona una foto.")
            return
        ruta_img = self._copiar_imagen()
        try:
            conn   = self._get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Employees (LastName, FirstName, BirthDate, Photo, Notes) "
                "VALUES (%s, %s, %s, %s, %s)",
                (apellido, nombre, fecha, ruta_img, notas))
            conn.commit()
            messagebox.showinfo("Éxito", "Empleado creado correctamente.")
            self.limpiar_campos(silencioso=True)
            self.cargar_empleados()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", str(e))
        finally:
            if conn.is_connected():
                cursor.close(); conn.close()

    def leer_empleado(self, event=None):
        """Carga los datos de la fila seleccionada en el formulario."""
        sel = self.tree.selection()
        if not sel:
            return
        eid = self.tree.item(sel[0])['values'][0]
        try:
            conn   = self._get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Employees WHERE EmployeeID = %s", (eid,))
            emp = cursor.fetchone()
            if emp:
                self.poblar_campos(emp)
        except mysql.connector.Error as e:
            messagebox.showerror("Error", str(e))
        finally:
            if conn.is_connected():
                cursor.close(); conn.close()

    def actualizar_empleado(self):
        eid, apellido, nombre, fecha, notas = [e.get().strip() for e in self.entries]
        if not eid:
            messagebox.showwarning("Advertencia", "Selecciona un empleado primero.")
            return
        ruta_img = self._copiar_imagen() if self.image_path else None
        try:
            conn   = self._get_connection()
            cursor = conn.cursor()
            if ruta_img:
                cursor.execute(
                    "UPDATE Employees SET LastName=%s, FirstName=%s, "
                    "BirthDate=%s, Photo=%s, Notes=%s WHERE EmployeeID=%s",
                    (apellido, nombre, fecha, ruta_img, notas, eid))
            else:
                cursor.execute(
                    "UPDATE Employees SET LastName=%s, FirstName=%s, "
                    "BirthDate=%s, Notes=%s WHERE EmployeeID=%s",
                    (apellido, nombre, fecha, notas, eid))
            conn.commit()
            messagebox.showinfo("Éxito", "Empleado actualizado correctamente.")
            self.limpiar_campos(silencioso=True)
            self.cargar_empleados()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", str(e))
        finally:
            if conn.is_connected():
                cursor.close(); conn.close()

    def eliminar_empleado(self):
        eid = self.entries[0].get().strip()
        if not eid:
            messagebox.showwarning("Advertencia", "Ingresa el ID del empleado.")
            return
        if not messagebox.askyesno("Confirmar", f"¿Eliminar empleado ID {eid}?"):
            return
        try:
            conn   = self._get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Employees WHERE EmployeeID = %s", (eid,))
            conn.commit()
            messagebox.showinfo("Éxito", "Empleado eliminado correctamente.")
            self.limpiar_campos(silencioso=True)
            self.cargar_empleados()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", str(e))
        finally:
            if conn.is_connected():
                cursor.close(); conn.close()

    def cargar_empleados(self):
        """Recarga el Treeview con todos los empleados de la BD."""
        try:
            conn   = self._get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT EmployeeID, LastName, FirstName, BirthDate, Photo, Notes "
                "FROM Employees")
            for item in self.tree.get_children():
                self.tree.delete(item)
            for emp in cursor.fetchall():
                self.tree.insert("", tk.END, values=emp)
        except mysql.connector.Error as e:
            messagebox.showerror("Error", str(e))
        finally:
            if conn.is_connected():
                cursor.close(); conn.close()

    def limpiar_campos(self, silencioso=False):
        for e in self.entries:
            e.delete(0, tk.END)
        self.image_path = ""
        self.image_label.config(image="", text="Sin imagen")
        if not silencioso:
            messagebox.showinfo("Limpiar", "Campos limpiados.")


# ── Punto de entrada ──────────────────────────────────────────────────────────
root = tk.Tk()
app  = EmployeeGUI(root)
root.mainloop()
