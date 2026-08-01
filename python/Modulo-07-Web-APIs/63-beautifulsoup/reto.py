import requests
from bs4 import BeautifulSoup

# URL del reto 03
url = "https://nerve.community.aleniastudios.me/laberinto/tz99/data-401.html"

# Realizamos la petición GET
respuesta = requests.get(url)

# Imprimimos el código de estado
print(f"[+] Código de estado: {respuesta.status_code}")

if respuesta.status_code == 200:
    # Parsea el HTML
    soup = BeautifulSoup(respuesta.text, "html.parser")
    
    # Buscamos la celda que tiene el atributo data-stock="true"
    elemento_celda = soup.find(attrs={"data-stock": "true"})
    
    if elemento_celda:
        numero = elemento_celda.text.strip()
        print(f"[+] Dato extraído de la tabla oculta: {numero}")
