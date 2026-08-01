from nerve.core import NexusHub, NexusClient
import time

ordenes_pendientes = {}

def trabajo_cocina(payload):
    try:
        id_orden = payload["id_orden"]
        platillo = payload["platillo"]
        
        print(f"🍳 [COCINA] Preparando: {platillo} (Orden {id_orden})...")
        print(f"🔔 [COCINA] ¡Orden {id_orden} terminada! Avisando al mesero...")
        
        ack = {"id_orden": id_orden, "status": "LISTO"}
        cocina.send(to="mesero", payload=ack)
    except Exception as e:
        print(f"Error procesando orden en cocina: {e}")

def trabajo_mesero(payload):
    if payload.get("status") == "LISTO":
        id_orden = payload.get("id_orden")
        if id_orden in ordenes_pendientes:
            platillo = ordenes_pendientes[id_orden]
            print(f"🏃 [MESERO] Recibí ACK. ¡Llevando {platillo} a la mesa! Órdenes pendientes: {len(ordenes_pendientes) - 1}")
            del ordenes_pendientes[id_orden]

if __name__ == "__main__":
    hub = NexusHub()
    hub.start()
    
    mesero = NexusClient()
    cocina = NexusClient()
    
    mesero.connect("mesero")
    cocina.connect("cocina")
    
    cocina.listen(on_payload=trabajo_cocina)
    mesero.listen(on_payload=trabajo_mesero)
    
    ordenes_pendientes[42] = "Hamburguesa con Papas"
    print("📝 [MESERO] Orden 42 anotada. Enviando a cocina...")
    mesero.send(to="cocina", payload={"id_orden": 42, "platillo": "Hamburguesa con Papas"})
    
    time.sleep(3)
    
    mesero.disconnect()
    cocina.disconnect()
    hub.stop()
