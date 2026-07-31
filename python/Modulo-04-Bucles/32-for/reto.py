maleta = ["ropa", "cepillo", "bomba", "zapatos", "líquido"]
print("Iniciando escaneo de equipaje...")
for objeto in maleta:
    print("Escaneando:")
    print(objeto)
    if objeto == "bomba":
        print("¡ALERTA ROJA! Objeto peligroso detectado.")
print("Escaneo finalizado.")
