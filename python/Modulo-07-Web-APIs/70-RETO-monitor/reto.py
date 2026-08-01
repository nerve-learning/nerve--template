import requests
from bs4 import BeautifulSoup

# URL del reto 10
url = "https://nerve.community.aleniastudios.me/laberinto/p6p/omega.html"

# Realizamos la petición GET
respuesta = requests.get(url)

# Imprimimos el código de estado
print(f"[+] Código de estado: {respuesta.status_code}")

if respuesta.status_code == 200:
    # Parsea el HTML
    soup = BeautifulSoup(respuesta.text, "html.parser")
    
    # Buscamos todos los fragmentos con la clase 'real-part'
    fragmentos = soup.find_all(class_="real-part")
    
    # Imprimimos la cantidad encontrada
    print(f"[+] Fragmentos encontrados: {len(fragmentos)}")
    
    # Unimos los fragmentos en orden
    mensaje = "".join(f.get_text() for f in fragmentos)
    print(f"[+] Protocolo reconstruido: {mensaje}")
