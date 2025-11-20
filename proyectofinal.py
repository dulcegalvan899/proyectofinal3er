#Proyecto Final
#Submodulo
#Autores: Galavan Dulce Guevara Kelly

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk  # Necesita instalar pillow: pip install pillow
import os

# -------------------------
# FUNCIONES (pantallas vacías por ahora)
# -------------------------
def abrir_registro_productos():
    messagebox.showinfo("Registro de Productos", "Aquí irá el módulo de registro de productos.")

def abrir_registro_ventas():
    messagebox.showinfo("Registro de Ventas", "Aquí irá el módulo de registro de ventas.")

def abrir_reportes():
    messagebox.showinfo("Reportes", "Aquí irá el módulo de reportes.")

def abrir_acerca_de():
    messagebox.showinfo("Acerca de", "Punto de Venta de Ropa\nProyecto Escolar\nVersión 1.0")

# -------------------------
# VENTANA PRINCIPAL
# -------------------------
ventana = tk.Tk()
ventana.title("Fashion D&K&L 1.0")
ventana.geometry("500x600")
ventana.resizable(False, False)
ventana.configure(bg="#ddcbd7")

# -------------------------
# LOGO
# -------------------------
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    imagen = Image.open(os.path.join(BASE_DIR,"ventas2025.png"))  # Cambia por el archivo del alumno
    imagen = imagen.resize((250, 250))  # Tamaño recomendado
    img_logo = ImageTk.PhotoImage(imagen)

    lbl_logo = tk.Label(ventana, image=img_logo)
    lbl_logo.pack(pady=20)
except:
    lbl_sin_logo = tk.Label(ventana, text="(Aquí va el logo del sistema)", font=("Arial", 14), fg="black")
    lbl_sin_logo.pack(pady=40)

# -------------------------
# BOTONES PRINCIPALES
# -------------------------
estilo = ttk.Style()
estilo.configure("TButton", 
                 font=("Arial", 12),  # Fuente de 12 puntos
                 padding=10, 
                 background="#f79df7",  # Color morado
                 foreground="black",  # Texto negro
                 relief="flat")  # Sin bordes elevados

btn_reg_prod = ttk.Button(ventana, text="Registro de Productos", command=abrir_registro_productos)
btn_reg_prod.pack(pady=10)

btn_reg_ventas = ttk.Button(ventana, text="Registro de Ventas", command=abrir_registro_ventas)
btn_reg_ventas.pack(pady=10)

btn_reportes = ttk.Button(ventana, text="Reportes", command=abrir_reportes)
btn_reportes.pack(pady=10)

btn_acerca = ttk.Button(ventana, text="Acerca de", command=abrir_acerca_de)
btn_acerca.pack(pady=10)

ventana.mainloop()
