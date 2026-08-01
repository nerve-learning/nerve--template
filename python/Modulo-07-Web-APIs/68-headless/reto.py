import requests
from bs4 import BeautifulSoup
import json

# URL del reto 08
url = "https://nerve.community.aleniastudios.me/laberinto/9x2/profile.html"

# Petición GET
respuesta = requests.get(url)

# Imprimimos el código de estado
print(f"[+] Código de estado: {respuesta.status_code}")

if respuesta.status_code == 200:
    # Parsea el HTML
    soup = BeautifulSoup(respuesta.text, "html.parser")
    
    # Encontramos la etiqueta script con type="application/json"
    script_tag = soup.find("script", type="application/json")
    
    if script_tag:
        # Cargamos el texto del script como un diccionario JSON
        datos = json.loads(script_tag.string)
        
        # Extraemos el campo email
        email = datos["email"]
        print(f"[+] Email encontrado en JSON incrustado: {email}")
