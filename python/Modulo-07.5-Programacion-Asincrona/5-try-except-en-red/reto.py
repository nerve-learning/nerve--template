import asyncio
import aiohttp

# Función asíncrona explorar(sesion, url)
async def explorar(sesion, url):
    try:
        async with sesion.get(url) as respuesta:
            # Hace que la respuesta lance una excepción si hay código de error HTTP (ej. 404)
            respuesta.raise_for_status()
            return "Exito"
    except Exception as e:
        print("Ocurrió un error al conectar")
        return "Fallo"

# Función principal main()
async def main():
    urls = [
        "https://nerve.community.aleniastudios.me/laberinto/a1b2/x9.html",
        "https://nerve.community.aleniastudios.me/laberinto/falsa-123.html"
    ]
    
    async with aiohttp.ClientSession() as sesion:
        # Ejecutamos las dos exploraciones concurrentemente usando asyncio.gather
        resultados = await asyncio.gather(
            explorar(sesion, urls[0]),
            explorar(sesion, urls[1])
        )
        # Imprimimos la lista de resultados
        print("Resultados:", resultados)

# Ejecutamos el programa principal
asyncio.run(main())
