mensajes = [
    "Hola, ¿cómo estás?",
    "Compra ahora con DESCUENTO increíble",
    "El partido fue increíble ayer",
    "GANA dinero desde casa GRATIS",
    "Me comí una pizza enorme",
    "URGENTE: reclama tu premio GRATIS",
    "El examen estuvo difícil",
    "Haz click AQUÍ para ganar DESCUENTO",
]

def filtrar_sospechosos(lista_mensajes, palabra_clave):
    for mensaje in lista_mensajes:
        if palabra_clave in mensaje:
            yield mensaje

palabra = "GRATIS"
print(f"=== Escaneando mensajes con la palabra: {palabra} ===\n")
generador = filtrar_sospechosos(mensajes, palabra)
contador = 0
for i, msj in enumerate(generador, start=1):
    print(f"Alerta #{i}: {msj}")
    contador = contador + 1

print(f"\nEscaneo completo. {contador} mensajes sospechosos encontrados.")
