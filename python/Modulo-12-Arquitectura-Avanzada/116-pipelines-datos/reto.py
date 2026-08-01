from nerve.core import NexusHub, NexusClient
import time

if __name__ == "__main__":
    hub = NexusHub()
    hub.start()
    
    amasadora = NexusClient()
    horno = NexusClient()
    vitrina = NexusClient()
    
    amasadora.connect("amasadora")
    horno.connect("horno")
    vitrina.connect("vitrina")
    
    def trabajo_horno(payload):
        print(f"🔥 [HORNO] Recibi {payload['estado']}. Horneando a 200 grados...")
        payload["estado"] = "Pan Horneado"
        horno.send(to="vitrina", payload=payload)
        
    def trabajo_vitrina(payload):
        print(f"🍞 [VITRINA] ¡Pan fresco listo para la venta! {payload}")
        
    horno.listen(on_payload=trabajo_horno)
    vitrina.listen(on_payload=trabajo_vitrina)
    
    masa = {"ingredientes": "Harina, Agua y Levadura", "estado": "Masa Cruda"}
    print("🥣 [AMASADORA] Mezclando ingredientes y enviando masa al horno...")
    amasadora.send(to="horno", payload=masa)
    
    time.sleep(3)
    
    amasadora.disconnect()
    horno.disconnect()
    vitrina.disconnect()
    hub.stop()
