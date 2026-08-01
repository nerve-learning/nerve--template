import time
from nerve import NexusClient

cliente = NexusClient()
cliente.connect("sensor_temp")

while True:
    try:
        print("Enviando temperatura...")
        cliente.broadcast({"temp": 25})
        time.sleep(1)
    except (KeyboardInterrupt, EOFError):
        break
