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
def factoss():
    url3 = "https://catfact.ninja/fact"
    data3 = requests.get(url3).json()
    facto = data3["fact"]
    return facto

url4 = f"http://wttr.in/solola?format=j1"
data4 = requests.get(url4).json()
temp = data4["current_condition"][0]["temp_C"]
descripcion = data4["current_condition"][0]["weatherDesc"][0]["value"]
viento = data4["current_condition"][0]["windspeedKmph"]


def obtener_datos():
    return hora, minutos,year,month,day,temp,descripcion,viento


