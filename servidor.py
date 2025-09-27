import requests

#api del tiempo
url = "https://timeapi.io/api/time/current/zone?timeZone=America%2FGuatemala"
data = requests.get(url)
hora = data.json()["hour"]
minutos = data.json()["minute"]

#api de la fecha
url2 = "https://tools.aimylogic.com/api/now?tz=America/Guatemala&format=yyyy-MM-dd"
data2  = requests.get(url2)
year = data2.json()["year"]
month = data2.json()["month"]
day = data2.json()["day"]

url3 = "https://catfact.ninja/facts"
ciudad = input("Ingresa tu ciudad: ")
url4 = f"http://wttr.in/{ciudad}?format=j1"


def obtener_datos():
    return hora, minutos,year,month,day








