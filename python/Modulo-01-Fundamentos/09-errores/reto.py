print("Iniciando diagnóstico del sistema de la nave...")

combustible_litros = 5000
distancia_km = 10000

# Calculamos el consumo
consumo = distancia_km / combustible_litros

# Mostramos el resultado
print(f"El consumo es de {consumo} kilómetros por litro.")

mensaje_final = "Diagnóstico completado. Nivel de éxito: "
porcentaje = 100

# Intentamos mostrar el mensaje final
resultado_final = f"{mensaje_final}{porcentaje}"
print(resultado_final)
