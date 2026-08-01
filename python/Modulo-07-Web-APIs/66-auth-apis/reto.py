import requests
from bs4 import BeautifulSoup
import re

# URL del reto 06
url = "https://nerve.community.aleniastudios.me/laberinto/m5v/dyn.html"

# Definimos cabeceras (headers) para pasar el test
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Realizamos la petición GET enviando las cabeceras
respuesta = requests.get(url, headers=headers)

# Imprimimos el código de estado
print(f"[+] Código de estado: {respuesta.status_code}")

if respuesta.status_code == 200:
    # Parsea el HTML
    soup = BeautifulSoup(respuesta.text, "html.parser")
    
    # Buscamos la etiqueta script que contiene la variable secretValue
    scripts = soup.find_all("script")
    for script in scripts:
        if "secretValue" in script.text:
            # Extraemos el número que está en el comentario al final de la línea
            match = re.search(r'//\s*(\d+)', script.text)
            if match:
                numero = match.group(1)
                print(f"[+] Número cuántico encontrado: {numero}")
