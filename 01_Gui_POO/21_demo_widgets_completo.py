"""
21_demo_widgets_completo.py
───────────────────────────
Demo completa de widgets Tkinter organizados en 4 pestañas
Tkinter intermedio · POO con clase que recibe root

Widgets incluidos:
  Pestaña 1: Label, Entry (normal y password), Button tk y ttk
  Pestaña 2: Checkbutton, Radiobutton, Combobox, Listbox
  Pestaña 3: Frame con borde, LabelFrame
  Pestaña 4: Text, ScrolledText, Scale, Progressbar, Spinbox,
             filedialog, colorchooser
"""

import tkinter as tk
from tkinter import ttk, messagebox, colorchooser, filedialog, scrolledtext


class DemoWidgets:
    def __init__(self, root):
        self.root = root
        self.root.title("21 — Demo Completa de Widgets")
        self.root.geometry("800x600")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)

        # === PESTAÑA 1: WIDGETS BÁSICOS ===
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text='  Básicos  ')

        tk.Label(self.tab1, text="Label normal").pack(pady=5)
        tk.Label(self.tab1, text="Label con color", fg="red", bg="yellow").pack(pady=5)
        tk.Label(self.tab1, text="Label con fuente", font=("Arial", 14, "bold")).pack(pady=5)

        self.entry_normal = tk.Entry(self.tab1, font=("Arial", 11))
        self.entry_normal.pack(pady=5)
        self.entry_normal.insert(0, "Entry normal")

        self.entry_pass = tk.Entry(self.tab1, show="*", font=("Arial", 11))
        self.entry_pass.pack(pady=5)
        self.entry_pass.insert(0, "contraseña")

        tk.Button(self.tab1, text="Botón tk",
                  font=("Arial", 11), bg="#4CAF50", fg="white",
                  command=self.mostrar_mensaje).pack(pady=5)
        ttk.Button(self.tab1, text="Botón ttk").pack(pady=5)

        # === PESTAÑA 2: SELECCIÓN ===
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text='  Selección  ')

        self.var_check = tk.BooleanVar()
        tk.Checkbutton(self.tab2, text="Checkbox",
                       variable=self.var_check).pack(pady=5)

        self.var_radio = tk.StringVar(value="1")
        tk.Radiobutton(self.tab2, text="Opción 1",
                       variable=self.var_radio, value="1").pack(pady=5)
        tk.Radiobutton(self.tab2, text="Opción 2",
                       variable=self.var_radio, value="2").pack(pady=5)

        self.combo = ttk.Combobox(self.tab2,
                                  values=["Opción 1", "Opción 2", "Opción 3"],
                                  state="readonly")
        self.combo.pack(pady=5)
        self.combo.set("Selecciona una opción")

        self.listbox = tk.Listbox(self.tab2, height=4, width=25)
        for item in ["Item 1", "Item 2", "Item 3", "Item 4"]:
            self.listbox.insert(tk.END, item)
        self.listbox.pack(pady=5)

        tk.Button(self.tab2, text="Ver selecciones",
                  font=("Arial", 10, "bold"), bg="#2196F3", fg="white",
                  command=self.ver_selecciones).pack(pady=8)

        # === PESTAÑA 3: CONTENEDORES ===
        self.tab3 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab3, text='  Contenedores  ')

        frame_borde = tk.Frame(self.tab3, bd=2, relief=tk.SUNKEN,
                                bg="#E3F2FD")
        frame_borde.pack(pady=10, padx=10, fill=tk.X)
        tk.Label(frame_borde, text="Frame con borde SUNKEN",
                 bg="#E3F2FD").pack(pady=10)

        label_frame = tk.LabelFrame(self.tab3, text="LabelFrame — Grupo de opciones",
                                     font=("Arial", 10, "bold"))
        label_frame.pack(pady=10, padx=10, fill=tk.X)
        tk.Button(label_frame, text="Botón 1",
                  command=lambda: messagebox.showinfo("Clic", "Botón 1")).pack(
            side=tk.LEFT, padx=5, pady=5)
        tk.Button(label_frame, text="Botón 2",
                  command=lambda: messagebox.showinfo("Clic", "Botón 2")).pack(
            side=tk.LEFT, padx=5, pady=5)

        # === PESTAÑA 4: AVANZADOS ===
        self.tab4 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab4, text='  Avanzados  ')

        self.text = tk.Text(self.tab4, height=3, width=40)
        self.text.pack(pady=5)
        self.text.insert(tk.END, "Widget Text para texto multilínea")

        self.scrolled_text = scrolledtext.ScrolledText(self.tab4, height=3, width=40)
        self.scrolled_text.pack(pady=5)
        self.scrolled_text.insert(tk.END, "ScrolledText — tiene Scrollbar integrado")

        tk.Label(self.tab4, text="Scale (deslizador):").pack()
        self.scale = tk.Scale(self.tab4, from_=0, to=100,
                              orient=tk.HORIZONTAL, length=200)
        self.scale.pack(pady=5)

        tk.Label(self.tab4, text="Progressbar:").pack()
        self.progress = ttk.Progressbar(self.tab4, length=200,
                                         mode='determinate')
        self.progress.pack(pady=5)
        self.progress['value'] = 70

        tk.Label(self.tab4, text="Spinbox (0-10):").pack()
        self.spinbox = tk.Spinbox(self.tab4, from_=0, to=10, width=5)
        self.spinbox.pack(pady=5)

        frame_dlg = tk.Frame(self.tab4)
        frame_dlg.pack(pady=5)
        tk.Button(frame_dlg, text="Abrir archivo",
                  font=("Arial", 10, "bold"), bg="#607D8B", fg="white",
                  command=self.abrir_archivo).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_dlg, text="Elegir color",
                  font=("Arial", 10, "bold"), bg="#9C27B0", fg="white",
                  command=self.elegir_color).pack(side=tk.LEFT, padx=5)

    def mostrar_mensaje(self):
        messagebox.showinfo("Mensaje", "¡Este es un mensaje de ejemplo!")

    def ver_selecciones(self):
        check = "Sí" if self.var_check.get() else "No"
        radio = self.var_radio.get()
        combo = self.combo.get()
        sel_lb = self.listbox.get(self.listbox.curselection()[0]) \
                 if self.listbox.curselection() else "Ninguno"
        messagebox.showinfo("Selecciones",
            f"Checkbox: {check}\nRadio: Opción {radio}\n"
            f"Combo: {combo}\nListbox: {sel_lb}")

    def abrir_archivo(self):
        archivo = filedialog.askopenfilename()
        if archivo:
            messagebox.showinfo("Archivo", f"Seleccionaste:\n{archivo}")

    def elegir_color(self):
        color = colorchooser.askcolor(title="Selecciona un color")
        if color[1]:
            messagebox.showinfo("Color", f"Color elegido: {color[1]}")


if __name__ == "__main__":
    root = tk.Tk()
    app = DemoWidgets(root)
    root.mainloop()
