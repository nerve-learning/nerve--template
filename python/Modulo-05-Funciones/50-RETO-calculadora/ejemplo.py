# ==========================================
# PLANTILLA DEL JEFE FINAL: LA CALCULADORA
# ==========================================
# Historia: Eres el Alquimista Supremo. Necesitas crear una calculadora
# mágica que pueda sumar, restar, multiplicar y realizar operaciones complejas.
# Te han dejado la estructura vacía. Tu trabajo es llenarla.

import math # Herramienta de Python para matemáticas avanzadas

# 1. Crea una función que sume infinitos números usando *args
def sumar_infinito(*numeros):
    return sum(numeros)

# 2. Crea una función con un parámetro por defecto
def multiplicar(a, b=2):
    return a * b

# 3. Crea una función lambda que divida dos números
dividir_rapido = lambda x, y: x / y # <-- ¡Este te lo regalamos!

# 4. Crea una función que use math.sqrt() para sacar la raíz cuadrada
def raiz_cuadrada(numero):
    return math.sqrt(numero)

# === PRUEBAS DEL ALQUIMISTA ===
# Descomenta las líneas de abajo quitando el '#' cuando termines tus funciones
# para ver si funcionan.

print(sumar_infinito(1, 2, 3, 4, 5))  # Debería mostrar 15
print(multiplicar(10))                # Debería mostrar 20 (porque b=2 por defecto)
print(dividir_rapido(100, 4))         # Debería mostrar 25.0
print(raiz_cuadrada(81))              # Debería mostrar 9.0

# 6. Bonus: Crea una función extra llamada historial
def historial(**kwargs):
    print("--- Historial de Operaciones ---")
    for operacion, resultado in kwargs.items():
        print(f"{operacion}: {resultado}")

historial(Suma=15, Multiplicacion=20, Division=25.0, Raiz=9.0)
