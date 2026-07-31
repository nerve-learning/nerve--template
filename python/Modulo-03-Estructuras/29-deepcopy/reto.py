import copy

estacion_real = ["Panel Solar", "Motor Principal", ["Computadora", "Soporte Vital"]]

simulacion = copy.deepcopy(estacion_real)
simulacion[2].remove("Soporte Vital")

print("--- REPORTE DE DAÑOS ---")
print(f"Estación Real: {estacion_real}")
print(f"Simulación: {simulacion}")
