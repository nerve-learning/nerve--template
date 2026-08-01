import asyncio
import random
from nerve.core import NexusClient

async def productor():
    print("🚀 [Productor] Iniciando...")
    cliente = NexusClient()
    
    # Manejo de reconexión automática delegada al NexusClient
    # Pero lo envolvemos en try/except por si el hub no está
    conectado = False
    while not conectado:
        try:
            cliente.connect("productor_01")
            conectado = True
            print("🚀 [Productor] Conectado al Hub.")
        except Exception as e:
            print(f"🚀 [Productor] Esperando al Hub... {e}")
            await asyncio.sleep(2)
            
    contador = 1
    while True:
        try:
            datos = {
                "id": contador,
                "valor_crudo": random.randint(10, 100)
            }
            print(f"🚀 [Productor] Enviando datos: {datos}")
            cliente.send(to="procesador_01", payload=datos)
            contador += 1
        except Exception as e:
            print(f"🚀 [Productor] Error al enviar: {e}")
            
        await asyncio.sleep(2)

if __name__ == "__main__":
    try:
        asyncio.run(productor())
    except KeyboardInterrupt:
        print("🚀 [Productor] Detenido.")
