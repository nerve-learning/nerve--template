import requests
from bs4 import BeautifulSoup
import base64

# URL del reto 07
url = "https://nerve.community.aleniastudios.me/laberinto/c8c/crypt.html"

# Realizamos la petición GET
respuesta = requests.get(url)

# Imprimimos el código de estado
print(f"[+] Código de estado: {respuesta.status_code}")

if respuesta.status_code == 200:
    # Parsea el HTML
    soup = BeautifulSoup(respuesta.text, "html.parser")
    
    # Buscamos el elemento blockquote que tiene el atributo data-secret
    elemento = soup.find(attrs={"data-secret": True})
    
    if elemento:
        # Extraemos el valor en base64
        valor_b64 = elemento["data-secret"]
        print(f"[+] Atributo data-secret encontrado (raw): {valor_b64}")
        
        # Decodificamos el valor de Base64 a texto normal
        token = base64.b64decode(valor_b64).decode("utf-8")
        print(f"[+] Token decodificado: {token}")
