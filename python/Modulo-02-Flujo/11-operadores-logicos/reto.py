altura = 150
edad = 13
residente = False

puede_subir = altura > 140 and edad >= 12
tiene_descuento = edad < 15 or residente

print("--- Control de Acceso: El Dragón ---")
print(f"¿El visitante puede subir a la montaña rusa?: {puede_subir}")
print(f"¿El visitante tiene derecho a descuento?: {tiene_descuento}")
