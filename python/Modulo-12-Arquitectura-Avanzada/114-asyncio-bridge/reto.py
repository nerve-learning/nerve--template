from nerve.core import NexusHub
from nerve.bridge import NerveBridge

if __name__ == "__main__":
    hub = NexusHub()
    hub.start()
    
    print("🌀 Abriendo portal interdimensional...")
    
    puente = NerveBridge(host="127.0.0.1", port=8080)
    puente.start()
