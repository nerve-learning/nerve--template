import time
from nerve import NexusClient

lista_tareas = []

def al_recibir_mensaje(remitente, mensaje=None):
    global lista_tareas
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
    if accion == "pedir_tareas":
        if len(lista_tareas) > 0:
            respuesta = {
                "accion": "enviar_tareas",
                "datos": lista_tareas
            }
            cliente.broadcast(respuesta)
    elif accion == "enviar_tareas":
        lista_tareas = msg.get("datos", [])
        print(f"\n[!] ¡Sincronizado! Tareas actuales: {lista_tareas}")
    elif accion == "nueva_tarea":
        tarea = msg.get("datos")
        if tarea and tarea not in lista_tareas:
            lista_tareas.append(tarea)
            print(f"\n[*] Nueva tarea recibida: {tarea}")

# Setup client
cliente = NexusClient()
cliente.connect("todo_client")
cliente.listen(al_recibir_mensaje)

print("[*] Pidiendo sincronización a la red...")
cliente.broadcast({"accion": "pedir_tareas"})
time.sleep(1)

while True:
    try:
        print("\n--- Lista de Tareas ---")
        for i, t in enumerate(lista_tareas, 1):
            print(f"{i}. {t}")
        nueva = input("Ingresa una nueva tarea: ")
        if nueva:
            lista_tareas.append(nueva)
            cliente.broadcast({"accion": "nueva_tarea", "datos": nueva})
    except (KeyboardInterrupt, EOFError):
        break
