playa = [
    ["arena", "arena", "arena"],
    ["arena", "tesoro", "arena"],
    ["arena", "arena", "arena"]
]
print("Iniciando escaneo de la playa...")
for fila in playa:
    print("Revisando nueva fila...")
    for cuadrante in fila:
        if cuadrante == "tesoro":
            print("¡Tesoro encontrado! 💎")
print("Escaneo terminado.")
