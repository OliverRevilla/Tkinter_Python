import requests
from tkinter import *


#llamada al API
def MostrarRespuesta(clima):
    try:
        nombre_ciudad = clima["name"]
        desc = clima["weather"][0]["description"]
        temp = clima["main"]["temp"]
        hum= clima["main"]["humidity"]

        ciudad["text"] = nombre_ciudad
        temperatura["text"] = str(int(temp)) + "°C"
        descripcion["text"] = desc
        humedad["text"] = str(float(hum)) + "%"
    except:
        ciudad["text"] = "No se encontró ciudad"
        temperatura["text"] = ""
        descripcion["text"] = ""
        humedad["text"] = ""

def clima_json(ciudad):
    #Manejo de errores:
    try:
        API_key = "3ff1f2e830b8a8297aa71126e771a8d3"
        URL = "https://api.openweathermap.org/data/2.5/weather" #Usar https:// porque es un pparámetro
        parametros = {"APPID": API_key, "q": ciudad, "units": "metric"}
        response = requests.get(URL, params = parametros)
        clima = response.json()
    except:
        print("Error")

    MostrarRespuesta(clima)

ventana = Tk()
ventana.geometry("350x550")

texto_ciudad = Entry(ventana, font = ("Courier",20,"normal"), justify = "center")
texto_ciudad.pack(padx = 30, pady = 30)

obtener_clima = Button(ventana, text = "Obtener Clima",font = ("Courier",10,"normal"), command = lambda: clima_json(texto_ciudad.get()))
obtener_clima.pack()
#Ciudad
ciudad = Label(font = ("Courier", 20, "normal"))
ciudad.pack(padx = 20, pady = 20)
#Temperatura
temperatura = Label( font = ("Courier", 50, "normal"))
temperatura.pack(padx = 20, pady = 20)
#Descripción
descripcion = Label(font = ("Courier", 20, "normal"))
descripcion.pack(padx = 20, pady = 20)
#Humedad
humedad = Label(font = ("Vendana", 20, "normal"))
humedad.pack(padx = 20, pady = 20)

#3ff1f2e830b8a8297aa71126e771a8d3
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
#api.openweathermap.org/data/2.5/weather?q={city name},{state code}&appid={API key}
#api.openweathermap.org/data/2.5/weather?q={city name},{state code},{country code}&appid={API key}



ventana.mainloop()

