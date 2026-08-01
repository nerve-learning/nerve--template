from nerve.core import NexusHub, NexusClient
import time

def escuchar_cajero(payload):
    print(f"🏦 [CAJERO] Procesando petición: {payload}")

if __name__ == "__main__":
    hub = NexusHub(rate_limit_messages_per_sec=1)
    hub.start()
    
    cajero = NexusClient()
    cajero.connect("cajero")
    cajero.listen(on_payload=escuchar_cajero)
    
    cliente_impaciente = NexusClient()
    cliente_impaciente.connect("cliente_impaciente")
    
    for i in range(5):
        cliente_impaciente.send(to="cajero", payload={"peticion": "¡Quiero mi dinero ya!"})
        time.sleep(0.2)
        
    time.sleep(2)
    
    cliente_impaciente.disconnect()
    cajero.disconnect()
    hub.stop()
