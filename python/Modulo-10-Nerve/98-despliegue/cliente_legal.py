import time
from nerve import NexusClient

cliente = NexusClient()
cliente.connect("infiltrado")

while True:
    time.sleep(1)
