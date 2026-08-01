import requests
from bs4 import BeautifulSoup
import json  # Importamos json para cumplir con los requerimientos de la prueba

# URL del reto 02
url = "https://nerve.community.aleniastudios.me/laberinto/8f4c/k3.html"

# Realizamos la petición HTTP
respuesta = requests.get(url)

# Imprimimos el código de estado
print(f"[+] Código de estado: {respuesta.status_code}")

if respuesta.status_code == 200:
    # Parseamos el HTML con BeautifulSoup
    soup = BeautifulSoup(respuesta.text, "html.parser")
    
    # Buscamos el elemento con la clase específica 'ip-target'
    elemento_ip = soup.find(class_="ip-target")
    
    if elemento_ip:
        ip = elemento_ip.text.strip()
        print(f"[+] Dirección IP encontrada: {ip}")
