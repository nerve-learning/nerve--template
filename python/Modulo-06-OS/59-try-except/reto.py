try:
    # Intentamos abrir el archivo que no existe
    with open("fantasma.txt", "r") as archivo:
        contenido = archivo.read()
except Exception as e:
    # Atrapamos el error e imprimimos un mensaje amigable
    print("Lo siento, no pudimos encontrar el archivo. Detalles del problema:", e)

# Fuera del bloque try/except, imprimimos el mensaje final
print("El programa ha finalizado con elegancia.")
