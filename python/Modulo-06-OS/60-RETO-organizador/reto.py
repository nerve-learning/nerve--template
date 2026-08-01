import os
import shutil
import logging

# Configura el diario de limpieza
logging.basicConfig(filename="limpieza.log", level=logging.INFO)

# Carpetas del cuarto y destinos
carpeta_caos = "cuarto_desordenado"
carpeta_imagenes = os.path.join(carpeta_caos, "imagenes")
carpeta_documentos = os.path.join(carpeta_caos, "documentos")

# Creamos las carpetas si no existen
if not os.path.exists(carpeta_imagenes):
    os.makedirs(carpeta_imagenes)

if not os.path.exists(carpeta_documentos):
    os.makedirs(carpeta_documentos)

# Leemos lo que hay en el cuarto desordenado
if os.path.exists(carpeta_caos):
    cosas = os.listdir(carpeta_caos)
    
    for cosa in cosas:
        ruta_origen = os.path.join(carpeta_caos, cosa)
        
        # Ignoramos si es una carpeta (como 'imagenes' o 'documentos')
        if not os.path.isfile(ruta_origen):
            continue
            
        # Determinamos la carpeta destino según la extensión del archivo
        if cosa.endswith(".jpg"):
            ruta_destino = os.path.join(carpeta_imagenes, cosa)
        elif cosa.endswith(".txt"):
            ruta_destino = os.path.join(carpeta_documentos, cosa)
        else:
            # Si no es imagen (.jpg) ni texto (.txt), lo ignoramos
            continue
            
        # Intentamos mover el archivo
        try:
            shutil.move(ruta_origen, ruta_destino)
            logging.info("Archivo movido: " + cosa)
        except Exception as e:
            logging.error("Fallo al mover: " + str(e))

print("Limpieza terminada")
