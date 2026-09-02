"""
22_entry_button_avanzado.py
───────────────────────────
Entry y Button avanzados — placeholder, validación, eventos, estado
Tkinter intermedio · POO con clase que recibe root

Conceptos nuevos:
  entry.bind('<FocusIn>', fn)      → evento al hacer clic en el Entry
  entry.bind('<FocusOut>', fn)     → evento al salir del Entry
  entry.bind('<Enter>', fn)        → ratón encima del widget
  validate='key'                   → validación en tiempo real
  button.config(state='disabled')  → deshabilitar botón
"""

import tkinter as tk
from tkinter import messagebox


class EjemploButtonsEntries:
    def __init__(self, root):
        self.root = root
        self.root.title("22 — Entry y Button Avanzados")
        self.root.geometry("400x520")
        self.root.configure(bg="white")
        self.root.resizable(False, False)

        tk.Label(root, text="Entry y Button Avanzados",
                 font=("Arial", 13, "bold"), fg="#1F4E79", bg="white").pack(pady=12)

        # ── Entry con texto por defecto ───────────────────────────────────────
        tk.Label(root, text="Entry básico:", font=("Arial", 11), bg="white").pack()
        self.entry_basico = tk.Entry(root, width=28, font=("Arial", 11),
                                     relief="solid", bd=1)
        self.entry_basico.pack(pady=5)
        self.entry_basico.insert(0, "Texto por defecto")

        # ── Entry para contraseña ─────────────────────────────────────────────
        tk.Label(root, text="Contraseña:", font=("Arial", 11), bg="white").pack()
        self.entry_password = tk.Entry(root, width=28, font=("Arial", 11),
                                       show="*", relief="solid", bd=1)
        self.entry_password.pack(pady=5)

        # ── Entry con placeholder (comportamiento) ────────────────────────────
        tk.Label(root, text="Entry con placeholder:", font=("Arial", 11), bg="white").pack()
        self.entry_placeholder = tk.Entry(root, width=28, font=("Arial", 11),
                                          relief="solid", bd=1, fg="grey")
        self.entry_placeholder.pack(pady=5)
        self.entry_placeholder.insert(0, "Escribe aquí...")
        self.entry_placeholder.bind('<FocusIn>',  self.on_entry_click)
        self.entry_placeholder.bind('<FocusOut>', self.on_focus_out)

        # ── Entry solo números (validación en tiempo real) ────────────────────
        tk.Label(root, text="Solo números:", font=("Arial", 11), bg="white").pack()
        vcmd = (root.register(self.validar_numero), '%P')
        self.entry_numerico = tk.Entry(root, width=28, font=("Arial", 11),
                                       validate='key',
                                       validatecommand=vcmd,
                                       relief="solid", bd=1)
        self.entry_numerico.pack(pady=5)

        # ── Botones ───────────────────────────────────────────────────────────
        tk.Button(root, text="Leer Entry básico",
                  font=("Arial", 10, "bold"), bg="#4CAF50", fg="white",
                  width=22, command=self.leer_entry).pack(pady=5)

        # Botón que se habilita/deshabilita
        self.btn_toggle = tk.Button(root, text="Botón deshabilitado",
                                    font=("Arial", 10, "bold"), bg="#9E9E9E",
                                    fg="white", width=22, state="disabled")
        self.btn_toggle.pack(pady=5)

        tk.Button(root, text="Habilitar / Deshabilitar",
                  font=("Arial", 10, "bold"), bg="#2196F3", fg="white",
                  width=22, command=self.toggle_boton).pack(pady=5)

        # Botón con hover (cambia color al pasar el mouse)
        self.btn_hover = tk.Button(root, text="Botón con efecto hover",
                                   font=("Arial", 10, "bold"), bg="#607D8B",
                                   fg="white", width=22,
                                   command=lambda: messagebox.showinfo(
                                       "Hover", "Pasaste el mouse por encima."))
        self.btn_hover.pack(pady=5)
        self.btn_hover.bind('<Enter>', lambda e: self.btn_hover.config(bg="#37474F"))
        self.btn_hover.bind('<Leave>', lambda e: self.btn_hover.config(bg="#607D8B"))

    def on_entry_click(self, event):
        if self.entry_placeholder.get() == "Escribe aquí...":
            self.entry_placeholder.delete(0, tk.END)
            self.entry_placeholder.config(fg='black')

    def on_focus_out(self, event):
        if self.entry_placeholder.get() == "":
            self.entry_placeholder.insert(0, "Escribe aquí...")
            self.entry_placeholder.config(fg='grey')

    def validar_numero(self, nuevo_valor):
        if nuevo_valor == "":
            return True
        try:
            float(nuevo_valor)
            return True
        except ValueError:
            return False

    def leer_entry(self):
        texto = self.entry_basico.get()
        messagebox.showinfo("Contenido", f"El Entry contiene: {texto}")

    def toggle_boton(self):
        estado = self.btn_toggle['state']
        if str(estado) == 'disabled':
            self.btn_toggle.config(state='normal', bg="#4CAF50",
                                   text="Botón habilitado ✔")
            messagebox.showinfo("Estado", "Botón habilitado.")
        else:
            self.btn_toggle.config(state='disabled', bg="#9E9E9E",
                                   text="Botón deshabilitado")


if __name__ == "__main__":
    root = tk.Tk()
    app = EjemploButtonsEntries(root)
    root.mainloop()
