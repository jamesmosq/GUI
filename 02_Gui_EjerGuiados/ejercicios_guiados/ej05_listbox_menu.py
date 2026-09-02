"""
ej05_listbox_menu.py
────────────────────
Ejercicio 5 — Listbox, Menu y Toplevel
POO Nivel 3 · Tkinter
"""
import tkinter as tk
from tkinter import messagebox

class AppListboxMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ej05 — Listbox y Menú")
        self.geometry("450x420")
        self.configure(bg="white")
        self.resizable(False, False)
        self.crear_menu()
        self.crear_widgets()

    def crear_menu(self):
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)
        m = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Archivo", menu=m)
        m.add_command(label="Limpiar lista", command=self.limpiar)
        m.add_separator()
        m.add_command(label="Salir", command=self.cerrar)
        m2 = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Ayuda", menu=m2)
        m2.add_command(label="Acerca de", command=self.acerca_de)

    def crear_widgets(self):
        tk.Label(self, text="LISTA DE ESTUDIANTES",
                 font=("Arial", 14, "bold"), fg="#1F4E79", bg="white").pack(pady=15)
        fe = tk.Frame(self, bg="white")
        fe.pack(pady=5)
        tk.Label(fe, text="Nombre:", font=("Arial", 12), bg="white").pack(side=tk.LEFT)
        self.entry_nombre = tk.Entry(fe, width=25, font=("Arial", 12), relief="solid", bd=1)
        self.entry_nombre.pack(side=tk.LEFT, padx=10)

        fl = tk.Frame(self, bg="white")
        fl.pack(pady=10)
        self.listbox = tk.Listbox(fl, width=35, height=8, font=("Arial", 11),
                                  selectbackground="#2E74B5", selectforeground="white")
        self.listbox.pack(side=tk.LEFT)
        sb = tk.Scrollbar(fl, command=self.listbox.yview)
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=sb.set)

        fb = tk.Frame(self, bg="white")
        fb.pack(pady=10)
        for txt, color, cmd in [
            ("Agregar",  "#4CAF50", self.agregar),
            ("Eliminar", "#f44336", self.eliminar),
            ("Ver info", "#2196F3", self.ver_info),
        ]:
            tk.Button(fb, text=txt, font=("Arial", 11, "bold"),
                      bg=color, fg="white", width=10,
                      command=cmd).pack(side=tk.LEFT, padx=5)

    def agregar(self):
        nombre = self.entry_nombre.get().strip()
        if not nombre:
            messagebox.showwarning("Advertencia", "Escribe un nombre primero.")
            return
        self.listbox.insert(tk.END, nombre)
        self.entry_nombre.delete(0, tk.END)
        messagebox.showinfo("Agregado", f"'{nombre}' agregado a la lista.")

    def eliminar(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showwarning("Advertencia", "Selecciona un elemento.")
            return
        nombre = self.listbox.get(sel[0])
        if messagebox.askyesno("Eliminar", f"¿Eliminar a '{nombre}'?"):
            self.listbox.delete(sel[0])
            messagebox.showinfo("Eliminado", f"'{nombre}' eliminado.")

    def ver_info(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showwarning("Advertencia", "Selecciona un elemento.")
            return
        messagebox.showinfo("Info",
            f"Seleccionado: {self.listbox.get(sel[0])}\nTotal: {self.listbox.size()}")

    def limpiar(self):
        if messagebox.askyesno("Limpiar", "¿Limpiar toda la lista?"):
            self.listbox.delete(0, tk.END)
            messagebox.showinfo("Lista", "Lista limpiada.")

    def acerca_de(self):
        messagebox.showinfo("Acerca de", "Ejercicio 5 — Listbox y Menú\nPOO Nivel 3")

    def cerrar(self):
        if messagebox.askyesno("Salir", "¿Deseas cerrar?"):
            self.destroy()

AppListboxMenu().mainloop()
