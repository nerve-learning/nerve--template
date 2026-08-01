import time
from nerve import NexusClient

print("Iniciando transmisor...")

# Connect client
cliente = NexusClient()
cliente.connect("agente_007")
print("Conectado como agente_007.")

# Secret report
informe_secreto = {
    "mision": "Aterrizaje Lunar",
    "objetivo": "Establecer base de comunicación",
    "nivel_peligro": 5
}

print("Enviando informe secreto al cuartel_general...")
cliente.send("cuartel_general", informe_secreto)
print("Informe enviado.")

print("Avisando a la red local...")
cliente.broadcast({"aviso": "Misión cumplida. Agente fuera."})

# Wait for transmission
time.sleep(1)
print("Misión cumplida. Agente fuera.")
