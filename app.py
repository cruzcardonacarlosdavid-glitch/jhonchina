#abner esta es tu rama
#Oh ciedos

import customtkinter
from tkinter import messagebox
import requests
import datetime
import time

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("App del Tiempo y Clima")
app.geometry("500x450")

CITY = "Guatemala"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}"

def Weather():
    response = requests.get(URL)
    data = response.json()
    temp = data["main"]["temp"]
    clima = data["weather"][0]["description"]
    viento = data["wind"]["speed"]
    return temp, clima, viento

def actualizar_datos():
    ahora = datetime.datetime.now()
    hora_texto = str(ahora.hour) + ":" + str(ahora.minute) + ":" + str(ahora.second)
    fecha_texto = str(ahora.day) + "/" + str(ahora.month) + "/" + str(ahora.year)

    temp, clima, viento = obtener_clima()

    hora_label["text"] = hora_texto
    fecha_label["text"] = fecha_texto
    temperatura_label["text"] = "Temperatura: " + str(temp) + " °C"
    clima_label["text"] = "Clima: " + clima
    viento_label["text"] = "Viento: " + str(viento) + " m/s"

app.after(10000, actualizar_datos)

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


actualizar_datos()
app.mainloop()


#4 etiquetas y una caja, señal de alerta