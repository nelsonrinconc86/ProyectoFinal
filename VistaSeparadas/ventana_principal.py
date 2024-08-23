import tkinter as tk

class VentanaPrincipal:
    def __init__(self, usuario):
        self.usuario = usuario

    def mostrar(self):
        ventana_principal = tk.Toplevel()
        ventana_principal.title("Ventana Principal")
        ventana_principal.geometry("800x600")
        ventana_principal.resizable(True, True)
        tk.Label(ventana_principal, text=f"Bienvenido, {self.usuario['nombre']}!", font=("Arial", 16)).pack(pady=20)
