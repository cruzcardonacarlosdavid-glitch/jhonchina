from servidor import *
from customtkinter import *
from tkinter import messagebox

def factss():
    facl = ""
    messagebox.showinfo("factos",f"{factoss(facl)}")

app = CTk()
app.title("datos")

fuente = CTkFont(family="Arial",size = 50)

caja = CTkLabel(app,text = f"tiempo : {hora} : {minutos}",font = fuente)
caja.grid(row= 0,column = 0, padx = 5, pady= 5)

caja2 = CTkLabel(app,text = f"fecha : {day} / {month} / {year}",font = fuente)
caja2.grid(row= 1,column = 0, padx = 5, pady= 5)

caja3 = CTkLabel(app,text = f"temperatura : {temp} C°",font = fuente)
caja3.grid(row= 2,column = 0, padx = 5, pady= 5)

caja4 = CTkLabel(app,text = f"velocidad del viento : {viento} km/h",font = fuente)
caja4.grid(row= 3,column = 0, padx = 5, pady= 5)


btn = CTkButton(app,text = "factos",command=factss, font= fuente)
btn.grid(row= 4,column = 0, padx = 5, pady= 5)
app.mainloop()