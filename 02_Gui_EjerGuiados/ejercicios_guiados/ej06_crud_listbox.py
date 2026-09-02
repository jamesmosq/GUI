"""
ej06_crud_listbox.py
────────────────────
Ejercicio 6 — Formulario + Listbox CRUD en memoria
POO Nivel 3 · Tkinter
"""
import tkinter as tk
from tkinter import messagebox

class GestorEstudiantes(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ej06 — Gestor de Estudiantes")
        self.geometry("500x520")
        self.configure(bg="white")
        self.resizable(False, False)
        self.estudiantes = []
        self.crear_widgets()

    def crear_widgets(self):
        tk.Label(self, text="GESTIÓN DE ESTUDIANTES",
                 font=("Arial", 14, "bold"), fg="#1F4E79", bg="white").pack(pady=15)

        form = tk.Frame(self, bg="white")
        form.pack(pady=5)
        for i, (lbl, key) in enumerate([("Nombre:", "nombre"), ("Nota:", "nota")]):
            tk.Label(form, text=lbl, font=("Arial", 12), bg="white",
                     width=8, anchor="e").grid(row=i, column=0, padx=5, pady=8)
            e = tk.Entry(form, width=28, font=("Arial", 12), relief="solid", bd=1)
            e.grid(row=i, column=1, pady=8)
            setattr(self, f"entry_{key}", e)

        fb = tk.Frame(self, bg="white")
        fb.pack(pady=10)
        for txt, color, cmd in [
            ("Agregar",    "#4CAF50", self.agregar),
            ("Actualizar", "#2196F3", self.actualizar),
            ("Eliminar",   "#f44336", self.eliminar),
            ("Limpiar",    "#FF9800", self.limpiar_form),
        ]:
            tk.Button(fb, text=txt, font=("Arial", 10, "bold"),
                      bg=color, fg="white", width=10,
                      command=cmd).pack(side=tk.LEFT, padx=3)

        tk.Label(self, text="Lista de estudiantes:",
                 font=("Arial", 11, "bold"), bg="white", fg="#2E74B5").pack(anchor="w", padx=20)

        fl = tk.Frame(self, bg="white")
        fl.pack(pady=5)
        self.listbox = tk.Listbox(fl, width=45, height=8, font=("Arial", 11),
                                  selectbackground="#2E74B5", selectforeground="white")
        self.listbox.pack(side=tk.LEFT)
        self.listbox.bind("<<ListboxSelect>>", self.cargar_en_form)
        sb = tk.Scrollbar(fl, command=self.listbox.yview)
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=sb.set)

        self.lbl_resumen = tk.Label(self, text="Total: 0 estudiantes",
                                    font=("Arial", 10), bg="white", fg="gray")
        self.lbl_resumen.pack(pady=5)

    def actualizar_lista(self):
        self.listbox.delete(0, tk.END)
        for e in self.estudiantes:
            self.listbox.insert(tk.END, f"{e['nombre']:<25} Nota: {e['nota']:.1f}")
        self.lbl_resumen.config(text=f"Total: {len(self.estudiantes)} estudiante(s)")

    def cargar_en_form(self, event):
        sel = self.listbox.curselection()
        if not sel:
            return
        e = self.estudiantes[sel[0]]
        for key in ["nombre", "nota"]:
            entry = getattr(self, f"entry_{key}")
            entry.delete(0, tk.END)
            entry.insert(0, e[key])

    def agregar(self):
        nombre = self.entry_nombre.get().strip()
        nota   = self.entry_nota.get().strip()
        if not nombre or not nota:
            messagebox.showerror("Error", "Nombre y nota son obligatorios.")
            return
        if not nota.replace(".", "", 1).isdigit() or not (0 <= float(nota) <= 5):
            messagebox.showerror("Error", "La nota debe ser un número entre 0.0 y 5.0")
            return
        self.estudiantes.append({"nombre": nombre, "nota": float(nota)})
        self.actualizar_lista()
        self.limpiar_form(silencioso=True)
        messagebox.showinfo("Agregado", f"'{nombre}' agregado correctamente.")

    def actualizar(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showwarning("Advertencia", "Selecciona un estudiante.")
            return
        nombre = self.entry_nombre.get().strip()
        nota   = self.entry_nota.get().strip()
        if not nombre or not nota:
            messagebox.showerror("Error", "Completa los campos.")
            return
        self.estudiantes[sel[0]] = {"nombre": nombre, "nota": float(nota)}
        self.actualizar_lista()
        messagebox.showinfo("Actualizado", "Registro actualizado correctamente.")

    def eliminar(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showwarning("Advertencia", "Selecciona un estudiante.")
            return
        nombre = self.estudiantes[sel[0]]["nombre"]
        if messagebox.askyesno("Eliminar", f"¿Eliminar a '{nombre}'?"):
            self.estudiantes.pop(sel[0])
            self.actualizar_lista()
            self.limpiar_form(silencioso=True)
            messagebox.showinfo("Eliminado", f"'{nombre}' eliminado.")

    def limpiar_form(self, silencioso=False):
        self.entry_nombre.delete(0, tk.END)
        self.entry_nota.delete(0, tk.END)
        if not silencioso:
            messagebox.showinfo("Limpiar", "Formulario limpiado.")

GestorEstudiantes().mainloop()
