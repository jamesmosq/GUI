"""
06_northwind_notebook_ui.py
───────────────────────────
Northwind — App con 3 pestañas, botones con messagebox, sin BD
Tkinter · GUI carpeta

Este archivo es la maqueta UI de la app Northwind:
  - 3 pestañas: Products, Customers, Employees
  - Formularios completos con grid()
  - Botones con messagebox funcionales
  - Sin conexión a BD — ideal para diseñar la UI antes de conectar

Siguiente paso → conectar los botones a los SPs
(ver 03_crud_empleados_sp.py y 32_northwind_crud_bd.py en Gui_POO)
"""

import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.geometry('900x600')
root.title("06 — Northwind Notebook UI")
root.resizable(False, False)

notebook = ttk.Notebook(root)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
notebook.add(tab1, text="  Products  ")
notebook.add(tab2, text="  Customers ")
notebook.add(tab3, text="  Employees ")
notebook.pack(expand=True, fill="both")


# ═══════════════════════════════════════════════════════════════════════════════
# FUNCIONES PARA PRODUCTS
# ═══════════════════════════════════════════════════════════════════════════════
def save_product():
    nombre = ProductName.get().strip()
    if not nombre:
        messagebox.showwarning("Advertencia", "Ingresa el nombre del producto.")
        return
    messagebox.showinfo("Guardar", f"Producto '{nombre}' guardado correctamente.")

def update_product():
    pid = ProductID.get().strip()
    if not pid:
        messagebox.showwarning("Advertencia", "Ingresa el ProductID para actualizar.")
        return
    messagebox.showinfo("Actualizar", f"Producto ID {pid} actualizado correctamente.")

def delete_product():
    pid = ProductID.get().strip()
    if not pid:
        messagebox.showwarning("Advertencia", "Ingresa el ProductID para eliminar.")
        return
    if messagebox.askyesno("Eliminar", f"¿Eliminar producto ID {pid}?"):
        messagebox.showinfo("Eliminado", "Producto eliminado correctamente.")
        clear_product_form()

def clear_product_form():
    for e in [ProductID, ProductName, SupplierID, CategoryID, Unit, Price]:
        e.delete(0, tk.END)
    messagebox.showinfo("Limpiar", "Formulario de Productos limpiado.")

# ── PESTAÑA 1: PRODUCTS ───────────────────────────────────────────────────────
tk.Label(tab1, text="FORM PRODUCTS",
         font=("Arial", 15, "bold"), fg="#4CAF50").pack(pady=15)

form_p = tk.Frame(tab1)
form_p.pack(pady=10, anchor="w", padx=50)

campos_p = [("ProductID:", "ProductID"), ("ProductName:", "ProductName"),
            ("SupplierID:", "SupplierID"), ("CategoryID:", "CategoryID"),
            ("Unit:", "Unit"), ("Price:", "Price")]

entries_p = {}
for i, (lbl, key) in enumerate(campos_p):
    tk.Label(form_p, text=lbl, font=("Arial", 12)).grid(
        row=i, column=0, sticky="w", padx=(0,10), pady=8)
    e = tk.Entry(form_p, width=25, font=("Arial", 12), relief="solid", bd=1)
    e.grid(row=i, column=1, sticky="w", pady=8)
    entries_p[key] = e

ProductID, ProductName = entries_p["ProductID"], entries_p["ProductName"]
SupplierID, CategoryID = entries_p["SupplierID"], entries_p["CategoryID"]
Unit, Price            = entries_p["Unit"],        entries_p["Price"]

btn_p = tk.Frame(tab1)
btn_p.pack(pady=15)
for txt, color, cmd in [
    ("Guardar",    "#4CAF50", save_product),
    ("Actualizar", "#2196F3", update_product),
    ("Eliminar",   "#f44336", delete_product),
    ("Limpiar",    "#FF9800", clear_product_form),
]:
    tk.Button(btn_p, text=txt, font=("Arial", 12), bg=color, fg="white",
              width=10, command=cmd).pack(side=tk.LEFT, padx=5)


# ═══════════════════════════════════════════════════════════════════════════════
# FUNCIONES PARA CUSTOMERS
# ═══════════════════════════════════════════════════════════════════════════════
def save_customer():
    nombre = CustomerName.get().strip()
    if not nombre:
        messagebox.showwarning("Advertencia", "Ingresa el nombre del cliente.")
        return
    messagebox.showinfo("Guardar", f"Cliente '{nombre}' guardado correctamente.")

def update_customer():
    cid = CustomerID.get().strip()
    if not cid:
        messagebox.showwarning("Advertencia", "Ingresa el CustomerID.")
        return
    messagebox.showinfo("Actualizar", f"Cliente ID {cid} actualizado.")

def delete_customer():
    cid = CustomerID.get().strip()
    if not cid:
        messagebox.showwarning("Advertencia", "Ingresa el CustomerID.")
        return
    if messagebox.askyesno("Eliminar", f"¿Eliminar cliente ID {cid}?"):
        messagebox.showinfo("Eliminado", "Cliente eliminado correctamente.")
        clear_customer_form()

def clear_customer_form():
    for e in [CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country]:
        e.delete(0, tk.END)
    messagebox.showinfo("Limpiar", "Formulario de Clientes limpiado.")

# ── PESTAÑA 2: CUSTOMERS ──────────────────────────────────────────────────────
tk.Label(tab2, text="GESTIÓN DE CUSTOMERS",
         font=("Arial", 15, "bold"), fg="#2196F3").pack(pady=15)

form_c = tk.Frame(tab2)
form_c.pack(pady=10, anchor="w", padx=50)

campos_c = [("CustomerID:", "CustomerID"), ("CustomerName:", "CustomerName"),
            ("ContactName:", "ContactName"), ("Address:", "Address"),
            ("City:", "City"), ("PostalCode:", "PostalCode"), ("Country:", "Country")]

entries_c = {}
for i, (lbl, key) in enumerate(campos_c):
    tk.Label(form_c, text=lbl, font=("Arial", 12)).grid(
        row=i, column=0, sticky="w", padx=(0,10), pady=8)
    e = tk.Entry(form_c, width=25, font=("Arial", 12), relief="solid", bd=1)
    e.grid(row=i, column=1, sticky="w", pady=8)
    entries_c[key] = e

CustomerID,   CustomerName = entries_c["CustomerID"],  entries_c["CustomerName"]
ContactName,  Address      = entries_c["ContactName"], entries_c["Address"]
City, PostalCode, Country  = entries_c["City"], entries_c["PostalCode"], entries_c["Country"]

btn_c = tk.Frame(tab2)
btn_c.pack(pady=15)
for txt, color, cmd in [
    ("Guardar",    "#4CAF50", save_customer),
    ("Actualizar", "#2196F3", update_customer),
    ("Eliminar",   "#f44336", delete_customer),
    ("Limpiar",    "#FF9800", clear_customer_form),
]:
    tk.Button(btn_c, text=txt, font=("Arial", 12), bg=color, fg="white",
              width=10, command=cmd).pack(side=tk.LEFT, padx=5)


# ═══════════════════════════════════════════════════════════════════════════════
# FUNCIONES PARA EMPLOYEES
# ═══════════════════════════════════════════════════════════════════════════════
def save_employee():
    nombre = FirstName.get().strip()
    if not nombre:
        messagebox.showwarning("Advertencia", "Ingresa el nombre del empleado.")
        return
    messagebox.showinfo("Guardar", f"Empleado '{nombre}' guardado correctamente.")

def update_employee():
    eid = EmployeeID.get().strip()
    if not eid:
        messagebox.showwarning("Advertencia", "Ingresa el EmployeeID.")
        return
    messagebox.showinfo("Actualizar", f"Empleado ID {eid} actualizado.")

def delete_employee():
    eid = EmployeeID.get().strip()
    if not eid:
        messagebox.showwarning("Advertencia", "Ingresa el EmployeeID.")
        return
    if messagebox.askyesno("Eliminar", f"¿Eliminar empleado ID {eid}?"):
        messagebox.showinfo("Eliminado", "Empleado eliminado correctamente.")
        clear_employee_form()

def clear_employee_form():
    for e in [EmployeeID, LastName, FirstName, BirthDate, Photo]:
        e.delete(0, tk.END)
    Notes.delete('1.0', tk.END)
    messagebox.showinfo("Limpiar", "Formulario de Empleados limpiado.")

# ── PESTAÑA 3: EMPLOYEES ──────────────────────────────────────────────────────
tk.Label(tab3, text="GESTIÓN DE EMPLOYEES",
         font=("Arial", 15, "bold"), fg="#f44336").pack(pady=15)

form_e = tk.Frame(tab3)
form_e.pack(pady=10, anchor="w", padx=50)

campos_e = [("EmployeeID:", "EmployeeID"), ("LastName:", "LastName"),
            ("FirstName:", "FirstName"), ("BirthDate (YYYY-MM-DD):", "BirthDate"),
            ("Photo:", "Photo")]

entries_e = {}
for i, (lbl, key) in enumerate(campos_e):
    tk.Label(form_e, text=lbl, font=("Arial", 12)).grid(
        row=i, column=0, sticky="w", padx=(0,10), pady=8)
    e = tk.Entry(form_e, width=25, font=("Arial", 12), relief="solid", bd=1)
    e.grid(row=i, column=1, sticky="w", pady=8)
    entries_e[key] = e

EmployeeID, LastName  = entries_e["EmployeeID"], entries_e["LastName"]
FirstName,  BirthDate = entries_e["FirstName"],  entries_e["BirthDate"]
Photo = entries_e["Photo"]

tk.Label(form_e, text="Notes:", font=("Arial", 12)).grid(
    row=len(campos_e), column=0, sticky="nw", padx=(0,10), pady=8)
Notes = tk.Text(form_e, width=25, height=4, font=("Arial", 12),
                relief="solid", bd=1)
Notes.grid(row=len(campos_e), column=1, sticky="w", pady=8)

btn_e = tk.Frame(tab3)
btn_e.pack(pady=15)
for txt, color, cmd in [
    ("Guardar",    "#4CAF50", save_employee),
    ("Actualizar", "#2196F3", update_employee),
    ("Eliminar",   "#f44336", delete_employee),
    ("Limpiar",    "#FF9800", clear_employee_form),
]:
    tk.Button(btn_e, text=txt, font=("Arial", 12), bg=color, fg="white",
              width=10, command=cmd).pack(side=tk.LEFT, padx=5)

root.mainloop()
