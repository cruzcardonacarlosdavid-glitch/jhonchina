import flask
import customtkinter
from tkinter import messagebox
import requests
import datetime

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("App Informativa")
app.geometry("400x350")

API_KEY = "TU_API_KEY"
CITY = "Guatemala"
URL = f"http://wttr.in/solola?format=j1{CITY}&appid={API_KEY}&units=metric&lang=es"
data = requests.get(URL).json()

def obtener_clima():
    response = requests.get(URL)
    data = response.json()

    if "main" in data:
        temp = data["main"]["temp"]
        clima = data["weather"][0]["description"]
        viento = data["wind"]["speed"]
        return temp, clima, viento
    else:
#Mensaje de error simple si falla
         return "?", "No disponible", "?"


def actualizar_datos():
    ahora = datetime.datetime.now()
    hora = str(ahora.hour) + ":" + str(ahora.minute) + ":" + str(ahora.second)
    fecha = str(ahora.day) + "/" + str(ahora.month) + "/" + str(ahora.year)

    temp, clima, viento = obtener_clima()

    hora_label["text"] = hora
    fecha_label["text"] = fecha
    temperatura_label["text"] = "Temperatura: " + str(temp) + " °C"
    clima_label["text"] = "Clima: " + clima
    viento_label["text"] = "Viento: " + str(viento) + " m/s"

    app.after(10000, actualizar_datos)

def mostrar_alerta(mensaje):
    messagebox.showinfo("Información", mensaje)

# Widgets
hora_label = customtkinter.CTkLabel(app, text="", font=("Arial", 24))
hora_label.pack(pady=5)

fecha_label = customtkinter.CTkLabel(app, text="", font=("Arial", 18))
fecha_label.pack(pady=5)

temperatura_label = customtkinter.CTkLabel(app, text="", font=("Arial", 16))
temperatura_label.pack(pady=5)

clima_label = customtkinter.CTkLabel(app, text="", font=("Arial", 16))
clima_label.pack(pady=5)

viento_label = customtkinter.CTkLabel(app, text="", font=("Arial", 16))
viento_label.pack(pady=5)

# Mensaje del backend (dato de gato o consejo)

actualizar_datos()
app.mainloop()
