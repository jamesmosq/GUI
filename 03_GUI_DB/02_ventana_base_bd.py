"""
02_ventana_base_bd.py
─────────────────────
Ventana base para apps con BD — estructura mínima
Tkinter + MySQL · GUI carpeta

Muestra la estructura base que se repite en todos los archivos
de esta carpeta: ventana + conexión + acción básica.

Antes de conectar a BD, siempre:
  1. Importar mysql.connector
  2. Definir DB_CONFIG con las credenciales
  3. Crear el objeto de conexión
  4. Llamar connect() antes de operar
  5. Llamar disconnect() al cerrar
"""

import tkinter as tk
from tkinter import messagebox
import mysql.connector

# ── Configuración de conexión ─────────────────────────────────────────────────
DB_CONFIG = {
    "host":     "localhost",
    "user":     "root",
    "password": "",          # ← tu contraseña de MySQL
    "database": "Northwind"
}

connection = None

def conectar():
    global connection
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        lbl_estado.config(text="Estado: ✔ Conectado", fg="#4CAF50")
        messagebox.showinfo("Conexión", "Conexión establecida correctamente.")
        btn_conectar.config(state="disabled")
        btn_desconectar.config(state="normal")
        btn_probar.config(state="normal")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"No se pudo conectar:\n{e}")

def desconectar():
    global connection
    if connection:
        connection.close()
        connection = None
    lbl_estado.config(text="Estado: ✗ Desconectado", fg="#f44336")
    messagebox.showinfo("Desconectado", "Conexión cerrada correctamente.")
    btn_conectar.config(state="normal")
    btn_desconectar.config(state="disabled")
    btn_probar.config(state="disabled")

def probar_consulta():
    """Ejecuta una consulta simple para verificar la conexión."""
    if not connection:
        messagebox.showwarning("Sin conexión", "Primero conecta a la base de datos.")
        return
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM Employees")
        total = cursor.fetchone()[0]
        cursor.close()
        messagebox.showinfo("Consulta OK", f"La BD responde correctamente.\nTotal empleados: {total}")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error en la consulta:\n{e}")

def cerrar():
    desconectar()
    root.destroy()

# ── Ventana principal ─────────────────────────────────────────────────────────
root = tk.Tk()
root.title("02 — Ventana Base con BD")
root.geometry("400x320")
root.configure(bg="white")
root.resizable(False, False)

tk.Label(root, text="Estructura Base — App con MySQL",
         font=("Arial", 13, "bold"), fg="#1F4E79", bg="white").pack(pady=15)

tk.Label(root,
         text=f"Host: {DB_CONFIG['host']}  |  BD: {DB_CONFIG['database']}",
         font=("Arial", 10), fg="gray", bg="white").pack()

lbl_estado = tk.Label(root, text="Estado: ✗ Desconectado",
                       font=("Arial", 11, "bold"), fg="#f44336", bg="white")
lbl_estado.pack(pady=10)

frame_btn = tk.Frame(root, bg="white")
frame_btn.pack(pady=5)

btn_conectar = tk.Button(frame_btn, text="Conectar",
                          font=("Arial", 11, "bold"), bg="#4CAF50", fg="white",
                          width=14, command=conectar)
btn_conectar.pack(pady=5)

btn_probar = tk.Button(frame_btn, text="Probar consulta",
                        font=("Arial", 11, "bold"), bg="#2196F3", fg="white",
                        width=14, state="disabled", command=probar_consulta)
btn_probar.pack(pady=5)

btn_desconectar = tk.Button(frame_btn, text="Desconectar",
                             font=("Arial", 11, "bold"), bg="#FF9800", fg="white",
                             width=14, state="disabled", command=desconectar)
btn_desconectar.pack(pady=5)

tk.Button(frame_btn, text="Cerrar app",
          font=("Arial", 11, "bold"), bg="#f44336", fg="white",
          width=14, command=cerrar).pack(pady=5)

root.protocol("WM_DELETE_WINDOW", cerrar)
root.mainloop()
