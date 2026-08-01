from nerve import NexusClient

def procesar_alarma(payload, sender):
    tamano = payload.get("tamano", 0)
    print(f"🚨 ¡PELIGRO! Asteroide gigante detectado de {tamano} metros 🚨")

if __name__ == "__main__":
    print("--- INICIANDO SISTEMA DE ALARMA ---")
    print("Esperando alertas de asteroides...")
    alarma = NexusClient(name="alarma")
    alarma.connect()
    alarma.listen(procesar_alarma)
