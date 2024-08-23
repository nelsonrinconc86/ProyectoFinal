import tkinter as tk
from tkinter import messagebox

# Paleta de colores
COLOR_FONDO = "#F0F0F0"
COLOR_BOTON = "#1E90FF"
COLOR_TEXTO = "#000000"
COLOR_BOTON_TEXTO = "#FFFFFF"

class LoginVentana:
    def __init__(self, primera_vista):
        self.primera_vista = primera_vista
        self.ventana_login = tk.Toplevel(primera_vista.root)
        self.ventana_login.title("Iniciar Sesión")
        self.ventana_login.geometry("400x300")
        self.ventana_login.resizable(False, False)
        self.login_frame = tk.Frame(self.ventana_login, bg=COLOR_FONDO)
        self.login_frame.pack(expand=True, fill='both')
        self.crear_widgets()
        self.ventana_login.protocol("WM_DELETE_WINDOW", self.on_close)

    def crear_widgets(self):
        tk.Label(self.login_frame, text="Correo Electrónico:", bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=10)
        self.email_entry = tk.Entry(self.login_frame, bg=COLOR_FONDO, fg=COLOR_TEXTO)
        self.email_entry.pack(pady=5)

        tk.Label(self.login_frame, text="Contraseña:", bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=10)
        self.contrasena_entry = tk.Entry(self.login_frame, show="*", bg=COLOR_FONDO, fg=COLOR_TEXTO)
        self.contrasena_entry.pack(pady=5)

        self.boton_frame = tk.Frame(self.login_frame, bg=COLOR_FONDO)
        self.boton_frame.pack(pady=20)

        self.login_boton = tk.Button(self.boton_frame, text="Iniciar Sesión", command=self.iniciar_sesion, bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO)
        self.login_boton.pack(side=tk.LEFT, padx=5)
        self.cancelar_boton = tk.Button(self.boton_frame, text="Cancelar", command=self.cancelar, bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO)
        self.cancelar_boton.pack(side=tk.RIGHT, padx=5)

    def iniciar_sesion(self):
        email = self.email_entry.get()
        contrasena = self.contrasena_entry.get()

        if email in self.primera_vista.usuarios:
            if self.primera_vista.usuarios[email]['contrasena'] == contrasena:
                self.primera_vista.usuario_actual = {'email': email, 'nombre': self.primera_vista.usuarios[email]['nombre'], 'barrio': self.primera_vista.usuarios[email]['barrio']}
                self.primera_vista.mostrar_ventana_principal()
                self.ventana_login.destroy()
            else:
                messagebox.showerror("Error", "Contraseña incorrecta.")
        else:
            messagebox.showerror("Error", "El correo electrónico no está registrado.")

    def cancelar(self):
        self.ventana_login.destroy()

    def on_close(self):
        self.ventana_login.destroy()
