import time
from nerve import NexusClient

# Connect client
cliente = NexusClient()
cliente.connect("cerebro_matematico")

# Define callback
def al_recibir_mensaje(remitente, mensaje=None):
    if mensaje is None:
        payload = remitente
        sender = payload.get("from")
        msg = payload.get("payload")
    else:
        sender = remitente
        msg = mensaje

    if not isinstance(msg, dict):
        return

    accion = msg.get("accion")
    if accion == "sumar":
        a = msg.get("a", 0)
        b = msg.get("b", 0)
        total = a + b
        print(f"\n[!] Petición de '{sender}' recibida: sumar {a} y {b}.")
        # Send result back
        cliente.send(sender, {"accion": "resultado", "total": total})
        print("[✓] Resultado calculado y enviado.")

# Register listener
cliente.listen(al_recibir_mensaje)

print("--- MODO CALCULADORA ---")
print("[*] Cerebro encendido.")

# Keep alive
while True:
    time.sleep(1)
