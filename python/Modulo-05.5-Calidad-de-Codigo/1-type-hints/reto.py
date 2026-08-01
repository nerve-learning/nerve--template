def calcular_impuesto(precio: float, porcentaje: float) -> float:
    return precio * (porcentaje / 100)

def repetir_mensaje(mensaje: str, veces: int) -> str:
    return mensaje * veces

def es_numero_par(numero: int) -> bool:
    return numero % 2 == 0

def construir_perfil(nombre: str, edad: int, ciudad: str) -> dict:
    return {"nombre": nombre, "edad": edad, "ciudad": ciudad}

def imprimir_separador(caracter: str, longitud: int) -> None:
    print(caracter * longitud)

# Pruebas con valores reales
impuesto = calcular_impuesto(500.0, 16.0)
print(f"Impuesto de $500 al 16%: ${impuesto}")

mensaje = repetir_mensaje("Hola", 3)
print(f"Mensaje repetido: {mensaje}")

es_par = es_numero_par(8)
print(f"¿El 8 es par?: {es_par}")

perfil = construir_perfil("Kaia", 25, "CDMX")
print(f"Perfil creado: {perfil}")

imprimir_separador("-", 30)
