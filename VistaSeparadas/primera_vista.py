import tkinter as tk
from tkinter import messagebox
from registro_ventana import RegistroVentana
from login_ventana import LoginVentana
from ventana_principal import VentanaPrincipal

# Paleta de colores
COLOR_FONDO = "#C0C0C0"  # PLATEADO
COLOR_BOTON = "#1E90FF"  # Azul neón
COLOR_BOTON_PRESIONADO = "#000000"  # Negro
COLOR_TEXTO = "#000000"  # Negro
COLOR_BOTON_TEXTO = "#FFFFFF"  # Blanco

class PrimeraVista:
    def __init__(self, root):
        self.root = root
        self.root.title("PROYECTO KOAJ")
        self.root.geometry("900x720")
        self.root.resizable(True, True)
        self.usuarios = {}  # Almacena los datos de usuarios en un diccionario
        self.ventana_registro = None
        self.ventana_login = None
        self.ventana_principal = None
        self.usuario_actual = None  # Guardará el usuario actualmente registrado
        self.crear_encabezado()

    def crear_encabezado(self):
        self.encabezado_frame = tk.Frame(self.root, bg=COLOR_FONDO, padx=10, pady=5)
        self.encabezado_frame.pack(fill=tk.X)
        self.secciones = [tk.Frame(self.encabezado_frame, bg=COLOR_FONDO, padx=10, pady=5) for _ in range(10)]

        for i, seccion in enumerate(self.secciones):
            seccion.grid(row=0, column=i, sticky="ew")

        tk.Label(self.secciones[0], text="Logo", bg=COLOR_FONDO).pack()
        tk.Label(self.secciones[3], text="K", bg=COLOR_FONDO, fg=COLOR_TEXTO).pack()
        tk.Label(self.secciones[4], text="O", bg=COLOR_FONDO, fg=COLOR_TEXTO).pack()
        tk.Label(self.secciones[5], text="A", bg=COLOR_FONDO, fg=COLOR_TEXTO).pack()
        tk.Label(self.secciones[6], text="J", bg=COLOR_FONDO, fg=COLOR_TEXTO).pack()
        tk.Button(self.secciones[8], text="REGISTRARSE", command=self.mostrar_registro, bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO).pack()
        tk.Button(self.secciones[9], text="INICIAR SESIÓN", command=self.iniciar_sesion, bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO).pack()

        for i in range(10):
            self.encabezado_frame.columnconfigure(i, weight=1)

    def iniciar_sesion(self):
        if self.ventana_login:
            self.ventana_login.destroy()
        self.ventana_login = LoginVentana(self)

    def mostrar_registro(self):
        if self.ventana_registro:
            self.ventana_registro.destroy()
        self.ventana_registro = RegistroVentana(self)

    def mostrar_ventana_principal(self):
        if self.ventana_principal:
            self.ventana_principal.destroy()
        self.ventana_principal = VentanaPrincipal(self.usuario_actual)
        self.ventana_principal.mostrar()

    def registrar_usuario(self, email, contrasena, nombre, barrio):
        self.usuarios[email] = {'contrasena': contrasena, 'nombre': nombre, 'barrio': barrio}
        self.usuario_actual = {'email': email, 'nombre': nombre, 'barrio': barrio}

    def change_button_color(self, event):
        button = event.widget
        button.config(bg=COLOR_BOTON_PRESIONADO, fg=COLOR_BOTON_TEXTO)
