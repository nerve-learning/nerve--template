# Cálculo de Velocidad (v = d/t)
distancia = 150.5  # metros
tiempo = 12.3      # segundos
velocidad = distancia / tiempo

print(f"Cálculo de Velocidad:")
print(f"Distancia: {distancia} m, Tiempo: {tiempo} s")
print(f"Velocidad calculada: {velocidad:.2f} m/s\n")

# Cálculo de Fuerza (F = m*a)
masa = 50.0        # kg
aceleracion = 9.81 # m/s²
fuerza = masa * aceleracion

print(f"Cálculo de Fuerza:")
print(f"Masa: {masa} kg, Aceleración: {aceleracion} m/s²")
print(f"Fuerza calculada: {fuerza:.2f} N\n")

# Cálculo de Energía Cinética (Ec = 0.5 * m * v²)
masa_ec = 75.0     # kg
velocidad_ec = 15.5# m/s
energia_cinetica = 0.5 * masa_ec * (velocidad_ec ** 2)

print(f"Cálculo de Energía Cinética:")
print(f"Masa: {masa_ec} kg, Velocidad: {velocidad_ec} m/s")
print(f"Energía Cinética calculada: {energia_cinetica:.2f} J\n")
