peso_maleta = 23.5
etiqueta_destino = "PARIS"
cantidad_liquidos = 150

peso_permitido = peso_maleta <= 25
destino_correcto = etiqueta_destino == "LONDRES"
excede_liquidos = cantidad_liquidos > 100

print("--- REPORTE DE ESCÁNER DE EQUIPAJE ---")
print(f"¿El peso de la maleta está permitido?: {peso_permitido}")
print(f"¿La maleta va al destino correcto (LONDRES)?: {destino_correcto}")
print(f"¿El pasajero excede el límite de líquidos?: {excede_liquidos}")
