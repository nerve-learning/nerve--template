from nerve import NexusClient

# Connect client
cliente = NexusClient()
cliente.connect("astronauta")

# Define callback
def auricular(datos):
    payload = datos.get("payload") if isinstance(datos, dict) else None
    if isinstance(payload, dict):
        inner_datos = payload
    else:
        inner_datos = datos

    if not isinstance(inner_datos, dict):
        return

    mensaje_recibido = inner_datos.get("mensaje")
    if mensaje_recibido:
        print("\n[Tierra]: " + str(mensaje_recibido))

# Register listener
cliente.listen(auricular)

# Interactive loop
while True:
    try:
        msg = input("Luna: ")
        paquete = {"mensaje": msg}
        cliente.send("tierra", paquete)
    except (KeyboardInterrupt, EOFError):
        break
