# Solución del Reto 52

# Función leer_diario que recibe el nombre del archivo
def leer_diario(nombre_archivo):
    # Resolvemos la ruta relativa al directorio de este script sin importar 'os'
    partes = __file__.replace("\\", "/").split("/")
    directorio = "/".join(partes[:-1])
    
    if directorio:
        ruta_completa = directorio + "/" + nombre_archivo
    else:
        ruta_completa = nombre_archivo
        
    # Abrimos el archivo en modo lectura
    with open(ruta_completa, "r") as archivo:
        # Leemos el contenido completo
        texto = archivo.read()
        
        # Imprimimos la información requerida
        print("Mi diario dice:")
        print(texto)
        
        # Contamos la cantidad de caracteres
        cantidad = len(texto)
        print(f"El diario tiene {cantidad} caracteres en total.")

# Llamamos a la función pasándole "diario.txt"
leer_diario("diario.txt")
