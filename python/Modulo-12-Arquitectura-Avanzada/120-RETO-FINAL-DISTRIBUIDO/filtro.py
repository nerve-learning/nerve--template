from nerve import NexusClient

def procesar_asteroide(payload, sender):
    tamano = payload.get("tamano", 0)
    if tamano < 50:
        print("Roca inofensiva.")
    else:
        # Enviar mensaje a alarma
        filtro.send(to="alarma", payload={"tamano": tamano})

if __name__ == "__main__":
    filtro = NexusClient(name="filtro")
    filtro.connect()
    filtro.listen(procesar_asteroide)
