import time
from nerve import NexusClient

# 2. Crea una instancia de NexusClient llamada trabajador
trabajador = NexusClient()

# 3. Conecta al trabajador a la red de Nerve bajo el nombre "procesador_web"
trabajador.connect("procesador_web")

# 4. Define una función callback llamada procesar_datos
def procesar_datos(datos):
    print("¡Mensaje recibido del puente web!")
    print(f"Contenido: {datos}")

# 5. Registra el callback
trabajador.listen(procesar_datos)

# 6. Crea un bucle infinito
while True:
    time.sleep(1)
