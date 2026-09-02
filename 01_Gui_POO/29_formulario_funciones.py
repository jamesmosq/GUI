"""
29_formulario_funciones.py
──────────────────────────
Formulario con funciones sueltas — transición hacia POO
Tkinter POO — nivel de transición

Muestra el estilo ANTES de POO completo:
  - Variables globales para los Entry
  - Funciones fuera de una clase (no métodos)

Compara este archivo con 28 (clase con root) y con
los ejercicios guiados (clase que hereda de tk.Tk).
"""

import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("29 — Formulario con Funciones")
ventana.geometry("400x420")
ventana.configure(bg='white')
ventana.resizable(False, False)

# ── Título ────────────────────────────────────────────────────────────────────
tk.Label(ventana,
         text="FORMULARIO DE REGISTRO",
         font=("Arial", 15, "bold"),
         fg="#1F4E79",
         bg="white").pack(pady=20)

# ── Campos ────────────────────────────────────────────────────────────────────
tk.Label(ventana, text="Nombre:", font=("Arial", 12), bg="white").pack()
nombre_entry = tk.Entry(ventana, width=30, font=("Arial", 12),
                        relief="solid", bd=1)
nombre_entry.pack(pady=5)

tk.Label(ventana, text="Edad:", font=("Arial", 12), bg="white").pack()
edad_entry = tk.Entry(ventana, width=30, font=("Arial", 12),
                      relief="solid", bd=1)
edad_entry.pack(pady=5)

tk.Label(ventana, text="Email:", font=("Arial", 12), bg="white").pack()
email_entry = tk.Entry(ventana, width=30, font=("Arial", 12),
                       relief="solid", bd=1)
email_entry.pack(pady=5)


# ── Funciones (equivalente a métodos, pero sueltas) ───────────────────────────
def guardar_datos():
    """Valida y muestra los datos del formulario."""
    nombre = nombre_entry.get().strip()
    edad   = edad_entry.get().strip()
    email  = email_entry.get().strip()

    if not all([nombre, edad, email]):
        messagebox.showerror("Error", "Por favor completa todos los campos.")
        return

    if not edad.isdigit():
        messagebox.showerror("Error", "La edad debe ser un número.")
        return

    messagebox.showinfo("Éxito",
        f"Datos guardados:\nNombre: {nombre}\nEdad: {edad}\nEmail: {email}")


def limpiar_campos():
    """Borra el contenido de todos los Entry."""
    nombre_entry.delete(0, tk.END)
    edad_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    messagebox.showinfo("Limpiar", "Campos limpiados correctamente.")


# ── Botones ───────────────────────────────────────────────────────────────────
frame_btn = tk.Frame(ventana, bg="white")
frame_btn.pack(pady=20)

tk.Button(frame_btn, text="Guardar",
          font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",
          width=12, command=guardar_datos).pack(side=tk.LEFT, padx=5)

tk.Button(frame_btn, text="Limpiar",
          font=("Arial", 12, "bold"), bg="#FF9800", fg="white",
          width=12, command=limpiar_campos).pack(side=tk.LEFT, padx=5)

# ── Notas pedagógicas ─────────────────────────────────────────────────────────
# Button()  → crea un botón clickeable
# command=  → función que se ejecuta al hacer clic
# .get()    → obtiene el texto de un Entry
# .delete(inicio, fin) → borra texto de un Entry
# messagebox.showinfo() → muestra ventana de mensaje
# tk.END    → representa el final del texto

ventana.mainloop()
