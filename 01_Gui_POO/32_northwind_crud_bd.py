"""
32_northwind_crud_bd.py
───────────────────────
Northwind CRUD completo con MySQL — Treeview + Stored Procedures
Tkinter POO avanzado · Conexión a BD

Requiere:
  pip install mysql-connector-python
  BD: Northwind con los SPs listados abajo

Stored Procedures usados:
  Products:  sp_InsertProduct, sp_UpdateProduct, sp_DeleteProduct,
             sp_GetProduct, sp_GetAllProducts
  Customers: sp_InsertCustomer, sp_UpdateCustomer, sp_DeleteCustomer,
             sp_GetCustomer, sp_GetAllCustomers
  Employees: sp_InsertEmployee, sp_UpdateEmployee, sp_DeleteEmployee,
             sp_GetEmployee, sp_GetAllEmployees

Mejoras respecto al original (TkinterLab):
  - Credenciales en una sección de config visible
  - Scrollbar correctamente posicionada (antes del pack del Treeview)
  - Comentarios pedagógicos en cada sección
  - Nombre de archivo descriptivo
"""

import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from datetime import datetime

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURACIÓN DE CONEXIÓN — Cambia estos valores según tu entorno
# ═══════════════════════════════════════════════════════════════════════════════
DB_CONFIG = {
    "host":     "localhost",
    "database": "Northwind",
    "user":     "root",
    "password": "",          # ← tu contraseña de MySQL
    "autocommit": False
}


# ═══════════════════════════════════════════════════════════════════════════════
# CLASE DE CONEXIÓN A BASE DE DATOS
# ═══════════════════════════════════════════════════════════════════════════════
class DatabaseConnection:
    """Maneja la conexión y ejecución de Stored Procedures."""

    def __init__(self):
        self.connection = None
        self.cursor     = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(**DB_CONFIG)
            self.cursor = self.connection.cursor(buffered=True)
            return True
        except mysql.connector.Error as err:
            messagebox.showerror("Error de Conexión",
                f"No se pudo conectar a la base de datos:\n{err}")
            return False

    def disconnect(self):
        if self.cursor:     self.cursor.close()
        if self.connection: self.connection.close()

    def call_procedure(self, procedure_name, parameters=None):
        """Ejecuta un SP y retorna (success, results)."""
        try:
            if parameters:
                self.cursor.callproc(procedure_name, parameters)
            else:
                self.cursor.callproc(procedure_name)

            results = []
            for result in self.cursor.stored_results():
                results.extend(result.fetchall())
            return True, results

        except mysql.connector.Error as err:
            self.connection.rollback()
            return False, str(err)


# ═══════════════════════════════════════════════════════════════════════════════
# FUNCIONES DE VALIDACIÓN
# ═══════════════════════════════════════════════════════════════════════════════
def validate_numeric(value, field_name):
    if not value.strip():
        return True, None
    try:
        return True, float(value) if '.' in value else int(value)
    except ValueError:
        messagebox.showerror("Validación", f"{field_name} debe ser un número.")
        return False, None

def validate_required(value, field_name):
    if not value.strip():
        messagebox.showerror("Validación", f"{field_name} es obligatorio.")
        return False
    return True

def validate_date(date_string):
    if not date_string.strip():
        return True, None
    try:
        return True, datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Validación", "Fecha debe estar en formato YYYY-MM-DD.")
        return False, None


# ═══════════════════════════════════════════════════════════════════════════════
# INSTANCIA GLOBAL DE CONEXIÓN
# ═══════════════════════════════════════════════════════════════════════════════
db = DatabaseConnection()


# ═══════════════════════════════════════════════════════════════════════════════
# FUNCIONES PARA PRODUCTS
# ═══════════════════════════════════════════════════════════════════════════════
def save_product():
    if not db.connection:
        if not db.connect(): return

    if not validate_required(ProductName.get(), "Nombre del Producto"): return

    supplier_valid, supplier_id = validate_numeric(SupplierID.get(), "ID Proveedor") \
                                  if SupplierID.get().strip() else (True, None)
    if not supplier_valid: return

    category_valid, category_id = validate_numeric(CategoryID.get(), "ID Categoría") \
                                   if CategoryID.get().strip() else (True, None)
    if not category_valid: return

    price_valid, price_value = validate_numeric(Price.get(), "Precio") \
                               if Price.get().strip() else (True, None)
    if not price_valid: return

    success, result = db.call_procedure('sp_InsertProduct', (
        ProductName.get(), supplier_id, category_id,
        Unit.get() if Unit.get().strip() else None, price_value))

    if success:
        messagebox.showinfo("Éxito", "Producto guardado correctamente.")
        clear_product_form()
        load_products_list()
    else:
        messagebox.showerror("Error", f"Error al guardar: {result}")


def update_product():
    if not db.connection:
        if not db.connect(): return

    pid_valid, product_id = validate_numeric(ProductID.get(), "ID Producto")
    if not pid_valid or not product_id:
        messagebox.showerror("Error", "Ingresa un ProductID válido."); return

    if not validate_required(ProductName.get(), "Nombre del Producto"): return

    supplier_valid, supplier_id = validate_numeric(SupplierID.get(), "ID Proveedor") \
                                  if SupplierID.get().strip() else (True, None)
    if not supplier_valid: return

    category_valid, category_id = validate_numeric(CategoryID.get(), "ID Categoría") \
                                   if CategoryID.get().strip() else (True, None)
    if not category_valid: return

    price_valid, price_value = validate_numeric(Price.get(), "Precio") \
                               if Price.get().strip() else (True, None)
    if not price_valid: return

    success, result = db.call_procedure('sp_UpdateProduct', (
        product_id, ProductName.get(), supplier_id,
        category_id, Unit.get() if Unit.get().strip() else None, price_value))

    if success:
        messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
        load_products_list()
    else:
        messagebox.showerror("Error", f"Error al actualizar: {result}")


def delete_product():
    if not db.connection:
        if not db.connect(): return

    pid_valid, product_id = validate_numeric(ProductID.get(), "ID Producto")
    if not pid_valid or not product_id:
        messagebox.showerror("Error", "Ingresa un ProductID válido."); return

    if messagebox.askyesno("Confirmar", "¿Eliminar este producto?"):
        success, result = db.call_procedure('sp_DeleteProduct', (product_id,))
        if success:
            messagebox.showinfo("Éxito", "Producto eliminado.")
            clear_product_form()
            load_products_list()
        else:
            messagebox.showerror("Error", f"Error al eliminar: {result}")


def search_product():
    if not db.connection:
        if not db.connect(): return

    pid_valid, product_id = validate_numeric(ProductID.get(), "ID Producto")
    if not pid_valid or not product_id:
        messagebox.showerror("Error", "Ingresa un ProductID válido."); return

    success, result = db.call_procedure('sp_GetProduct', (product_id,))
    if success and result:
        p = result[0]
        for entry, val in zip(
            [ProductName, SupplierID, CategoryID, Unit, Price],
            [p[1], p[2], p[3], p[4], p[5]]
        ):
            entry.delete(0, tk.END)
            entry.insert(0, val if val else "")
    else:
        messagebox.showinfo("No encontrado", "Producto no encontrado.")


def clear_product_form():
    for e in [ProductID, ProductName, SupplierID, CategoryID, Unit, Price]:
        e.delete(0, tk.END)


def load_products_list():
    if not db.connection:
        if not db.connect(): return
    success, results = db.call_procedure('sp_GetAllProducts')
    if success:
        for item in products_tree.get_children():
            products_tree.delete(item)
        for product in results:
            products_tree.insert('', 'end', values=product)


# ═══════════════════════════════════════════════════════════════════════════════
# FUNCIONES PARA CUSTOMERS
# ═══════════════════════════════════════════════════════════════════════════════
def save_customer():
    if not db.connection:
        if not db.connect(): return
    if not validate_required(CustomerName.get(), "Nombre del Cliente"): return
    success, result = db.call_procedure('sp_InsertCustomer', (
        CustomerName.get(),
        ContactName.get() if ContactName.get().strip() else None,
        Address.get() if Address.get().strip() else None,
        City.get() if City.get().strip() else None,
        PostalCode.get() if PostalCode.get().strip() else None,
        Country.get() if Country.get().strip() else None))
    if success:
        messagebox.showinfo("Éxito", "Cliente guardado correctamente.")
        clear_customer_form()
        load_customers_list()
    else:
        messagebox.showerror("Error", f"Error al guardar: {result}")


def update_customer():
    if not db.connection:
        if not db.connect(): return
    cid_valid, customer_id = validate_numeric(CustomerID.get(), "ID Cliente")
    if not cid_valid or not customer_id:
        messagebox.showerror("Error", "Ingresa un CustomerID válido."); return
    if not validate_required(CustomerName.get(), "Nombre del Cliente"): return
    success, result = db.call_procedure('sp_UpdateCustomer', (
        customer_id, CustomerName.get(),
        ContactName.get() if ContactName.get().strip() else None,
        Address.get() if Address.get().strip() else None,
        City.get() if City.get().strip() else None,
        PostalCode.get() if PostalCode.get().strip() else None,
        Country.get() if Country.get().strip() else None))
    if success:
        messagebox.showinfo("Éxito", "Cliente actualizado.")
        load_customers_list()
    else:
        messagebox.showerror("Error", f"Error al actualizar: {result}")


def delete_customer():
    if not db.connection:
        if not db.connect(): return
    cid_valid, customer_id = validate_numeric(CustomerID.get(), "ID Cliente")
    if not cid_valid or not customer_id:
        messagebox.showerror("Error", "Ingresa un CustomerID válido."); return
    if messagebox.askyesno("Confirmar", "¿Eliminar este cliente?"):
        success, result = db.call_procedure('sp_DeleteCustomer', (customer_id,))
        if success:
            messagebox.showinfo("Éxito", "Cliente eliminado.")
            clear_customer_form()
            load_customers_list()
        else:
            messagebox.showerror("Error", f"Error al eliminar: {result}")


def search_customer():
    if not db.connection:
        if not db.connect(): return
    cid_valid, customer_id = validate_numeric(CustomerID.get(), "ID Cliente")
    if not cid_valid or not customer_id:
        messagebox.showerror("Error", "Ingresa un CustomerID válido."); return
    success, result = db.call_procedure('sp_GetCustomer', (customer_id,))
    if success and result:
        c = result[0]
        for entry, val in zip(
            [CustomerName, ContactName, Address, City, PostalCode, Country],
            [c[1], c[2], c[3], c[4], c[5], c[6]]
        ):
            entry.delete(0, tk.END)
            entry.insert(0, val if val else "")
    else:
        messagebox.showinfo("No encontrado", "Cliente no encontrado.")


def clear_customer_form():
    for e in [CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country]:
        e.delete(0, tk.END)


def load_customers_list():
    if not db.connection:
        if not db.connect(): return
    success, results = db.call_procedure('sp_GetAllCustomers')
    if success:
        for item in customers_tree.get_children():
            customers_tree.delete(item)
        for c in results:
            customers_tree.insert('', 'end', values=c)


# ═══════════════════════════════════════════════════════════════════════════════
# FUNCIONES PARA EMPLOYEES
# ═══════════════════════════════════════════════════════════════════════════════
def save_employee():
    if not db.connection:
        if not db.connect(): return
    if not validate_required(LastName.get(), "Apellido"): return
    if not validate_required(FirstName.get(), "Nombre"):  return
    date_valid, birth_date = validate_date(BirthDate.get())
    if not date_valid: return
    success, result = db.call_procedure('sp_InsertEmployee', (
        LastName.get(), FirstName.get(), birth_date,
        Photo.get() if Photo.get().strip() else None,
        Notes.get('1.0', tk.END).strip() or None))
    if success:
        messagebox.showinfo("Éxito", "Empleado guardado correctamente.")
        clear_employee_form()
        load_employees_list()
    else:
        messagebox.showerror("Error", f"Error al guardar: {result}")


def update_employee():
    if not db.connection:
        if not db.connect(): return
    eid_valid, employee_id = validate_numeric(EmployeeID.get(), "ID Empleado")
    if not eid_valid or not employee_id:
        messagebox.showerror("Error", "Ingresa un EmployeeID válido."); return
    if not validate_required(LastName.get(), "Apellido"):  return
    if not validate_required(FirstName.get(), "Nombre"):   return
    date_valid, birth_date = validate_date(BirthDate.get())
    if not date_valid: return
    success, result = db.call_procedure('sp_UpdateEmployee', (
        employee_id, LastName.get(), FirstName.get(), birth_date,
        Photo.get() if Photo.get().strip() else None,
        Notes.get('1.0', tk.END).strip() or None))
    if success:
        messagebox.showinfo("Éxito", "Empleado actualizado.")
        load_employees_list()
    else:
        messagebox.showerror("Error", f"Error al actualizar: {result}")


def delete_employee():
    if not db.connection:
        if not db.connect(): return
    eid_valid, employee_id = validate_numeric(EmployeeID.get(), "ID Empleado")
    if not eid_valid or not employee_id:
        messagebox.showerror("Error", "Ingresa un EmployeeID válido."); return
    if messagebox.askyesno("Confirmar", "¿Eliminar este empleado?"):
        success, result = db.call_procedure('sp_DeleteEmployee', (employee_id,))
        if success:
            messagebox.showinfo("Éxito", "Empleado eliminado.")
            clear_employee_form()
            load_employees_list()
        else:
            messagebox.showerror("Error", f"Error al eliminar: {result}")


def search_employee():
    if not db.connection:
        if not db.connect(): return
    eid_valid, employee_id = validate_numeric(EmployeeID.get(), "ID Empleado")
    if not eid_valid or not employee_id:
        messagebox.showerror("Error", "Ingresa un EmployeeID válido."); return
    success, result = db.call_procedure('sp_GetEmployee', (employee_id,))
    if success and result:
        e = result[0]
        for entry, val in zip([LastName, FirstName, BirthDate, Photo], [e[1],e[2],e[3],e[4]]):
            entry.delete(0, tk.END)
            if val:
                entry.insert(0, val.strftime("%Y-%m-%d") if hasattr(val, 'strftime') else str(val))
        Notes.delete('1.0', tk.END)
        Notes.insert('1.0', e[5] if e[5] else "")
    else:
        messagebox.showinfo("No encontrado", "Empleado no encontrado.")


def clear_employee_form():
    for e in [EmployeeID, LastName, FirstName, BirthDate, Photo]:
        e.delete(0, tk.END)
    Notes.delete('1.0', tk.END)


def load_employees_list():
    if not db.connection:
        if not db.connect(): return
    success, results = db.call_procedure('sp_GetAllEmployees')
    if success:
        for item in employees_tree.get_children():
            employees_tree.delete(item)
        for emp in results:
            bd = emp[3].strftime("%Y-%m-%d") if emp[3] else ""
            notes_short = (emp[5][:50] + "...") if emp[5] and len(emp[5]) > 50 else emp[5]
            employees_tree.insert('', 'end', values=(emp[0], emp[1], emp[2], bd, emp[4], notes_short))


# ═══════════════════════════════════════════════════════════════════════════════
# EVENTOS DE SELECCIÓN EN TREEVIEW
# ═══════════════════════════════════════════════════════════════════════════════
def on_product_select(event):
    sel = products_tree.selection()
    if sel:
        v = products_tree.item(sel[0])['values']
        for entry, val in zip([ProductID, ProductName, SupplierID, CategoryID, Unit, Price], v):
            entry.delete(0, tk.END)
            entry.insert(0, val if val else "")

def on_customer_select(event):
    sel = customers_tree.selection()
    if sel:
        v = customers_tree.item(sel[0])['values']
        for entry, val in zip([CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country], v):
            entry.delete(0, tk.END)
            entry.insert(0, val if val else "")

def on_employee_select(event):
    sel = employees_tree.selection()
    if sel:
        v = employees_tree.item(sel[0])['values']
        for entry, val in zip([EmployeeID, LastName, FirstName, BirthDate, Photo], v[:5]):
            entry.delete(0, tk.END)
            entry.insert(0, val if val else "")
        Notes.delete('1.0', tk.END)
        Notes.insert('1.0', v[5] if v[5] else "")


# ═══════════════════════════════════════════════════════════════════════════════
# INTERFAZ GRÁFICA
# ═══════════════════════════════════════════════════════════════════════════════
root = tk.Tk()
root.geometry('1200x700')
root.title("32 — Northwind CRUD con MySQL")
root.resizable(True, True)

# Conectar al iniciar
if not db.connect():
    root.destroy()
    exit()

notebook = ttk.Notebook(root)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
notebook.add(tab1, text="  Products  ")
notebook.add(tab2, text="  Customers ")
notebook.add(tab3, text="  Employees ")
notebook.pack(expand=True, fill="both")


# ── PESTAÑA 1: PRODUCTS ───────────────────────────────────────────────────────
main_p = tk.Frame(tab1)
main_p.pack(fill="both", expand=True, padx=10, pady=10)

left_p = tk.Frame(main_p)
left_p.pack(side="left", fill="y", padx=(0,10))

tk.Label(left_p, text="GESTIÓN DE PRODUCTOS",
         font=("Arial", 14, "bold"), fg="#4CAF50").pack(pady=15)

form_p = tk.Frame(left_p)
form_p.pack(padx=20)

for i, (lbl, var_name) in enumerate([
    ("ProductID:", "ProductID"), ("ProductName:", "ProductName"),
    ("SupplierID:", "SupplierID"), ("CategoryID:", "CategoryID"),
    ("Unit:", "Unit"), ("Price:", "Price")
]):
    tk.Label(form_p, text=lbl, font=("Arial", 11)).grid(
        row=i, column=0, sticky="w", padx=(0,8), pady=6)
    e = tk.Entry(form_p, width=22, font=("Arial", 11), relief="solid", bd=1)
    e.grid(row=i, column=1, sticky="w", pady=6)
    globals()[var_name] = e

btn_p = tk.Frame(left_p)
btn_p.pack(pady=12)
for txt, color, cmd in [
    ("Guardar",    "#4CAF50", save_product),
    ("Actualizar", "#2196F3", update_product),
    ("Eliminar",   "#f44336", delete_product),
    ("Buscar",     "#FF9800", search_product),
    ("Limpiar",    "#9E9E9E", clear_product_form),
]:
    tk.Button(btn_p, text=txt, font=("Arial", 9, "bold"),
              bg=color, fg="white", width=9,
              command=cmd).pack(side=tk.LEFT, padx=2)

right_p = tk.Frame(main_p)
right_p.pack(side="right", fill="both", expand=True)
tk.Label(right_p, text="LISTA DE PRODUCTOS",
         font=("Arial", 12, "bold")).pack(pady=8)

# Scrollbar ANTES del pack del Treeview
frame_tree_p = tk.Frame(right_p)
frame_tree_p.pack(fill="both", expand=True, padx=10)

products_tree = ttk.Treeview(frame_tree_p,
    columns=('ID','Name','SupplierID','CategoryID','Unit','Price'),
    show='headings', height=18)
for col, w in zip(('ID','Name','SupplierID','CategoryID','Unit','Price'),
                   (50, 150, 80, 80, 80, 80)):
    products_tree.heading(col, text=col)
    products_tree.column(col, width=w)

sb_p = ttk.Scrollbar(frame_tree_p, orient="vertical", command=products_tree.yview)
products_tree.configure(yscrollcommand=sb_p.set)
products_tree.pack(side=tk.LEFT, fill="both", expand=True)
sb_p.pack(side=tk.RIGHT, fill="y")
products_tree.bind('<<TreeviewSelect>>', on_product_select)


# ── PESTAÑA 2: CUSTOMERS ──────────────────────────────────────────────────────
main_c = tk.Frame(tab2)
main_c.pack(fill="both", expand=True, padx=10, pady=10)

left_c = tk.Frame(main_c)
left_c.pack(side="left", fill="y", padx=(0,10))

tk.Label(left_c, text="GESTIÓN DE CLIENTES",
         font=("Arial", 14, "bold"), fg="#2196F3").pack(pady=15)

form_c = tk.Frame(left_c)
form_c.pack(padx=20)

for i, (lbl, var_name) in enumerate([
    ("CustomerID:", "CustomerID"), ("CustomerName:", "CustomerName"),
    ("ContactName:", "ContactName"), ("Address:", "Address"),
    ("City:", "City"), ("PostalCode:", "PostalCode"), ("Country:", "Country")
]):
    tk.Label(form_c, text=lbl, font=("Arial", 11)).grid(
        row=i, column=0, sticky="w", padx=(0,8), pady=6)
    e = tk.Entry(form_c, width=22, font=("Arial", 11), relief="solid", bd=1)
    e.grid(row=i, column=1, sticky="w", pady=6)
    globals()[var_name] = e

btn_c = tk.Frame(left_c)
btn_c.pack(pady=12)
for txt, color, cmd in [
    ("Guardar",    "#4CAF50", save_customer),
    ("Actualizar", "#2196F3", update_customer),
    ("Eliminar",   "#f44336", delete_customer),
    ("Buscar",     "#FF9800", search_customer),
    ("Limpiar",    "#9E9E9E", clear_customer_form),
]:
    tk.Button(btn_c, text=txt, font=("Arial", 9, "bold"),
              bg=color, fg="white", width=9,
              command=cmd).pack(side=tk.LEFT, padx=2)

right_c = tk.Frame(main_c)
right_c.pack(side="right", fill="both", expand=True)
tk.Label(right_c, text="LISTA DE CLIENTES",
         font=("Arial", 12, "bold")).pack(pady=8)

frame_tree_c = tk.Frame(right_c)
frame_tree_c.pack(fill="both", expand=True, padx=10)

customers_tree = ttk.Treeview(frame_tree_c,
    columns=('ID','Name','Contact','Address','City','Postal','Country'),
    show='headings', height=18)
for col, w in zip(('ID','Name','Contact','Address','City','Postal','Country'),
                   (50,120,100,120,80,60,80)):
    customers_tree.heading(col, text=col)
    customers_tree.column(col, width=w)

sb_c = ttk.Scrollbar(frame_tree_c, orient="vertical", command=customers_tree.yview)
customers_tree.configure(yscrollcommand=sb_c.set)
customers_tree.pack(side=tk.LEFT, fill="both", expand=True)
sb_c.pack(side=tk.RIGHT, fill="y")
customers_tree.bind('<<TreeviewSelect>>', on_customer_select)


# ── PESTAÑA 3: EMPLOYEES ──────────────────────────────────────────────────────
main_e = tk.Frame(tab3)
main_e.pack(fill="both", expand=True, padx=10, pady=10)

left_e = tk.Frame(main_e)
left_e.pack(side="left", fill="y", padx=(0,10))

tk.Label(left_e, text="GESTIÓN DE EMPLEADOS",
         font=("Arial", 14, "bold"), fg="#f44336").pack(pady=15)

form_e = tk.Frame(left_e)
form_e.pack(padx=20)

for i, (lbl, var_name) in enumerate([
    ("EmployeeID:", "EmployeeID"), ("LastName:", "LastName"),
    ("FirstName:", "FirstName"), ("BirthDate (YYYY-MM-DD):", "BirthDate"),
    ("Photo:", "Photo")
]):
    tk.Label(form_e, text=lbl, font=("Arial", 11)).grid(
        row=i, column=0, sticky="w", padx=(0,8), pady=6)
    e = tk.Entry(form_e, width=22, font=("Arial", 11), relief="solid", bd=1)
    e.grid(row=i, column=1, sticky="w", pady=6)
    globals()[var_name] = e

tk.Label(form_e, text="Notes:", font=("Arial", 11)).grid(
    row=5, column=0, sticky="nw", padx=(0,8), pady=6)
Notes = tk.Text(form_e, width=22, height=4, font=("Arial", 11), relief="solid", bd=1)
Notes.grid(row=5, column=1, sticky="w", pady=6)

btn_e = tk.Frame(left_e)
btn_e.pack(pady=12)
for txt, color, cmd in [
    ("Guardar",    "#4CAF50", save_employee),
    ("Actualizar", "#2196F3", update_employee),
    ("Eliminar",   "#f44336", delete_employee),
    ("Buscar",     "#FF9800", search_employee),
    ("Limpiar",    "#9E9E9E", clear_employee_form),
]:
    tk.Button(btn_e, text=txt, font=("Arial", 9, "bold"),
              bg=color, fg="white", width=9,
              command=cmd).pack(side=tk.LEFT, padx=2)

right_e = tk.Frame(main_e)
right_e.pack(side="right", fill="both", expand=True)
tk.Label(right_e, text="LISTA DE EMPLEADOS",
         font=("Arial", 12, "bold")).pack(pady=8)

frame_tree_e = tk.Frame(right_e)
frame_tree_e.pack(fill="both", expand=True, padx=10)

employees_tree = ttk.Treeview(frame_tree_e,
    columns=('ID','LastName','FirstName','BirthDate','Photo','Notes'),
    show='headings', height=18)
for col, w in zip(('ID','LastName','FirstName','BirthDate','Photo','Notes'),
                   (50,100,100,100,80,150)):
    employees_tree.heading(col, text=col)
    employees_tree.column(col, width=w)

sb_e = ttk.Scrollbar(frame_tree_e, orient="vertical", command=employees_tree.yview)
employees_tree.configure(yscrollcommand=sb_e.set)
employees_tree.pack(side=tk.LEFT, fill="both", expand=True)
sb_e.pack(side=tk.RIGHT, fill="y")
employees_tree.bind('<<TreeviewSelect>>', on_employee_select)


# ═══════════════════════════════════════════════════════════════════════════════
# CARGA INICIAL Y CIERRE
# ═══════════════════════════════════════════════════════════════════════════════
def load_initial_data():
    load_products_list()
    load_customers_list()
    load_employees_list()

def on_closing():
    db.disconnect()
    root.destroy()

root.after(500, load_initial_data)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
