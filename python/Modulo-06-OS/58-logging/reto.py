import logging

# Configura el sistema para que:
# - El archivo donde se guardará todo se llame diario_robot.txt
# - El nivel mínimo de registro sea de Información (logging.INFO)
logging.basicConfig(filename="diario_robot.txt", level=logging.INFO)

# Mensaje de Información
logging.info("El robot ha aterrizado en Marte.")

# Mensaje de Advertencia
logging.warning("Tormenta de arena detectada. Visibilidad reducida.")

# Mensaje de Error
logging.error("¡Atasco! La rueda derecha no responde.")

# Print final
print("Simulación del robot terminada. Revisando la bitácora...")
