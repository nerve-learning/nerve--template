from nerve.core import NexusHub, NexusClient
import time

if __name__ == "__main__":
    maquina_central = NexusHub(heartbeat_interval=1.5)
    maquina_central.start()
    print("🏥 Maquina Central encendida: Monitor cardiaco cada 1.5s")
    
    androide_azul = NexusClient()
    androide_azul.connect("androide_azul")
    print("🤖 Androide Azul conectado.")
    
    time.sleep(4)
    
    androide_azul.disconnect()
    maquina_central.stop()
    print("🛑 Desconexion exitosa.")
