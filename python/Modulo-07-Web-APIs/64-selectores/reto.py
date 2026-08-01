import requests
from bs4 import BeautifulSoup

# URL del reto 04
url = "https://nerve.community.aleniastudios.me/laberinto/v2n/layout_b.html"

# Hacemos la petición GET
respuesta = requests.get(url)

# Imprimimos el código de estado
print(f"[+] Código de estado: {respuesta.status_code}")

if respuesta.status_code == 200:
    # Parsea el HTML
    soup = BeautifulSoup(respuesta.text, "html.parser")
    
    # Usamos select() con selectores CSS para navegar la lista secreta
    elementos = soup.select(".secret-structure li.file")
    
    for elemento in elementos:
        texto = elemento.get_text().strip()
        if "ZETA" in texto:
            # Extraemos el código dividiendo por dos puntos
            partes = texto.split(":")
            codigo = partes[1].strip()
            print(f"[+] Código de identificación: {codigo}")
