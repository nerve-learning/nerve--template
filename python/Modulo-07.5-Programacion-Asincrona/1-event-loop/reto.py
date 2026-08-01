import asyncio

# Función asíncrona abrir_restaurante()
async def abrir_restaurante():
    print("Encendiendo luces...")
    print("Limpiando mesas...")
    print("¡Restaurante abierto!")

# Ejecutamos la función asíncrona usando asyncio.run()
asyncio.run(abrir_restaurante())
