import time
from nerve import NexusClient

# Se conecta a la red con el nombre "estudiante_curioso"
emisor = NexusClient()

try:
    emisor.connect("estudiante_curioso")
    
    # Utilizar un bucle while para enviar 10 mensajes
    i = 1
    while i <= 10:
        mensaje = {"mensaje": "Hola Hub", "numero_de_intento": i}
        emisor.send("servidor_central", mensaje)
        time.sleep(2)
        i += 1

except ConnectionRefusedError:
    pass
