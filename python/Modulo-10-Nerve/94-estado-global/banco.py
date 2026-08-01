from nerve import NexusClient

saldo_boveda = 1000

def cajero(datos):
    global saldo_boveda
    payload = datos.get("payload") if isinstance(datos, dict) else None
    if isinstance(payload, dict):
        inner_datos = payload
    else:
        inner_datos = datos

    if not isinstance(inner_datos, dict):
        return

    retiro = inner_datos.get("retiro", 0)
    if retiro > 0:
        saldo_boveda = saldo_boveda - retiro
        print(f"Retiro procesado de: {retiro}. Saldo actual: {saldo_boveda}")

# Setup client
cliente = NexusClient()
cliente.connect("banco_central")
cliente.listen(cajero)

input("Banco abierto. Presiona ENTER para cerrar...\n")
