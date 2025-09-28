import customtkinter
from tkinter import messagebox
import requests
from requests import *
from flask import *
import datetime

#Configuración 
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("App Informativa")
app.geometry("400x350")

#API del clima
CITY = "Guatemala"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}"

#Funciones
def obtener_clima():
    try:
        response = requests.get(URL)
        data = response.json()
        temp = data["main"]["temp"]
        clima = data["weather"][0]["description"]
        viento = data["wind"]["speed"]
        return temp, clima, viento
    except:
        return "?", "No disponible", "?"

def actualizar_datos():
    ahora = datetime.datetime.now()
    hora_label.configure(text=ahora.strftime("%H:%M:%S"))
    fecha_label.configure(text=ahora.strftime("%d/%m/%Y"))

    temp, clima, viento = obtener_clima()
    temperatura_label.configure(text=f" {temp} °C")
    clima_label.configure(text=f" {clima}")
    viento_label.configure(text=f" {viento} m/s")

#Para que actualice cada cierto tiempo.
    app.after(10000, actualizar_datos)

#Una funcion de boton.
def mostrar_alerta(mensaje):
    """Recibe el mensaje desde el backend"""
    messagebox.showinfo("Información", mensaje)

#Los botoncitos
hora_label = customtkinter.CTkLabel(app, text="", font=("Arial", 24))
hora_label.pack(pady=10)

fecha_label = customtkinter.CTkLabel(app, text="", font=("Arial", 18))
fecha_label.pack(pady=5)

temperatura_label = customtkinter.CTkLabel(app, text="", font=("Arial", 16))
temperatura_label.pack(pady=5)

clima_label = customtkinter.CTkLabel(app, text="", font=("Arial", 16))
clima_label.pack(pady=5)

viento_label = customtkinter.CTkLabel(app, text="", font=("Arial", 16))
viento_label.pack(pady=5)

#Las alertas.
btn = customtkinter.CTkButton(app, text="Mostrar alerta", command=lambda: mostrar_alerta("Consejos"))
btn.pack(pady=15)

#Ejecutar.
actualizar_datos()
app.mainloop()


