import requests
from bs4 import BeautifulSoup

# URL del reto
url = "https://nerve.community.aleniastudios.me/laberinto/a1b2/x9.html"

# Haz un requests.get() a la URL
respuesta = requests.get(url)

# Verifica el status_code e imprime
print(f"[+] Código de estado: {respuesta.status_code}")

if respuesta.status_code == 200:
    # Crea el objeto BeautifulSoup
    soup = BeautifulSoup(respuesta.text, "html.parser")
    
    # Busca el elemento con el ID 'secret-code'
    codigo_elemento = soup.find(id="secret-code")
    
    if codigo_elemento:
        # Extrae el texto y lo muestra
        codigo_acceso = codigo_elemento.text.strip()
        print(f"[+] Código de acceso encontrado: {codigo_acceso}")
