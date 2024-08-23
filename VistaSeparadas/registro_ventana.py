import tkinter as tk
from tkinter import messagebox, Toplevel, StringVar, Checkbutton, Button, Frame, Label, Entry, Radiobutton

# Paleta de colores
COLOR_FONDO = "#F0F0F0"
COLOR_BOTON = "#1E90FF"
COLOR_TEXTO = "#000000"
COLOR_BOTON_TEXTO = "#FFFFFF"

class RegistroVentana:
    def __init__(self, primera_vista):
        self.primera_vista = primera_vista
        self.ventana_registro = Toplevel(primera_vista.root)
        self.ventana_registro.title("¡REGÍSTRATE AHORA!")
        self.ventana_registro.geometry("800x600")
        self.ventana_registro.resizable(True, True)
        self.registro_frame = Frame(self.ventana_registro, bg=COLOR_FONDO)
        self.registro_frame.pack(expand=True, fill='both')
        self.crear_widgets()
        self.ventana_registro.protocol("WM_DELETE_WINDOW", self.on_close)

    def crear_widgets(self):
        # Marco principal con cuadrícula para dividir la ventana en 4 partes
        top_frame = Frame(self.registro_frame, bg=COLOR_FONDO)
        top_frame.pack(side=tk.TOP, fill='x', expand=True, padx=10, pady=10)

        bottom_frame = Frame(self.registro_frame, bg=COLOR_FONDO)
        bottom_frame.pack(side=tk.BOTTOM, fill='x', expand=False, padx=10, pady=10)

        # Sección de información personal (superior izquierda)
        left_frame = Frame(top_frame, bg=COLOR_FONDO)
        left_frame.pack(side=tk.LEFT, fill='y', expand=True, padx=10, pady=10)

        tk.Label(left_frame, text="Nombre:", bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=0, column=0, sticky="w")
        self.nombre_entry = Entry(left_frame, bg=COLOR_FONDO, fg=COLOR_TEXTO)
        self.nombre_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        tk.Label(left_frame, text="Apellido:", bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=1, column=0, sticky="w")
        self.apellido_entry = Entry(left_frame, bg=COLOR_FONDO, fg=COLOR_TEXTO)
        self.apellido_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        tk.Label(left_frame, text="Sexo:", bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=2, column=0, sticky="w")
        self.sexo_var = StringVar(value="Masculino")
        Radiobutton(left_frame, text="Masculino", variable=self.sexo_var, value="Masculino", bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=2, column=1, padx=5, pady=5, sticky="w")
        Radiobutton(left_frame, text="Femenino", variable=self.sexo_var, value="Femenino", bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=2, column=2, padx=5, pady=5, sticky="w")

        tk.Label(left_frame, text="Fecha de Nacimiento:", bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=3, column=0, sticky="w")
        fecha_frame = Frame(left_frame, bg=COLOR_FONDO)
        fecha_frame.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
        tk.Label(fecha_frame, text="DD", bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=0, column=0, padx=2, pady=2, sticky="w")
        self.dia_entry = Entry(fecha_frame, bg=COLOR_FONDO, fg=COLOR_TEXTO, width=5)
        self.dia_entry.grid(row=0, column=1, padx=2, pady=2, sticky="w")
        tk.Label(fecha_frame, text="MM", bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=0, column=2, padx=2, pady=2, sticky="w")
        self.mes_entry = Entry(fecha_frame, bg=COLOR_FONDO, fg=COLOR_TEXTO, width=5)
        self.mes_entry.grid(row=0, column=3, padx=2, pady=2, sticky="w")
        tk.Label(fecha_frame, text="AAAA", bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=0, column=4, padx=2, pady=2, sticky="w")
        self.anio_entry = Entry(fecha_frame, bg=COLOR_FONDO, fg=COLOR_TEXTO, width=10)
        self.anio_entry.grid(row=0, column=5, padx=2, pady=2, sticky="w")

        tk.Label(left_frame, text="Cédula:", bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=4, column=0, sticky="w")
        self.cedula_entry = Entry(left_frame, bg=COLOR_FONDO, fg=COLOR_TEXTO)
        self.cedula_entry.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

        # Sección de datos de registro (superior derecha)
        right_frame = Frame(top_frame, bg=COLOR_FONDO)
        right_frame.pack(side=tk.RIGHT, fill='y', expand=True, padx=10, pady=10)

        tk.Label(right_frame, text="Correo Electrónico:", bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=0, column=0, sticky="w")
        self.email_entry = Entry(right_frame, bg=COLOR_FONDO, fg=COLOR_TEXTO)
        self.email_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        tk.Label(right_frame, text="Contraseña:", bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=1, column=0, sticky="w")
        self.contrasena_entry = Entry(right_frame, show="*", bg=COLOR_FONDO, fg=COLOR_TEXTO)
        self.contrasena_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        tk.Label(right_frame, text="Confirmar Contraseña:", bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=2, column=0, sticky="w")
        self.confirmar_contrasena_entry = Entry(right_frame, show="*", bg=COLOR_FONDO, fg=COLOR_TEXTO)
        self.confirmar_contrasena_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        self.mostrar_contrasena_var = tk.BooleanVar()
        self.mostrar_contrasena_check = Checkbutton(right_frame, text="Mostrar Contraseña", variable=self.mostrar_contrasena_var, bg=COLOR_FONDO, fg=COLOR_TEXTO, command=self.toggle_password_visibility)
        self.mostrar_contrasena_check.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        tk.Label(right_frame, text="Rol:", bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=4, column=0, sticky="w")
        self.rol_var = StringVar(value="Usuario")
        Radiobutton(right_frame, text="Usuario", variable=self.rol_var, value="Usuario", bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=4, column=1, padx=5, pady=5, sticky="w")
        Radiobutton(right_frame, text="Admin", variable=self.rol_var, value="Admin", bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=4, column=2, padx=5, pady=5, sticky="w")

        # Parte Inferior
        terms_checkbox_frame = Frame(bottom_frame, bg=COLOR_FONDO)
        terms_checkbox_frame.pack(side=tk.TOP, fill='x', pady=10)

        self.terms_var = tk.BooleanVar()
        self.terms_checkbox = Checkbutton(terms_checkbox_frame, text="Acepto los términos y condiciones", variable=self.terms_var, bg=COLOR_FONDO, fg=COLOR_TEXTO, command=self.abrir_terminos)
        self.terms_checkbox.pack()

        buttons_frame = Frame(bottom_frame, bg=COLOR_FONDO)
        buttons_frame.pack(side=tk.BOTTOM, fill='x', pady=10)

        self.aceptar_boton = Button(buttons_frame, text="Aceptar", command=self.aceptar, bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO)
        self.aceptar_boton.pack(side=tk.LEFT, padx=5)
        self.cancelar_boton = Button(buttons_frame, text="Cancelar", command=self.cancelar, bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO)
        self.cancelar_boton.pack(side=tk.RIGHT, padx=5)

    def toggle_password_visibility(self):
        if self.mostrar_contrasena_var.get():
            self.contrasena_entry.config(show="")
            self.confirmar_contrasena_entry.config(show="")
        else:
            self.contrasena_entry.config(show="*")
            self.confirmar_contrasena_entry.config(show="*")

    def abrir_terminos(self):
        # Abre una ventana emergente con los términos y condiciones
        terms_window = Toplevel(self.ventana_registro)
        terms_window.title("Términos y Condiciones")
        terms_window.geometry("400x300")
        terms_window.resizable(True, True)
        terms_text = """Aquí van los términos y condiciones..."""
        text_widget = tk.Text(terms_window, wrap=tk.WORD, padx=10, pady=10)
        text_widget.insert(tk.END, terms_text)
        text_widget.config(state=tk.DISABLED)
        text_widget.pack(expand=True, fill='both')

    def aceptar(self):
        if not self.terms_var.get():
            messagebox.showerror("Error", "Debes aceptar los términos y condiciones.")
            return

        email = self.email_entry.get()
        contrasena = self.contrasena_entry.get()
        confirmar_contrasena = self.confirmar_contrasena_entry.get()
        nombre = self.nombre_entry.get()
        barrio = self.barrio_entry.get()

        if contrasena != confirmar_contrasena:
            messagebox.showerror("Error", "Las contraseñas no coinciden.")
            return

        if email in self.primera_vista.usuarios:
            messagebox.showerror("Error", "El correo electrónico ya está registrado.")
            return

        self.primera_vista.registrar_usuario(email, contrasena, nombre, barrio)
        self.primera_vista.mostrar_ventana_principal()
        self.ventana_registro.destroy()

    def cancelar(self):
        self.ventana_registro.destroy()

    def on_close(self):
        self.ventana_registro.destroy()
