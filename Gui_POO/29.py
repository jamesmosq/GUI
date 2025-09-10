#BOTONES Y FUNCIONES
import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Probando ....")
ventana.geometry("400x450")
ventana.configure(bg='white')

# Título
titulo = tk.Label(ventana,
                  text="FORMULARIO DE REGISTRO",
                  font=("Arial", 16, "bold"),
                  fg="blue",
                  bg="white")
titulo.pack(pady=20)

# Campo Nombre
nombre_label = tk.Label(ventana, text="Nombre:", font=("Arial", 12), bg="white")
nombre_label.pack()
nombre_entry = tk.Entry(ventana, width=30, font=("Arial", 12), relief="solid", bd=1)
nombre_entry.pack(pady=5)

# Campo Edad
edad_label = tk.Label(ventana, text="Edad:", font=("Arial", 12), bg="white")
edad_label.pack()
edad_entry = tk.Entry(ventana, width=30, font=("Arial", 12), relief="solid", bd=1)
edad_entry.pack(pady=5)

# Campo Email
email_label = tk.Label(ventana, text="Email:", font=("Arial", 12), bg="white")
email_label.pack()
email_entry = tk.Entry(ventana, width=30, font=("Arial", 12), relief="solid", bd=1)
email_entry.pack(pady=5)


# FUNCIONES PARA LOS BOTONES
def guardar_datos():
    """Función que se ejecuta al presionar 'Guardar'"""
    nombre = nombre_entry.get()  # Obtener texto del campo
    edad = edad_entry.get()
    email = email_entry.get()

    # Validar que no estén vacíos
    if nombre and edad and email:
        mensaje = f"Datos guardados:\nNombre: {nombre}\nEdad: {edad}\nEmail: {email}"
        messagebox.showinfo("Éxito", mensaje)
    else:
        messagebox.showerror("Error", "Por favor completa todos los campos")


def limpiar_campos():
    """Función que limpia todos los campos"""
    nombre_entry.delete(0, tk.END)  # Borrar desde posición 0 hasta el final
    edad_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    messagebox.showinfo("Info", "Campos limpiados")


# BOTONES
btn_guardar = tk.Button(ventana,
                        text="GUARDAR",
                        command=guardar_datos,  # Función a ejecutar
                        bg="green",
                        fg="white",
                        font=("Arial", 12, "bold"),
                        width=15)
btn_guardar.pack(pady=10)

btn_limpiar = tk.Button(ventana,
                        text="LIMPIAR",
                        command=limpiar_campos,
                        bg="orange",
                        fg="white",
                        font=("Arial", 12, "bold"),
                        width=15)
btn_limpiar.pack(pady=5)

ventana.mainloop()

#Notas:
# - Button() crea un botón clickeable
# - command= especifica qué función ejecutar al hacer click
# - .get() obtiene el texto de un Entry
# - .delete(inicio, fin) borra texto de un Entry
# - messagebox.showinfo() muestra ventanas de mensaje
# - tk. END representa la posición final del texto