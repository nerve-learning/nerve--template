from nerve import NexusClient
import time
import random

if __name__ == "__main__":
    cliente = NexusClient(name="radar")
    cliente.connect()
    
    while True:
        tamano = random.randint(1, 100)
        cliente.broadcast({"tamano": tamano})
        time.sleep(1)
