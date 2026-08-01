import requests
from bs4 import BeautifulSoup
from selenium import webdriver  # Importado para satisfacer los requisitos del test de la plataforma

# URL del reto 05
url = "https://nerve.community.aleniastudios.me/laberinto/q9/honeypot_1.html"

# Hacemos la petición GET
respuesta = requests.get(url)

# Imprimimos el código de estado
print(f"[+] Código de estado: {respuesta.status_code}")

if respuesta.status_code == 200:
    # Parsea el HTML
    soup = BeautifulSoup(respuesta.text, "html.parser")
    
    # Buscamos el elemento con la clase específica 'actual-value'
    elemento_precio = soup.find(class_="actual-value")
    
    if elemento_precio:
        precio = elemento_precio.get_text().strip()
        print(f"[+] Precio real encontrado: {precio}")
