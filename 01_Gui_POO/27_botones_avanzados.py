"""
27_botones_avanzados.py
───────────────────────
Botones avanzados — estado, toggle, confirmación, hover, estilos
Tkinter intermedio · POO con clase que recibe root

Complementa al 22 — aquí el foco es en el comportamiento
del botón mismo: cómo cambiar su texto, habilitarlo/deshabilitarlo,
agregar confirmación y efectos visuales.
"""

import tkinter as tk
from tkinter import ttk, messagebox


class EjemploBotones:
    def __init__(self, root):
        self.root = root
        self.root.title("27 — Botones Avanzados")
        self.root.geometry("420x520")
        self.root.configure(bg="white")
        self.root.resizable(False, False)

        tk.Label(root, text="Botones Avanzados",
                 font=("Arial", 14, "bold"), fg="#1F4E79", bg="white").pack(pady=12)

        frame = ttk.Frame(root, padding="15")
        frame.pack(fill=tk.BOTH, expand=True)

        # 1. Botón básico
        ttk.Label(frame, text="1. Botón básico:").pack(anchor=tk.W, pady=(0,3))
        ttk.Button(frame, text="Haz clic",
                   command=self.boton_basico_click).pack(fill=tk.X, pady=(0,10))

        # 2. Botón que cambia su texto
        ttk.Label(frame, text="2. Botón que cambia de texto:").pack(anchor=tk.W, pady=(0,3))
        self.btn_cambiar = tk.Button(frame, text="Cambiar texto",
                                      font=("Arial", 10, "bold"),
                                      bg="#2196F3", fg="white",
                                      command=self.cambiar_texto)
        self.btn_cambiar.pack(fill=tk.X, pady=(0,10))

        # 3. Botón habilitar/deshabilitar
        ttk.Label(frame, text="3. Habilitar / Deshabilitar:").pack(anchor=tk.W, pady=(0,3))
        self.btn_controlado = tk.Button(frame, text="Botón controlado",
                                         font=("Arial", 10, "bold"),
                                         bg="#9E9E9E", fg="white",
                                         state="disabled")
        self.btn_controlado.pack(fill=tk.X, pady=(0,5))
        tk.Button(frame, text="Habilitar / Deshabilitar",
                  font=("Arial", 10, "bold"), bg="#FF9800", fg="white",
                  command=self.toggle_boton).pack(fill=tk.X, pady=(0,10))

        # 4. Botón que lee Entry
        ttk.Label(frame, text="4. Botón que lee Entry:").pack(anchor=tk.W, pady=(0,3))
        self.entry = ttk.Entry(frame, font=("Arial", 11))
        self.entry.pack(fill=tk.X, pady=(0,5))
        ttk.Button(frame, text="Leer Entry",
                   command=self.leer_entry).pack(fill=tk.X, pady=(0,10))

        # 5. Botón con confirmación
        ttk.Label(frame, text="5. Con confirmación askyesno:").pack(anchor=tk.W, pady=(0,3))
        tk.Button(frame, text="Acción importante (pide confirmación)",
                  font=("Arial", 10, "bold"), bg="#f44336", fg="white",
                  command=self.confirmar_accion).pack(fill=tk.X, pady=(0,10))

        # 6. Estilos tk vs ttk
        ttk.Label(frame, text="6. tk.Button vs ttk.Button:").pack(anchor=tk.W, pady=(0,3))
        f_estilos = tk.Frame(frame, bg="white")
        f_estilos.pack(fill=tk.X)
        tk.Button(f_estilos, text="tk (más personalizable)",
                  bg="#1F4E79", fg="white", font=("Arial", 10, "bold"),
                  command=lambda: messagebox.showinfo("tk", "Botón tk: permite bg, fg, etc.")).pack(
            side=tk.LEFT, padx=(0,5), fill=tk.X, expand=True)
        ttk.Button(f_estilos, text="ttk (nativo SO)",
                   command=lambda: messagebox.showinfo("ttk", "Botón ttk: estilo del SO.")).pack(
            side=tk.LEFT, fill=tk.X, expand=True)

    def boton_basico_click(self):
        messagebox.showinfo("Clic", "¡Has hecho clic en el botón básico!")

    def cambiar_texto(self):
        actual = self.btn_cambiar["text"]
        nuevo  = "Texto original" if actual == "Texto cambiado ✔" else "Texto cambiado ✔"
        self.btn_cambiar["text"] = nuevo

    def toggle_boton(self):
        estado = str(self.btn_controlado["state"])
        if estado == "disabled":
            self.btn_controlado.config(state="normal", bg="#4CAF50",
                                        text="Botón habilitado ✔")
            messagebox.showinfo("Estado", "Botón habilitado.")
        else:
            self.btn_controlado.config(state="disabled", bg="#9E9E9E",
                                        text="Botón controlado")

    def leer_entry(self):
        texto = self.entry.get().strip()
        if texto:
            messagebox.showinfo("Contenido", f"El entry contiene: {texto}")
        else:
            messagebox.showwarning("Vacío", "El entry está vacío.")

    def confirmar_accion(self):
        if messagebox.askyesno("Confirmar", "¿Estás seguro de realizar esta acción?"):
            messagebox.showinfo("Éxito", "Acción realizada correctamente.")
        else:
            messagebox.showinfo("Cancelado", "Acción cancelada.")


if __name__ == "__main__":
    root = tk.Tk()
    app  = EjemploBotones(root)
    root.mainloop()
