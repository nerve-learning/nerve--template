import asyncio
from nerve.core import NexusClient

class Procesador:
    def __init__(self):
        self.cliente = NexusClient()
        self.cola_mensajes = asyncio.Queue()

    def al_recibir(self, payload):
        # Callback síncrono del NexusClient
        # Lo pasamos a la cola asíncrona de manera segura si usamos threadsafe, 
        # pero como Nerve usa threads, meter a la cola de asyncio requiere cuidado.
        # Una forma sencilla es procesar aquí mismo o crear un event loop wrapper.
        # Dado que Nerve es síncrono en sus callbacks, haremos el procesamiento asíncrono
        # en el bucle principal.
        
        # Para evitar problemas de hilos con asyncio, podemos simplemente mutar una lista
        # o usar call_soon_threadsafe si tuviéramos acceso al loop.
        pass

# Mejor enfoque para este reto donde "no puedes usar threading directamente (usa async/await)":
# NexusClient ya maneja su propio hilo. Solo necesitamos que el procesador 
# reciba, transforme y envíe.

cliente = NexusClient()
cola_eventos = []

def on_payload(payload):
    cola_eventos.append(payload)

async def procesador_main():
    print("⚙️  [Procesador] Iniciando...")
    
    conectado = False
    while not conectado:
        try:
            cliente.connect("procesador_01")
            cliente.listen(on_payload=on_payload)
            conectado = True
            print("⚙️  [Procesador] Conectado al Hub y escuchando.")
        except Exception as e:
            print(f"⚙️  [Procesador] Esperando al Hub... {e}")
            await asyncio.sleep(2)
            
    while True:
        if cola_eventos:
            # Extraemos el más antiguo
            payload = cola_eventos.pop(0)
            print(f"⚙️  [Procesador] Recibido: {payload}")
            
            # Transformamos (ej. multiplicamos valor_crudo por 2)
            if "valor_crudo" in payload:
                payload["valor_procesado"] = payload["valor_crudo"] * 2
                payload["status"] = "OK"
                
                print(f"⚙️  [Procesador] Enviando al monitor: {payload}")
                try:
                    cliente.send(to="monitor_01", payload=payload)
                except Exception as e:
                    print(f"⚙️  [Procesador] Error al enviar al monitor: {e}")
        
        # Pequeña pausa para no bloquear el loop
        await asyncio.sleep(0.5)

if __name__ == "__main__":
    try:
        asyncio.run(procesador_main())
    except KeyboardInterrupt:
        print("⚙️  [Procesador] Detenido.")
