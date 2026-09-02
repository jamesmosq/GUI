"""
18_frames_layout.py
───────────────────
Frames como layout — División de ventana en zonas
Tkinter intermedio · POO con herencia de tk.Tk

Conceptos:
  LabelFrame → Frame con título visible
  side=LEFT / RIGHT → divide horizontalmente
  fill=BOTH, expand=True → ocupa todo el espacio disponible

Regla: NUNCA mezcles pack() y grid() en el mismo contenedor.
"""

import tkinter as tk
from tkinter import ttk, messagebox


class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("18 — Frames como Layout")
        self.geometry("560x380")
        self.configure(bg="#F0F4F8")
        self.resizable(False, False)
        self.crear_widgets()

    def crear_widgets(self):
        tk.Label(self, text="Layout con Frames",
                 font=("Arial", 13, "bold"), fg="#1F4E79",
                 bg="#F0F4F8").pack(pady=8)

        # Frame principal que contiene los dos paneles
        main_frame = tk.Frame(self, bg="#F0F4F8")
        main_frame.pack(padx=15, pady=5, fill="both", expand=True)

        # ── Panel izquierdo ───────────────────────────────────────────────────
        self.left_frame = tk.LabelFrame(main_frame, text="Entrada de datos",
                                         font=("Arial", 10, "bold"),
                                         bg="#F0F4F8", padx=10, pady=10)
        self.left_frame.pack(side=tk.LEFT, fill="y", padx=(0, 8))

        tk.Label(self.left_frame, text="Texto:",
                 font=("Arial", 11), bg="#F0F4F8").pack(anchor="w")
        self.entry = tk.Entry(self.left_frame, width=22,
                              font=("Arial", 11), relief="solid", bd=1)
        self.entry.pack(pady=5)

        tk.Label(self.left_frame, text="Categoría:",
                 font=("Arial", 11), bg="#F0F4F8").pack(anchor="w")
        self.combo = ttk.Combobox(self.left_frame,
                                  values=["Info", "Advertencia", "Error"],
                                  width=19, state="readonly")
        self.combo.current(0)
        self.combo.pack(pady=5)

        self.check_var = tk.IntVar()
        tk.Checkbutton(self.left_frame, text="Marcar como urgente",
                       variable=self.check_var,
                       font=("Arial", 10), bg="#F0F4F8").pack(anchor="w", pady=5)

        tk.Button(self.left_frame, text="Agregar registro",
                  font=("Arial", 10, "bold"), bg="#4CAF50", fg="white",
                  command=self.agregar).pack(pady=8, fill="x")

        # ── Panel derecho ─────────────────────────────────────────────────────
        self.right_frame = tk.LabelFrame(main_frame, text="Registros",
                                          font=("Arial", 10, "bold"),
                                          bg="#F0F4F8", padx=10, pady=10)
        self.right_frame.pack(side=tk.RIGHT, fill="both", expand=True)

        self.text_area = tk.Text(self.right_frame, width=28, height=12,
                                  font=("Arial", 10), relief="solid", bd=1)
        self.text_area.pack(fill="both", expand=True)

        tk.Button(self.right_frame, text="Limpiar registros",
                  font=("Arial", 10, "bold"), bg="#f44336", fg="white",
                  command=self.limpiar).pack(pady=5, fill="x")

    def agregar(self):
        texto     = self.entry.get().strip()
        categoria = self.combo.get()
        urgente   = "⚠ URGENTE" if self.check_var.get() else ""
        if not texto:
            messagebox.showwarning("Vacío", "Escribe un texto antes de agregar.")
            return
        linea = f"[{categoria}] {urgente} {texto}\n"
        self.text_area.insert(tk.END, linea)
        self.entry.delete(0, tk.END)
        messagebox.showinfo("Agregado", "Registro agregado correctamente.")

    def limpiar(self):
        if messagebox.askyesno("Limpiar", "¿Limpiar todos los registros?"):
            self.text_area.delete("1.0", tk.END)
            messagebox.showinfo("Limpiar", "Registros limpiados.")


if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
