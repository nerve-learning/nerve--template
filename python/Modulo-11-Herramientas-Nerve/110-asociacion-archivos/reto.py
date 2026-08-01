import os

print("--- Iniciando el Desinstalador ---")
print("Eliminando configuración de Nerve...")

# Ejecutar nerve unassociate
os.system("nerve unassociate")

# Borrar el archivo de prueba si existe
os.system("rm -f mi_caja_fuerte_de_prueba.nrv")

print("¡Limpieza completada! Gracias por usar nuestro software.")
