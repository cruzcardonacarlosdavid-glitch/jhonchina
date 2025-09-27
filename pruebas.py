from servidor import *

from customtkinter import *

app = CTk()
app.title("Nueva carpeta")

caja = CTkLabel(app, text = "")
caja.configure(text = f"{hora}:{minutos}" )
caja.pack()

app.mainloop()
