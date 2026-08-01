import asyncio
from nerve.core import NexusClient
import os

cliente = NexusClient()
datos_recibidos = []

def on_payload(payload):
    datos_recibidos.append(payload)
    # Mantenemos solo los últimos 5 para el dashboard
    if len(datos_recibidos) > 5:
        datos_recibidos.pop(0)

async def monitor_main():
    print("📊 [Monitor] Iniciando...")
    
    conectado = False
    while not conectado:
        try:
            cliente.connect("monitor_01")
            cliente.listen(on_payload=on_payload)
            conectado = True
            print("📊 [Monitor] Conectado al Hub y escuchando.")
        except Exception as e:
            print(f"📊 [Monitor] Esperando al Hub... {e}")
            await asyncio.sleep(2)
            
    while True:
        # Limpiar consola (multiplataforma)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("========================================")
        print("        📊 DASHBOARD EN TIEMPO REAL      ")
        print("========================================")
        
        if not datos_recibidos:
            print("Esperando datos...")
        else:
            for dato in reversed(datos_recibidos):
                id_msj = dato.get('id', '?')
                crudo = dato.get('valor_crudo', 0)
                procesado = dato.get('valor_procesado', 0)
                status = dato.get('status', 'N/A')
                print(f"ID: {id_msj: <4} | Crudo: {crudo: <4} | Procesado: {procesado: <4} | Status: {status}")
        
        print("========================================")
        print("Presiona Ctrl+C para salir.")
        
        await asyncio.sleep(1)

if __name__ == "__main__":
    try:
        asyncio.run(monitor_main())
    except KeyboardInterrupt:
        print("📊 [Monitor] Detenido.")
