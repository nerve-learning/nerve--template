import math

def sumar_infinito(*numeros):
    return sum(numeros)

def multiplicar(a, b=2):
    return a * b

dividir_rapido = lambda x, y: x / y

def raiz_cuadrada(numero):
    return math.sqrt(numero)

print(sumar_infinito(1, 2, 3, 4, 5)) 
print(multiplicar(10))               
print(dividir_rapido(100, 4))        
print(raiz_cuadrada(81))             

def historial(**kwargs):
    print("--- Historial de Operaciones ---")
    for operacion, resultado in kwargs.items():
        print(f"{operacion}: {resultado}")

historial(Suma=15, Multiplicacion=20, Division=25.0, Raiz=9.0)
