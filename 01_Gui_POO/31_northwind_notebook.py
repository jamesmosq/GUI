"""
31_northwind_notebook.py
────────────────────────
Northwind — App con 3 pestañas y CRUD visual (sin BD)
Tkinter POO — nivel avanzado (sin conexión a BD)

Este archivo es la versión mejorada del northwind.py original.
Correcciones aplicadas:
  - Eliminado el SQL comentado al inicio
  - Corregida variable CustomerID → ProductID en pestaña Products
  - Botones con command= y messagebox funcionales
  - Pestaña Employees completada con campos y botones
  - Función limpiar() real en cada pestaña

Siguiente paso → TkinterLab (32) que conecta todo con MySQL.
"""

import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.geometry('900x560')
root.title("31 — Northwind Management (sin BD)")
root.resizable(False, False)

notebook = ttk.Notebook(root)

tab_products  = ttk.Frame(notebook)
tab_customers = ttk.Frame(notebook)
tab_employees = ttk.Frame(notebook)

notebook.add(tab_products,  text="  Products  ")
notebook.add(tab_customers, text="  Customers ")
notebook.add(tab_employees, text="  Employees ")
notebook.pack(expand=True, fill="both")


# ═══════════════════════════════════════════════════════════════════════════════
# PESTAÑA 1 — PRODUCTS
# ═══════════════════════════════════════════════════════════════════════════════
tk.Label(tab_products, text="GESTIÓN DE PRODUCTS",
         font=("Arial", 14, "bold"), fg="#4CAF50").pack(pady=15)

form_p = tk.Frame(tab_products)
form_p.pack(pady=5, anchor="w", padx=50)

campos_p = ["ProductID:", "ProductName:", "SupplierID:", "CategoryID:", "Unit:", "Price:"]
entries_p = {}

for i, campo in enumerate(campos_p):
    tk.Label(form_p, text=campo, font=("Arial", 12)).grid(
        row=i, column=0, sticky="w", padx=(0, 10), pady=8)
    e = tk.Entry(form_p, width=25, font=("Arial", 12), relief="solid", bd=1)
    e.grid(row=i, column=1, sticky="w", pady=8)
    entries_p[campo] = e

def limpiar_p(silencioso=False):
    for e in entries_p.values(): e.delete(0, tk.END)
    if not silencioso: messagebox.showinfo("Limpiar", "Formulario de Productos limpiado.")

btn_frame_p = tk.Frame(tab_products)
btn_frame_p.pack(pady=12)
for txt, color, cmd in [
    ("Guardar",    "#4CAF50", lambda: messagebox.showinfo("Guardar",
        f"Producto '{entries_p['ProductName:'].get()}' guardado.")
        if entries_p["ProductName:"].get()
        else messagebox.showwarning("Advertencia", "Ingresa el nombre del producto.")),
    ("Actualizar", "#2196F3", lambda: messagebox.showinfo("Actualizar", "Producto actualizado.")
        if entries_p["ProductID:"].get()
        else messagebox.showwarning("Advertencia", "Ingresa el ProductID.")),
    ("Eliminar",   "#f44336", lambda: messagebox.askyesno("Eliminar",
        f"¿Eliminar producto ID {entries_p['ProductID:'].get()}?")
        if entries_p["ProductID:"].get()
        else messagebox.showwarning("Advertencia", "Ingresa el ProductID.")),
    ("Limpiar",    "#FF9800", limpiar_p),
]:
    tk.Button(btn_frame_p, text=txt, font=("Arial", 11),
              bg=color, fg="white", width=10,
              command=cmd).pack(side=tk.LEFT, padx=5)


# ═══════════════════════════════════════════════════════════════════════════════
# PESTAÑA 2 — CUSTOMERS
# ═══════════════════════════════════════════════════════════════════════════════
tk.Label(tab_customers, text="GESTIÓN DE CUSTOMERS",
         font=("Arial", 14, "bold"), fg="#2196F3").pack(pady=15)

form_c = tk.Frame(tab_customers)
form_c.pack(pady=5, anchor="w", padx=50)

campos_c = ["CustomerID:", "CustomerName:", "ContactName:", "Address:", "City:", "Country:"]
entries_c = {}

for i, campo in enumerate(campos_c):
    tk.Label(form_c, text=campo, font=("Arial", 12)).grid(
        row=i, column=0, sticky="w", padx=(0, 10), pady=8)
    e = tk.Entry(form_c, width=25, font=("Arial", 12), relief="solid", bd=1)
    e.grid(row=i, column=1, sticky="w", pady=8)
    entries_c[campo] = e

def limpiar_c(silencioso=False):
    for e in entries_c.values(): e.delete(0, tk.END)
    if not silencioso: messagebox.showinfo("Limpiar", "Formulario de Clientes limpiado.")

btn_frame_c = tk.Frame(tab_customers)
btn_frame_c.pack(pady=12)
for txt, color, cmd in [
    ("Guardar",    "#4CAF50", lambda: messagebox.showinfo("Guardar",
        f"Cliente '{entries_c['CustomerName:'].get()}' guardado.")),
    ("Actualizar", "#2196F3", lambda: messagebox.showinfo("Actualizar", "Cliente actualizado.")),
    ("Eliminar",   "#f44336", lambda: messagebox.askyesno("Eliminar", "¿Eliminar este cliente?")),
    ("Limpiar",    "#FF9800", limpiar_c),
]:
    tk.Button(btn_frame_c, text=txt, font=("Arial", 11),
              bg=color, fg="white", width=10,
              command=cmd).pack(side=tk.LEFT, padx=5)


# ═══════════════════════════════════════════════════════════════════════════════
# PESTAÑA 3 — EMPLOYEES
# ═══════════════════════════════════════════════════════════════════════════════
tk.Label(tab_employees, text="GESTIÓN DE EMPLOYEES",
         font=("Arial", 14, "bold"), fg="#f44336").pack(pady=15)

form_e = tk.Frame(tab_employees)
form_e.pack(pady=5, anchor="w", padx=50)

campos_e = ["EmployeeID:", "FirstName:", "LastName:", "BirthDate (YYYY-MM-DD):", "Notes:"]
entries_e = {}

for i, campo in enumerate(campos_e):
    tk.Label(form_e, text=campo, font=("Arial", 12)).grid(
        row=i, column=0, sticky="w", padx=(0, 10), pady=8)
    e = tk.Entry(form_e, width=25, font=("Arial", 12), relief="solid", bd=1)
    e.grid(row=i, column=1, sticky="w", pady=8)
    entries_e[campo] = e

def limpiar_e(silencioso=False):
    for e in entries_e.values(): e.delete(0, tk.END)
    if not silencioso: messagebox.showinfo("Limpiar", "Formulario de Empleados limpiado.")

btn_frame_e = tk.Frame(tab_employees)
btn_frame_e.pack(pady=12)
for txt, color, cmd in [
    ("Guardar",    "#4CAF50", lambda: messagebox.showinfo("Guardar",
        f"Empleado '{entries_e['FirstName:'].get()}' guardado.")),
    ("Actualizar", "#2196F3", lambda: messagebox.showinfo("Actualizar", "Empleado actualizado.")),
    ("Eliminar",   "#f44336", lambda: messagebox.askyesno("Eliminar", "¿Eliminar este empleado?")),
    ("Limpiar",    "#FF9800", limpiar_e),
]:
    tk.Button(btn_frame_e, text=txt, font=("Arial", 11),
              bg=color, fg="white", width=10,
              command=cmd).pack(side=tk.LEFT, padx=5)

root.mainloop()
