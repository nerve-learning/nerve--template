import asyncio

# Función asíncrona calentar_comida()
async def calentar_comida():
    print("Metiendo la comida al microondas...")
    # Simula 2 segundos de cocción asíncrona
    await asyncio.sleep(2)
    print("¡Comida lista! (Beep beep)")

# Función asíncrona principal main()
async def main():
    print("Tengo hambre")
    # Llama a calentar_comida usando await
    await calentar_comida()
    print("A comer")

# Ejecución de la función principal
asyncio.run(main())
