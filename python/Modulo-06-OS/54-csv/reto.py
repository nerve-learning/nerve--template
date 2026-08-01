import csv

# 2. Variable peliculas (lista de listas con título y calificación)
peliculas = [["Shrek", 10], ["Titanic", 8], ["Matrix", 9]]

# 3. Función guardar_peliculas(lista_peliculas)
def guardar_peliculas(lista_peliculas):
    # Resolvemos la ruta para el archivo CSV
    partes = __file__.replace("\\", "/").split("/")
    directorio = "/".join(partes[:-1])
    ruta = (directorio + "/mis_peliculas.csv") if directorio else "mis_peliculas.csv"
    
    # Abrimos el archivo en modo escritura con newline=""
    with open(ruta, "w", newline="") as archivo:
        # Creamos al escritor
        escritor = csv.writer(archivo)
        # Escribimos los encabezados
        escritor.writerow(["Titulo", "Calificacion"])
        # Escribimos cada película
        for peli in lista_peliculas:
            escritor.writerow(peli)

# 9. Función leer_peliculas()
def leer_peliculas():
    # Resolvemos la ruta para el archivo CSV
    partes = __file__.replace("\\", "/").split("/")
    directorio = "/".join(partes[:-1])
    ruta = (directorio + "/mis_peliculas.csv") if directorio else "mis_peliculas.csv"
    
    # Abrimos en modo lectura
    with open(ruta, "r") as archivo:
        # Creamos al lector
        lector = csv.reader(archivo)
        # Imprimimos cada fila
        for fila in lector:
            print(fila)

# Llamamos a guardar_peliculas pasándole la lista original
guardar_peliculas(peliculas)

# Llamamos a leer_peliculas para verificar
leer_peliculas()
