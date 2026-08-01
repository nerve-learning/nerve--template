from nerve.core import NexusHub, NexusClient
import time

estado_tamagotchi = {
    "hambre": 50,
    "felicidad": 50
}

def procesar_comando(payload):
    if payload == "alimentar":
        estado_tamagotchi["hambre"] -= 10
        print(f"🍕 Tamagotchi comio. Hambre actual: {estado_tamagotchi['hambre']}")
    elif payload == "jugar":
        estado_tamagotchi["felicidad"] += 10
        print(f"⚽ Tamagotchi jugo. Felicidad actual: {estado_tamagotchi['felicidad']}")

if __name__ == "__main__":
    hub = NexusHub()
    hub.start()
    
    cliente = NexusClient()
    cliente.connect("tamagotchi")
    cliente.listen(on_payload=procesar_comando)
    
    time.sleep(1)
    cliente.send(to="tamagotchi", payload="alimentar")
    time.sleep(1)
    cliente.send(to="tamagotchi", payload="alimentar")
    time.sleep(1)
    cliente.send(to="tamagotchi", payload="jugar")
    time.sleep(1)
    
    cliente.disconnect()
    hub.stop()
