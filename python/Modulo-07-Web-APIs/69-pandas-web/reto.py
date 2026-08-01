import requests
from bs4 import BeautifulSoup

# URL del reto 09
url = "https://nerve.community.aleniastudios.me/laberinto/0w1/vector.html"

# Realizamos la petición GET
respuesta = requests.get(url)

# Imprimimos el código de estado
print(f"[+] Código de estado: {respuesta.status_code}")

if respuesta.status_code == 200:
    # Parsea el HTML
    soup = BeautifulSoup(respuesta.text, "html.parser")
    
    # Buscamos la etiqueta svg (exigida por la prueba)
    svg = soup.find("svg")
    
    if svg:
        # Buscamos el elemento text dentro del svg
        texto_svg = svg.find("text")
        if texto_svg:
            codigo = texto_svg.get_text().strip()
            print(f"[+] Código vectorial encontrado: {codigo}")
