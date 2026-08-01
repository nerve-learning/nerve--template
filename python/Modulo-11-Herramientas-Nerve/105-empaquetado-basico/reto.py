import os

print("Preparando la misión...")
# 1. Crear carpeta mision
os.makedirs("mision", exist_ok=True)

# 2. Crear coordenadas.txt con el texto "Latitud 40, Longitud -3"
with open("mision/coordenadas.txt", "w") as f:
    f.write("Latitud 40, Longitud -3")

print("Carpeta creada.")

# 3. Empacar con Nerve usando la clave "agente007"
print("Empacando con Nerve...")
clave = "agente007"
origen = "mision"
caja_fuerte = "paquete_seguro.nrv"
comando_pack = f'NERVE_NRV_PASSWORD="{clave}" nerve pack {origen} {caja_fuerte}'
os.system(comando_pack)

# 4. Desempacar en la base base_aliada
print("Desempacando en la base...")
destino = "base_aliada"
comando_unpack = f'NERVE_NRV_PASSWORD="{clave}" nerve unpack {caja_fuerte} {destino}'
os.system(comando_unpack)

print("Misión completada.")
