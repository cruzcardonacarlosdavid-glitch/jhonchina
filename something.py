import customtkinter
from tkinter import messagebox

import datetime

import requests


# Configuración de la app
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("App Informativa")
app.geometry("400x300")

# API del clima
CITY = "Guatemala"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid"
data = requests.get(URL).json()


# Función para obtener el clima
def obtener_clima():

    temp = data["main"]["temp"]
    clima = data["weather"][0]["description"]
    viento = data["wind"]["speed"]
    return temp, clima, viento


# Función para actualizar los datos en pantalla
def actualizar_datos():
    ahora = datetime.datetime.now()
    hora_texto = str(ahora.hour) + ":" + str(ahora.minute) + ":" + str(ahora.second)
    fecha_texto = str(ahora.day) + "/" + str(ahora.month) + "/" + str(ahora.year)

    temp = obtener_clima()
    clima = obtener_clima()
    viento = obtener_clima()

    hora_lbl["text"] = hora_texto
    fecha_lbl["text"] = fecha_texto
    temperatura_lbl["text"] = "Temperatura: " + str(temp) + " °C"
    clima_lbl["text"] = "Clima: " + clima
    viento_lbl["text"] = "Viento: " + str(viento) + " m/s"

    app.after(10000, actualizar_datos)  # Actualiza cada 10 segundos


# Función para el botón (el mensaje viene del backend)
def mostrar_alerta(mensaje):
    messagebox.showinfo("Información", mensaje)


# Widgets
hora_lbl = customtkinter.CTkLabel(app, text="", font=("Arial", 24))
hora_lbl.pack(pady=5)

fecha_lbl = customtkinter.CTkLabel(app, text="", font=("Arial", 18))
fecha_lbl.pack(pady=5)

temperatura_lbl = customtkinter.CTkLabel(app, text="", font=("Arial", 16))
temperatura_lbl.pack(pady=5)

clima_lbl = customtkinter.CTkLabel(app, text="", font=("Arial", 16))
clima_lbl.pack(pady=5)

viento_lbl = customtkinter.CTkLabel(app, text="", font=("Arial", 16))
viento_lbl.pack(pady=5)

btn = customtkinter.CTkButton(app, text="Mostrar alerta", command=lambda: mostrar_alerta("Este mensaje viene del backend"))
btn.pack(pady=10)

# Ejecutar
actualizar_datos()
app.mainloop()
