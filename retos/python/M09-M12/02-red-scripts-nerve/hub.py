from nerve.core import NexusHub
import time

if __name__ == "__main__":
    print("🌐 [Hub] Iniciando NexusHub...")
    try:
        hub = NexusHub()
        hub.start()
        print("🌐 [Hub] NexusHub encendido. Presiona Ctrl+C para detener.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 [Hub] Apagando NexusHub...")
        hub.stop()
