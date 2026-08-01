import os

print("Preparando tu regalo...")
# 1. Crear carpeta regalo
os.makedirs("regalo", exist_ok=True)

# 2. Crear mensaje.txt
with open("regalo/mensaje.txt", "w") as f:
    f.write("¡Feliz Cumpleaños!")

# 3. Empacar con nerve
clave = "pastel"
os.system(f'NERVE_NRV_PASSWORD="{clave}" nerve pack regalo regalo_seguro.nrv')

print("¡Regalo envuelto en regalo_seguro.nrv!")

# 4. Borrar la carpeta original regalo
os.system("rm -rf regalo")

# 5. Imprimir mensaje
print("Amigo, ¡es hora de abrir tu regalo! Por favor escribe la contraseña.")

# 6. nerve open regalo_seguro.nrv (pedira la clave interactivamente)
os.system("nerve open regalo_seguro.nrv")

print("¡Felicidades, regalo abierto!")

# 7. Desasociar
print("Limpiando configuración (desasociando)...")
os.system("nerve unassociate")

print("Terminado.")
