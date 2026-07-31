accesos = ["admin", "usuario1", "HACKER", "invitado", "usuario2"]
print("Analizando accesos al servidor...")
for codigo in accesos:
    print("Revisando:")
    print(codigo)
    if codigo == "HACKER":
        print("¡INTRUSO DETECTADO! Apagando sistema...")
        break
print("Servidor fuera de línea.")
