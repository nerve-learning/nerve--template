import asyncio
import aiohttp

# Función asíncrona obtener_astronautas()
async def obtener_astronautas():
    url = "http://api.open-notify.org/astros.json"
    # Usamos async with para abrir la sesión de cliente
    async with aiohttp.ClientSession() as sesion:
        # Usamos async with para realizar la petición GET
        async with sesion.get(url) as respuesta:
            # Extraemos los datos en formato JSON de forma asíncrona
            datos = await respuesta.json()
            # Imprimimos el resultado
            print(f"Hay {datos['number']} astronautas en el espacio.")

# Función principal main()
async def main():
    await obtener_astronautas()

# Iniciamos el programa usando asyncio.run()
asyncio.run(main())
