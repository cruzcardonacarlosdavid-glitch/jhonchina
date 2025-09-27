import requests
from customtkinter import *

url = "https://timeapi.io/api/time/current/zone?timeZone=America%2FGuatemala"  #Cambiamos el URL con la API que requerimos
url2 = "https://tools.aimylogic.com/api/now?tz=America/Guatemala&format=yyyy-MM-dd"
url3 = "https://catfact.ninja/facts"
ciudad = input("Ingresa tu ciudad: ")
url4 = f"http://wttr.in/{ciudad}?format=j1"
