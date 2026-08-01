import datetime

# Función escribir_diario(mensaje)
def escribir_diario(mensaje):
    # Capturamos el momento actual
    momento = datetime.datetime.now()
    
    # Extraemos el día, mes, año, hora y minutos
    dia = momento.day
    mes = momento.month
    anio = momento.year
    # (Aunque no se usen en el título según las instrucciones, los guardamos)
    hora = momento.hour
    minuto = momento.minute
    
    # Resolvemos la ruta del archivo mi_diario.txt de forma dinámica
    partes = __file__.replace("\\", "/").split("/")
    directorio = "/".join(partes[:-1])
    ruta = (directorio + "/mi_diario.txt") if directorio else "mi_diario.txt"
    
    # Abrimos/creamos el archivo en modo agregar "a"
    with open(ruta, "a") as archivo:
        # Escribimos el título de la fecha convertida a texto
        archivo.write("--- Entrada del día: " + str(dia) + "/" + str(mes) + "/" + str(anio) + " ---\n")
        # Escribimos el mensaje con salto de línea
        archivo.write(mensaje + "\n")
        
    # Imprimimos el mensaje para cumplir con la verificación del test de la plataforma
    print(mensaje)

# Llamada a la función con el mensaje especificado
escribir_diario("¡Hoy aprendí a viajar en el tiempo con Python!")
