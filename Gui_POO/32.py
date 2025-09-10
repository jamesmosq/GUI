# Formulario con grid layout en Tkinter
import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario con Grid")
ventana.geometry("500x400")
ventana.configure(bg='white', padx=20, pady=20)

# Título - ocupa toda la fila
titulo = tk.Label(ventana,
                  text="FORMULARIO DE REGISTRO",
                  font=("Arial", 18, "bold"),
                  fg="darkblue",
                  bg="white")
titulo.grid(row=0, column=0, columnspan=2, pady=(0, 30))

# CAMPOS DEL FORMULARIO usando grid()
# Fila 1: Nombre
tk.Label(ventana, text="Nombre:", font=("Arial", 12), bg="white").grid(row=1, column=0, sticky="e", padx=(0, 10),
                                                                       pady=10)
nombre_entry = tk.Entry(ventana, width=25, font=("Arial", 12), relief="solid", bd=1)
nombre_entry.grid(row=1, column=1, pady=10)

# Fila 2: Apellido
tk.Label(ventana, text="Apellido:", font=("Arial", 12), bg="white").grid(row=2, column=0, sticky="e", padx=(0, 10),
                                                                         pady=10)
apellido_entry = tk.Entry(ventana, width=25, font=("Arial", 12), relief="solid", bd=1)
apellido_entry.grid(row=2, column=1, pady=10)

# Fila 3: Edad
tk.Label(ventana, text="Edad:", font=("Arial", 12), bg="white").grid(row=3, column=0, sticky="e", padx=(0, 10), pady=10)
edad_entry = tk.Entry(ventana, width=25, font=("Arial", 12), relief="solid", bd=1)
edad_entry.grid(row=3, column=1, pady=10)

# Fila 4: Email
tk.Label(ventana, text="Email:", font=("Arial", 12), bg="white").grid(row=4, column=0, sticky="e", padx=(0, 10),
                                                                      pady=10)
email_entry = tk.Entry(ventana, width=25, font=("Arial", 12), relief="solid", bd=1)
email_entry.grid(row=4, column=1, pady=10)

# Fila 5: Teléfono
tk.Label(ventana, text="Teléfono:", font=("Arial", 12), bg="white").grid(row=5, column=0, sticky="e", padx=(0, 10),
                                                                         pady=10)
telefono_entry = tk.Entry(ventana, width=25, font=("Arial", 12), relief="solid", bd=1)
telefono_entry.grid(row=5, column=1, pady=10)


# FUNCIONES
def guardar_datos():
    datos = {
        'nombre': nombre_entry.get(),
        'apellido': apellido_entry.get(),
        'edad': edad_entry.get(),
        'email': email_entry.get(),
        'telefono': telefono_entry.get()
    }

    # Verificar campos vacíos
    campos_vacios = [campo for campo, valor in datos.items() if not valor.strip()]

    if campos_vacios:
        messagebox.showerror("Error", f"Completa estos campos: {', '.join(campos_vacios)}")
    else:
        mensaje = "DATOS GUARDADOS:\n\n"
        for campo, valor in datos.items():
            mensaje += f"{campo.capitalize()}: {valor}\n"
        messagebox.showinfo("Éxito", mensaje)


def limpiar_campos():
    for entry in [nombre_entry, apellido_entry, edad_entry, email_entry, telefono_entry]:
        entry.delete(0, tk.END)
    messagebox.showinfo("Info", "Formulario limpiado")


# BOTONES - Fila 6
frame_botones = tk.Frame(ventana, bg="white")
frame_botones.grid(row=6, column=0, columnspan=2, pady=(30, 0))

btn_guardar = tk.Button(frame_botones,
                        text="GUARDAR",
                        command=guardar_datos,
                        bg="darkgreen",
                        fg="white",
                        font=("Arial", 12, "bold"),
                        width=12,
                        cursor="hand2")
btn_guardar.pack(side="left", padx=10)

btn_limpiar = tk.Button(frame_botones,
                        text="LIMPIAR",
                        command=limpiar_campos,
                        bg="darkorange",
                        fg="white",
                        font=("Arial", 12, "bold"),
                        width=12,
                        cursor="hand2")
btn_limpiar.pack(side="left", padx=10)

ventana.mainloop()

# EXPLICACIÓN DE GRID:
# - grid(row=, column=) posiciona elementos en filas y columnas
# - columnspan= hace que un elemento ocupe varias columnas
# - sticky="e" alinea a la derecha (east), "w"=izquierda, "n"=arriba, "s"=abajo
# - padx= espacio horizontal, pady= espacio vertical
# - Frame() crea un contenedor para agrupar elementos
# - cursor="hand2" cambia el cursr cuando pasas sobre el botón