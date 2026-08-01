from nerve.core import NexusClient
import time

def mensaje_torre(payload):
    print(f"🗼 [TORRE] Mensaje recibido: {payload}")

if __name__ == "__main__":
    torre_control = NexusClient()
    torre_control.connect("torre_control")
    torre_control.listen(on_payload=mensaje_torre)
    
    avion_01 = NexusClient()
    avion_01.connect("avion_01")
    avion_01.send(to="torre_control", payload={"mensaje": "Solicito permiso para aterrizar"})
    
    time.sleep(2)
    
    torre_control.disconnect()
    avion_01.disconnect()
