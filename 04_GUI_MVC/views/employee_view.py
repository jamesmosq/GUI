"""
views/employee_view.py
────────────────────────
VISTA de Employees. Solo widgets Tkinter — sin BD ni validaciones.
Usa DateEntry (tkcalendar) para BirthDate, igual que 03_GUI_DB/03_crud_empleados_sp.py.
"""

import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

FIELDS = [
    ("EmployeeID:", "EmployeeID"),
    ("LastName:",   "LastName"),
    ("FirstName:",  "FirstName"),
    ("Photo:",      "Photo"),
]

TREE_COLUMNS = (('ID', 50), ('LastName', 100), ('FirstName', 100),
                 ('BirthDate', 100), ('Photo', 80), ('Notes', 150))


class EmployeeView(ttk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.entries = {}
        self._crear_widgets()

    def _crear_widgets(self):
        main = tk.Frame(self)
        main.pack(fill="both", expand=True, padx=10, pady=10)

        left = tk.Frame(main)
        left.pack(side="left", fill="y", padx=(0, 10))

        tk.Label(left, text="GESTIÓN DE EMPLEADOS",
                 font=("Arial", 14, "bold"), fg="#f44336").pack(pady=15)

        form = tk.Frame(left)
        form.pack(padx=20)

        tk.Label(form, text="EmployeeID:", font=("Arial", 11)).grid(
            row=0, column=0, sticky="w", padx=(0, 8), pady=6)
        e = tk.Entry(form, width=22, font=("Arial", 11), relief="solid", bd=1)
        e.grid(row=0, column=1, sticky="w", pady=6)
        self.entries["EmployeeID"] = e

        tk.Label(form, text="LastName:", font=("Arial", 11)).grid(
            row=1, column=0, sticky="w", padx=(0, 8), pady=6)
        e = tk.Entry(form, width=22, font=("Arial", 11), relief="solid", bd=1)
        e.grid(row=1, column=1, sticky="w", pady=6)
        self.entries["LastName"] = e

        tk.Label(form, text="FirstName:", font=("Arial", 11)).grid(
            row=2, column=0, sticky="w", padx=(0, 8), pady=6)
        e = tk.Entry(form, width=22, font=("Arial", 11), relief="solid", bd=1)
        e.grid(row=2, column=1, sticky="w", pady=6)
        self.entries["FirstName"] = e

        tk.Label(form, text="BirthDate:", font=("Arial", 11)).grid(
            row=3, column=0, sticky="w", padx=(0, 8), pady=6)
        self.birth_date = DateEntry(form, width=19, background='darkblue',
                                     foreground='white', borderwidth=2,
                                     date_pattern='yyyy-mm-dd', font=("Arial", 11))
        self.birth_date.grid(row=3, column=1, sticky="w", pady=6)

        tk.Label(form, text="Photo:", font=("Arial", 11)).grid(
            row=4, column=0, sticky="w", padx=(0, 8), pady=6)
        e = tk.Entry(form, width=22, font=("Arial", 11), relief="solid", bd=1)
        e.grid(row=4, column=1, sticky="w", pady=6)
        self.entries["Photo"] = e

        tk.Label(form, text="Notes:", font=("Arial", 11)).grid(
            row=5, column=0, sticky="nw", padx=(0, 8), pady=6)
        self.notes = tk.Text(form, width=22, height=4, font=("Arial", 11), relief="solid", bd=1)
        self.notes.grid(row=5, column=1, sticky="w", pady=6)

        btns = tk.Frame(left)
        btns.pack(pady=12)
        for txt, color, cmd in [
            ("Guardar",    "#4CAF50", lambda: self.controller.guardar()),
            ("Actualizar", "#2196F3", lambda: self.controller.actualizar()),
            ("Eliminar",   "#f44336", lambda: self.controller.eliminar()),
            ("Buscar",     "#FF9800", lambda: self.controller.buscar()),
            ("Limpiar",    "#9E9E9E", lambda: self.controller.limpiar()),
        ]:
            tk.Button(btns, text=txt, font=("Arial", 9, "bold"),
                      bg=color, fg="white", width=9, command=cmd).pack(side="left", padx=2)

        right = tk.Frame(main)
        right.pack(side="right", fill="both", expand=True)
        tk.Label(right, text="LISTA DE EMPLEADOS",
                 font=("Arial", 12, "bold")).pack(pady=8)

        frame_tree = tk.Frame(right)
        frame_tree.pack(fill="both", expand=True, padx=10)

        cols = [c for c, _ in TREE_COLUMNS]
        self.tree = ttk.Treeview(frame_tree, columns=cols, show='headings', height=18)
        for col, width in TREE_COLUMNS:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width)

        scrollbar = ttk.Scrollbar(frame_tree, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        self.tree.bind('<<TreeviewSelect>>', lambda e: self.controller.on_select(e))

    # ── API usada por el controlador ──────────────────────────────────────────
    def get_form_data(self) -> dict:
        data = {key: entry.get() for key, entry in self.entries.items()}
        data["BirthDate"] = self.birth_date.get()
        data["Notes"] = self.notes.get('1.0', tk.END).strip()
        return data

    def set_form_data(self, values: dict):
        for key, entry in self.entries.items():
            entry.delete(0, tk.END)
            val = values.get(key)
            if val is not None:
                entry.insert(0, str(val))

        birth_date = values.get("BirthDate")
        if birth_date:
            try:
                self.birth_date.set_date(birth_date)
            except Exception:
                pass

        self.notes.delete('1.0', tk.END)
        notes = values.get("Notes")
        if notes:
            self.notes.insert('1.0', str(notes))

    def clear_form(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.notes.delete('1.0', tk.END)

    def set_tree_data(self, rows):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in rows:
            self.tree.insert('', 'end', values=row)

    def get_selected_tree_values(self):
        selection = self.tree.selection()
        if not selection:
            return None
        return self.tree.item(selection[0])['values']
