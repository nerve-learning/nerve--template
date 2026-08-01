from nerve.core import NexusClient

def leer_transmision(payload):
    print(f"[COMUNICADO]: {payload}")

def alerta_red_restablecida():
    print("⚠️ ENLACE DE COMUNICACIONES RESTABLECIDO ⚠️")

if __name__ == "__main__":
    cliente = NexusClient()
    cliente.connect("monitor_alpha")
    cliente.listen(on_payload=leer_transmision, on_reconnect=alerta_red_restablecida)
