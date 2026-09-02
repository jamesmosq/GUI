"""
07_poo_formulario_funciones.py
──────────────────────────────
Formulario con botones y funciones — transición hacia POO
Nivel: intermedio

Muestra el estilo ANTES de POO completo:
  • Variables globales para los Entry
  • Funciones separadas (no métodos de clase)
  • Útil para comparar con el Ejercicio 3 (versión POO)

Basado en: 29.py (versión mejorada y comentada)
"""

import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("07 — Formulario con Funciones")
ventana.geometry("400x400")
ventana.configure(bg="white")
ventana.resizable(False, False)

# ── Título ────────────────────────────────────────────────────────────────────
tk.Label(ventana, text="FORMULARIO DE REGISTRO",
         font=("Arial", 15, "bold"), fg="#1F4E79", bg="white").pack(pady=20)

# ── Campos ────────────────────────────────────────────────────────────────────
for etiqueta in ["Nombre:", "Edad:", "Email:"]:
    tk.Label(ventana, text=etiqueta,
             font=("Arial", 12), bg="white").pack()
    globals()[etiqueta.replace(":", "").lower() + "_entry"] = tk.Entry(
        ventana, width=30, font=("Arial", 12), relief="solid", bd=1)
    globals()[etiqueta.replace(":", "").lower() + "_entry"].pack(pady=5)

nombre_entry = ventana.nametowidget(ventana.winfo_children()[2])
edad_entry   = ventana.winfo_children()[4]
email_entry  = ventana.winfo_children()[6]

# Forma más clara: crear los Entry directamente con nombres
ventana.winfo_children()  # limpieza conceptual

# Re-creación limpia de los campos
for w in ventana.winfo_children():
    w.destroy()

tk.Label(ventana, text="FORMULARIO DE REGISTRO",
         font=("Arial", 15, "bold"), fg="#1F4E79", bg="white").pack(pady=15)

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

# ── Funciones de los botones ──────────────────────────────────────────────────
def guardar_datos():
    """Lee los campos y muestra los datos si están completos."""
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
frame_btn.pack(pady=15)

tk.Button(frame_btn, text="Guardar",
          font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",
          width=12, command=guardar_datos).pack(side=tk.LEFT, padx=5)

tk.Button(frame_btn, text="Limpiar",
          font=("Arial", 12, "bold"), bg="#FF9800", fg="white",
          width=12, command=limpiar_campos).pack(side=tk.LEFT, padx=5)

ventana.mainloop()
