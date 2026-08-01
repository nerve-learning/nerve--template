import asyncio

# Función asíncrona corredor(nombre, tiempo_tardanza)
async def corredor(nombre, tiempo_tardanza):
    print(nombre + " empezó a correr.")
    await asyncio.sleep(tiempo_tardanza)
    print(nombre + " llegó a la meta.")

# Función asíncrona carrera()
async def carrera():
    # Usamos asyncio.gather para lanzar ambos corredores concurrentemente
    await asyncio.gather(
        corredor("Rayo", 1),
        corredor("Tortuga", 3)
    )
    print("¡La carrera ha terminado!")

# Iniciamos la carrera usando asyncio.run()
asyncio.run(carrera())
