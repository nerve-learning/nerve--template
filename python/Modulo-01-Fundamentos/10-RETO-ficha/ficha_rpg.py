# Pedir datos
print("--- GENERADOR DE HÉROES ---")
nombre = input("Nombre: ")
clase = input("Clase: ")
nivel = int(input("Nivel: "))
dinero = float(input("Dinero inicial: "))

# Calcular stats
vida_maxima = nivel * 15
poder_magico = nivel / 2
dinero_restante = dinero - 10.5

# Imprimir ficha
print("====================================")
print("      FICHA DE PERSONAJE")
print("====================================")
print(f"Nombre: {nombre}")
print(f"Clase: {clase}")
print(f"Nivel: {nivel}")
print("------------------------------------")
print("Estadísticas:")
print(f"Vida Máxima: {vida_maxima}")
print(f"Poder Mágico: {poder_magico}")
print(f"Oro Restante: {dinero_restante}")
print("====================================")
