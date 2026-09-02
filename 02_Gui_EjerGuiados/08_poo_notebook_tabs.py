"""
08_poo_notebook_tabs.py
───────────────────────
ttk.Notebook con múltiples pestañas — estilo Northwind
Nivel: intermedio-avanzado

Mejoras respecto al northwind.py original:
  • Eliminado el SQL comentado del inicio
  • Corrección: ProductID usa variable correcta (no CustomerID)
  • Botones con command= y messagebox funcionales
  • Botón Limpiar con función real en cada pestaña
  • Código limpio y comentado

Próximo paso → ver 09_northwind_poo.py (versión con clases por pestaña)
"""

import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.geometry("800x500")
root.title("08 — Notebook con Pestañas")
root.resizable(False, False)

notebook = ttk.Notebook(root)

tab_products  = ttk.Frame(notebook)
tab_customers = ttk.Frame(notebook)
tab_employees = ttk.Frame(notebook)

notebook.add(tab_products,  text="  Products  ")
notebook.add(tab_customers, text="  Customers ")
notebook.add(tab_employees, text="  Employees ")
notebook.pack(expand=True, fill="both")

# ══════════════════════════════════════════════════════════════════
# PESTAÑA 1 — PRODUCTS
# ══════════════════════════════════════════════════════════════════
tk.Label(tab_products, text="FORM PRODUCTS",
         font=("Arial", 16, "bold"), fg="green").pack(pady=20)

form_p = tk.Frame(tab_products)
form_p.pack(pady=10, anchor="w", padx=50)

campos_p = ["ProductID:", "ProductName:", "SupplierID:",
            "CategoryID:", "Unit:", "Price:"]
entries_p = {}

for i, campo in enumerate(campos_p):
    tk.Label(form_p, text=campo, font=("Arial", 12)).grid(
        row=i, column=0, sticky="w", padx=(0, 10), pady=8)
    e = tk.Entry(form_p, width=25, font=("Arial", 12), relief="solid", bd=1)
    e.grid(row=i, column=1, sticky="w", pady=8)
    entries_p[campo] = e

def limpiar_productos():
    for e in entries_p.values():
        e.delete(0, tk.END)
    messagebox.showinfo("Limpiar", "Formulario de Productos limpiado.")

btn_frame_p = tk.Frame(tab_products)
btn_frame_p.pack(pady=15)

for txt, color, cmd in [
    ("Guardar",    "#4CAF50",
     lambda: messagebox.showinfo("Guardar", f"Producto '{entries_p['ProductName:'].get()}' guardado.")),
    ("Actualizar", "#2196F3",
     lambda: messagebox.showinfo("Actualizar", "Producto actualizado.")),
    ("Eliminar",   "#f44336",
     lambda: messagebox.askyesno("Eliminar", "¿Eliminar este producto?")),
    ("Limpiar",    "#FF9800", limpiar_productos),
]:
    tk.Button(btn_frame_p, text=txt, font=("Arial", 12),
              bg=color, fg="white", width=10,
              command=cmd).pack(side=tk.LEFT, padx=5)

# ══════════════════════════════════════════════════════════════════
# PESTAÑA 2 — CUSTOMERS
# ══════════════════════════════════════════════════════════════════
tk.Label(tab_customers, text="GESTIÓN DE CUSTOMERS",
         font=("Arial", 16, "bold"), fg="#2196F3").pack(pady=20)

form_c = tk.Frame(tab_customers)
form_c.pack(pady=10, anchor="w", padx=50)

campos_c = ["CustomerID:", "CustomerName:", "ContactName:", "Address:"]
entries_c = {}

for i, campo in enumerate(campos_c):
    tk.Label(form_c, text=campo, font=("Arial", 12)).grid(
        row=i, column=0, sticky="w", padx=(0, 10), pady=10)
    e = tk.Entry(form_c, width=25, font=("Arial", 12), relief="solid", bd=1)
    e.grid(row=i, column=1, sticky="w", pady=10)
    entries_c[campo] = e

def limpiar_customers():
    for e in entries_c.values():
        e.delete(0, tk.END)
    messagebox.showinfo("Limpiar", "Formulario de Clientes limpiado.")

btn_frame_c = tk.Frame(tab_customers)
btn_frame_c.pack(pady=15)

for txt, color, cmd in [
    ("Guardar",    "#4CAF50",
     lambda: messagebox.showinfo("Guardar", f"Cliente '{entries_c['CustomerName:'].get()}' guardado.")),
    ("Actualizar", "#2196F3",
     lambda: messagebox.showinfo("Actualizar", "Cliente actualizado.")),
    ("Eliminar",   "#f44336",
     lambda: messagebox.askyesno("Eliminar", "¿Eliminar este cliente?")),
    ("Limpiar",    "#FF9800", limpiar_customers),
]:
    tk.Button(btn_frame_c, text=txt, font=("Arial", 12),
              bg=color, fg="white", width=10,
              command=cmd).pack(side=tk.LEFT, padx=5)

# ══════════════════════════════════════════════════════════════════
# PESTAÑA 3 — EMPLOYEES
# ══════════════════════════════════════════════════════════════════
tk.Label(tab_employees, text="GESTIÓN DE EMPLOYEES",
         font=("Arial", 16, "bold"), fg="#f44336").pack(pady=20)

form_e = tk.Frame(tab_employees)
form_e.pack(pady=10, anchor="w", padx=50)

campos_e = ["EmployeeID:", "FirstName:", "LastName:", "BirthDate:", "Notes:"]
entries_e = {}

for i, campo in enumerate(campos_e):
    tk.Label(form_e, text=campo, font=("Arial", 12)).grid(
        row=i, column=0, sticky="w", padx=(0, 10), pady=8)
    e = tk.Entry(form_e, width=25, font=("Arial", 12), relief="solid", bd=1)
    e.grid(row=i, column=1, sticky="w", pady=8)
    entries_e[campo] = e

def limpiar_employees():
    for e in entries_e.values():
        e.delete(0, tk.END)
    messagebox.showinfo("Limpiar", "Formulario de Empleados limpiado.")

btn_frame_e = tk.Frame(tab_employees)
btn_frame_e.pack(pady=15)

for txt, color, cmd in [
    ("Guardar",    "#4CAF50",
     lambda: messagebox.showinfo("Guardar", f"Empleado '{entries_e['FirstName:'].get()}' guardado.")),
    ("Actualizar", "#2196F3",
     lambda: messagebox.showinfo("Actualizar", "Empleado actualizado.")),
    ("Eliminar",   "#f44336",
     lambda: messagebox.askyesno("Eliminar", "¿Eliminar este empleado?")),
    ("Limpiar",    "#FF9800", limpiar_employees),
]:
    tk.Button(btn_frame_e, text=txt, font=("Arial", 12),
              bg=color, fg="white", width=10,
              command=cmd).pack(side=tk.LEFT, padx=5)

root.mainloop()
