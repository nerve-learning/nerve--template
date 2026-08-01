import shutil

# Función falsificar_arte(nombre_original, nombre_falso)
def falsificar_arte(nombre_original, nombre_falso):
    # Resolvemos la ruta relativa al script
    partes = __file__.replace("\\", "/").split("/")
    directorio = "/".join(partes[:-1])
    
    ruta_orig = (directorio + "/" + nombre_original) if directorio else nombre_original
    ruta_falsa = (directorio + "/" + nombre_falso) if directorio else nombre_falso
    
    # Copiamos el archivo original al nuevo nombre falso
    shutil.copy(ruta_orig, ruta_falsa)
    print(f"¡Muajaja! He creado una copia falsa llamada: {nombre_falso}")

# Preparar el terreno fuera de la función: crear "monalisa.txt"
partes = __file__.replace("\\", "/").split("/")
directorio = "/".join(partes[:-1])
ruta_monalisa = (directorio + "/monalisa.txt") if directorio else "monalisa.txt"

with open(ruta_monalisa, "w") as archivo:
    archivo.write("Soy la pintura original")

# Llamamos a falsificar_arte con los nombres requeridos
falsificar_arte("monalisa.txt", "monalisa_falsa.txt")

# Bono Opcional: mover/renombrar monalisa.txt a cuadro_robado.txt
ruta_robado = (directorio + "/cuadro_robado.txt") if directorio else "cuadro_robado.txt"
shutil.move(ruta_monalisa, ruta_robado)
