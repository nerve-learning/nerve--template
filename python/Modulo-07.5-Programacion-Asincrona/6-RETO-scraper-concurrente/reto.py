import asyncio
import aiohttp

# Función asíncrona descargar_ruta(sesion, url)
async def descargar_ruta(sesion, url):
    try:
        async with sesion.get(url) as respuesta:
            respuesta.raise_for_status()
            texto = await respuesta.text()
            print(f"URL: {url} - Descargados {len(texto)} caracteres.")
    except Exception as e:
        print(f"Ocurrió un error al descargar {url}: {e}")

# Función principal main()
async def main():
    base_url = "https://nerve.community.aleniastudios.me"
    rutas = ["/laberinto/a1b2/x9.html", "/laberinto/8f4c/k3.html", "/laberinto/tz99/data-401.html"]
    
    print("Iniciando extracción masiva...")
    
    async with aiohttp.ClientSession() as sesion:
        tareas = []
        for ruta in rutas:
            url_completa = base_url + ruta
            # Añadimos la tarea a la lista sin hacer await aquí
            tareas.append(descargar_ruta(sesion, url_completa))
            
        # Ejecutamos todas las tareas simultáneamente
        await asyncio.gather(*tareas)
        
    print("Extracción finalizada.")

# Iniciamos el programa principal
asyncio.run(main())
