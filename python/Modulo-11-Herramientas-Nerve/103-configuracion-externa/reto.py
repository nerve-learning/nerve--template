from nerve import NexusClient

# Crear un cliente Nerve (lee nerve.config automáticamente)
cliente = NexusClient()
cliente.connect("caja_fuerte")

# Enviar mensaje a yo_mismo
cliente.send("yo_mismo", {"mensaje": "¡Llegamos a la nueva casa!"})
