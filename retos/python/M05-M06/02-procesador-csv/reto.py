import csv
import requests
import io

URL_CSV = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

def descargar_csv(url):
    """Descarga el contenido de un CSV desde una URL."""
    try:
        respuesta = requests.get(url, timeout=10)
        respuesta.raise_for_status()
        return respuesta.text
    except Exception as e:
        print(f"Error al descargar: {e}")
        return ""

def procesar_filas(contenido_csv):
    """Limpia las filas y extrae solo las que tienen datos válidos para Age y Fare."""
    lector = csv.DictReader(io.StringIO(contenido_csv))
    filas_limpias = []
    for fila in lector:
        edad_str = fila.get("Age", "").strip()
        tarifa_str = fila.get("Fare", "").strip()
        if edad_str and tarifa_str:
            try:
                edad = float(edad_str)
                tarifa = float(tarifa_str)
                nombre = fila.get("Name", "").strip().title()
                filas_limpias.append({
                    "Nombre": nombre,
                    "Edad": edad,
                    "Tarifa": tarifa
                })
            except ValueError:
                pass
    return filas_limpias

def calcular_metricas(filas):
    """Calcula mínimo, máximo y promedio de las columnas Edad y Tarifa."""
    edades = [f["Edad"] for f in filas]
    tarifas = [f["Tarifa"] for f in filas]
    
    if not edades or not tarifas:
        return {}

    metricas = {
        "Edad_min": min(edades),
        "Edad_max": max(edades),
        "Edad_promedio": round(sum(edades) / len(edades), 2),
        "Tarifa_min": min(tarifas),
        "Tarifa_max": max(tarifas),
        "Tarifa_promedio": round(sum(tarifas) / len(tarifas), 2)
    }
    return metricas

def guardar_reporte(metricas, archivo_salida="reporte_limpio.csv"):
    """Guarda las métricas calculadas en un nuevo archivo CSV."""
    if not metricas:
        print("No hay métricas para guardar.")
        return
    try:
        with open(archivo_salida, mode="w", newline="", encoding="utf-8") as f:
            campos = list(metricas.keys())
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()
            escritor.writerow(metricas)
        print(f"Reporte guardado exitosamente en '{archivo_salida}'.")
    except Exception as e:
        print(f"Error al guardar reporte: {e}")

if __name__ == "__main__":
    print("Descargando datos...")
    contenido = descargar_csv(URL_CSV)
    
    if contenido:
        print("Procesando datos...")
        datos_limpios = procesar_filas(contenido)
        print(f"Se procesaron {len(datos_limpios)} filas válidas.")
        
        metricas = calcular_metricas(datos_limpios)
        
        print("\n=== REPORTE DE MÉTRICAS ===")
        print(f"Edades -> Min: {metricas['Edad_min']}, Max: {metricas['Edad_max']}, Promedio: {metricas['Edad_promedio']}")
        print(f"Tarifas -> Min: {metricas['Tarifa_min']}, Max: {metricas['Tarifa_max']}, Promedio: {metricas['Tarifa_promedio']}\n")
        
        guardar_reporte(metricas)
