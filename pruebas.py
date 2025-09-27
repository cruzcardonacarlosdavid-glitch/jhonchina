from servidor import *

from customtkinter import *

app = CTk()
app.title("Nueva carpeta")

caja = CTkLabel(app, text = "")
caja.configure(text = f"{hora}:{minutos}" )
caja.pack()

caja2 = CTkLabel(app, text = "")
caja2.configure(text = f"{day}/{month}/{year}" )
caja2.pack()

caja3 = CTkLabel(app, text = "")
caja3.configure(text = f"{temp}")
caja3.pack()

caja4 = CTkLabel(app, text = "")
caja4.configure(text = f"{viento}")
caja4.pack()
app.mainloop()
