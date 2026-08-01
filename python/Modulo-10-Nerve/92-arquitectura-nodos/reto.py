from nerve import NexusClient

# Connect client
cliente = NexusClient()
cliente.connect("central_alarmas")

# Define callback
def vigilante(datos):
    # Support both wrapped and unwrapped payload formats
    payload = datos.get("payload") if isinstance(datos, dict) else None
    if isinstance(payload, dict):
        inner_datos = payload
    else:
        inner_datos = datos

    if not isinstance(inner_datos, dict):
        return

    peligro = inner_datos.get("peligro")
    if peligro == "fuego":
        print("¡ALERTA ROJA! Activando aspersores de agua.")
    elif peligro == "ladron":
        print("¡ALERTA AZUL! Llamando a la policía local.")
    else:
        print("Situación normal. Seguimos vigilando.")

# Register listener
cliente.listen(vigilante)

# Wait for reports
input("Central de Alarmas activada. Esperando reportes...\n")
