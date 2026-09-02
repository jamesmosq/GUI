"""
24_formulario_secciones.py
──────────────────────────
Formulario organizado en secciones con LabelFrame y Separator
Tkinter intermedio · POO con clase que recibe root

Conceptos nuevos:
  ttk.LabelFrame → Frame con título visible (agrupa campos)
  ttk.Separator  → línea divisoria horizontal o vertical
  tk.Text        → para campos de texto multilínea (ej. Dirección)
"""

import tkinter as tk
from tkinter import ttk, messagebox


class AplicacionOrganizada:
    def __init__(self, root):
        self.root = root
        self.root.title("24 — Formulario con Secciones")
        self.root.geometry("500x580")
        self.root.resizable(False, False)

        frame_principal = ttk.Frame(root, padding="20")
        frame_principal.pack(fill=tk.BOTH, expand=True)

        self.crear_seccion_personal(frame_principal)
        ttk.Separator(frame_principal, orient='horizontal').pack(fill=tk.X, pady=15)
        self.crear_seccion_contacto(frame_principal)
        ttk.Separator(frame_principal, orient='horizontal').pack(fill=tk.X, pady=15)
        self.crear_seccion_botones(frame_principal)

    def crear_seccion_personal(self, padre):
        frame = ttk.LabelFrame(padre, text="Datos Personales", padding="10")
        frame.pack(fill=tk.X, pady=5)

        for i, (lbl, key) in enumerate([("Nombre:", "nombre"),
                                          ("Apellido:", "apellido"),
                                          ("Edad:", "edad")]):
            ttk.Label(frame, text=lbl).grid(row=i, column=0,
                                             sticky=tk.W, pady=6)
            e = ttk.Entry(frame,
                          width=10 if key == "edad" else 30)
            e.grid(row=i, column=1, sticky=tk.EW if key != "edad" else tk.W,
                   padx=5, pady=6)
            setattr(self, f"entry_{key}", e)

        frame.columnconfigure(1, weight=1)

    def crear_seccion_contacto(self, padre):
        frame = ttk.LabelFrame(padre, text="Datos de Contacto", padding="10")
        frame.pack(fill=tk.X, pady=5)

        ttk.Label(frame, text="Email:").pack(anchor=tk.W)
        self.entry_email = ttk.Entry(frame)
        self.entry_email.pack(fill=tk.X, pady=5)

        frame_tel = ttk.Frame(frame)
        frame_tel.pack(fill=tk.X, pady=5)
        ttk.Label(frame_tel, text="Teléfono:").pack(side=tk.LEFT)
        self.entry_telefono = ttk.Entry(frame_tel)
        self.entry_telefono.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)

        ttk.Label(frame, text="Dirección:").pack(anchor=tk.W)
        self.text_direccion = tk.Text(frame, height=3,
                                      font=("Arial", 10), relief="solid", bd=1)
        self.text_direccion.pack(fill=tk.X, pady=5)

    def crear_seccion_botones(self, padre):
        frame = ttk.Frame(padre)
        frame.pack(fill=tk.X, pady=5)

        tk.Button(frame, text="Guardar",
                  font=("Arial", 11, "bold"), bg="#4CAF50", fg="white",
                  width=12, command=self.guardar).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Limpiar",
                  font=("Arial", 11, "bold"), bg="#FF9800", fg="white",
                  width=12, command=self.limpiar).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Salir",
                  font=("Arial", 11, "bold"), bg="#f44336", fg="white",
                  width=12,
                  command=lambda: self.root.destroy()
                  if messagebox.askyesno("Salir", "¿Cerrar la aplicación?")
                  else None).pack(side=tk.RIGHT, padx=5)

    def guardar(self):
        nombre   = self.entry_nombre.get().strip()
        apellido = self.entry_apellido.get().strip()
        if not nombre or not apellido:
            messagebox.showerror("Error", "Nombre y Apellido son obligatorios.")
            return
        messagebox.showinfo("Guardado",
            f"Datos de {nombre} {apellido} guardados correctamente.")

    def limpiar(self):
        for attr in ["entry_nombre", "entry_apellido", "entry_edad",
                     "entry_email", "entry_telefono"]:
            getattr(self, attr).delete(0, tk.END)
        self.text_direccion.delete("1.0", tk.END)
        messagebox.showinfo("Limpiar", "Formulario limpiado.")


if __name__ == "__main__":
    root = tk.Tk()
    app  = AplicacionOrganizada(root)
    root.mainloop()
