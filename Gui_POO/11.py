#11. Cuadro combinado (Combobox)
from tkinter import Tk
from tkinter.ttk import Combobox
root = Tk()
root.geometry('400x300')
combo = Combobox(root, values=["Opción 1", "Opción 2", "Opción 3","Opción 4"])
combo.pack()
root.mainloop()  # Inicia el bucle de eventos de la ventana
