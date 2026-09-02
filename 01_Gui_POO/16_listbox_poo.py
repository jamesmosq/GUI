"""
16_listbox_poo.py
─────────────────
Listbox con POO — Lista de compras
Tkinter intermedio

Primera vez que usamos class App(tk.Tk):
  La clase HEREDA de tk.Tk → ella misma es la ventana
  Todos los widgets usan self en lugar de root
"""

import tkinter as tk
from tkinter import messagebox


class ListaCompras(tk.Tk):
    """App de lista de compras — hereda de tk.Tk."""

    def __init__(self):
        super().__init__()
        self.title("16 — Lista de Compras (POO)")
        self.geometry("360x420")
        self.configure(bg="white")
        self.resizable(False, False)
        self.crear_widgets()

    def crear_widgets(self):
        tk.Label(self, text="Lista de Compras",
                 font=("Arial", 14, "bold"), fg="#1F4E79", bg="white").pack(pady=10)

        # Entry para ingresar elemento
        frame_entrada = tk.Frame(self, bg="white")
        frame_entrada.pack(pady=5)
        self.entry = tk.Entry(frame_entrada, width=22,
                              font=("Arial", 12), relief="solid", bd=1)
        self.entry.pack(side=tk.LEFT, padx=5)
        tk.Button(frame_entrada, text="+ Agregar",
                  font=("Arial", 10, "bold"), bg="#4CAF50", fg="white",
                  command=self.agregar).pack(side=tk.LEFT)

        # Listbox
        frame_lista = tk.Frame(self, bg="white")
        frame_lista.pack(pady=8)
        self.listbox = tk.Listbox(frame_lista, width=30, height=10,
                                  font=("Arial", 11),
                                  selectbackground="#2196F3",
                                  selectforeground="white")
        self.listbox.pack(side=tk.LEFT)
        sb = tk.Scrollbar(frame_lista, command=self.listbox.yview)
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=sb.set)

        # Elementos iniciales
        for item in ["Manzanas", "Peras", "Plátanos", "Leche", "Huevos", "Pan"]:
            self.listbox.insert(tk.END, item)

        # Botones
        frame_btn = tk.Frame(self, bg="white")
        frame_btn.pack(pady=8)
        tk.Button(frame_btn, text="Eliminar",
                  font=("Arial", 10, "bold"), bg="#f44336", fg="white",
                  width=12, command=self.eliminar).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Limpiar todo",
                  font=("Arial", 10, "bold"), bg="#FF9800", fg="white",
                  width=12, command=self.limpiar_todo).pack(side=tk.LEFT, padx=5)

        # Label contador
        self.lbl_total = tk.Label(self, text="Total: 6 items",
                                  font=("Arial", 10), bg="white", fg="gray")
        self.lbl_total.pack()

    def agregar(self):
        nuevo = self.entry.get().strip()
        if not nuevo:
            messagebox.showwarning("Vacío", "Escribe un elemento primero.")
            return
        self.listbox.insert(tk.END, nuevo)
        self.entry.delete(0, tk.END)
        self.actualizar_contador()
        messagebox.showinfo("Agregado", f"'{nuevo}' agregado a la lista.")

    def eliminar(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showwarning("Sin selección", "Selecciona un elemento.")
            return
        nombre = self.listbox.get(sel[0])
        if messagebox.askyesno("Eliminar", f"¿Eliminar '{nombre}'?"):
            self.listbox.delete(sel[0])
            self.actualizar_contador()
            messagebox.showinfo("Eliminado", f"'{nombre}' eliminado.")

    def limpiar_todo(self):
        if messagebox.askyesno("Limpiar", "¿Limpiar toda la lista?"):
            self.listbox.delete(0, tk.END)
            self.actualizar_contador()
            messagebox.showinfo("Lista", "Lista limpiada.")

    def actualizar_contador(self):
        total = self.listbox.size()
        self.lbl_total.config(text=f"Total: {total} item(s)")


if __name__ == "__main__":
    app = ListaCompras()
    app.mainloop()
