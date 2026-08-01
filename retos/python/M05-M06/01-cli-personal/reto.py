import sys
import json
import os

ARCHIVO_DATOS = "tareas.json"

def cargar_datos():
    """Carga los datos desde el archivo JSON o devuelve una lista vacía."""
    if not os.path.exists(ARCHIVO_DATOS):
        return []
    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def guardar_datos(datos):
    """Guarda la lista de datos en el archivo JSON."""
    try:
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error al guardar: {e}")

def add_tarea(tarea):
    """Añade una nueva tarea a la lista y la guarda."""
    datos = cargar_datos()
    datos.append(tarea)
    guardar_datos(datos)
    print(f"Tarea añadida: '{tarea}'")

def list_tareas():
    """Muestra todas las tareas guardadas actualmente."""
    datos = cargar_datos()
    if not datos:
        print("No hay tareas guardadas.")
        return
    print("=== TAREAS ===")
    for i, t in enumerate(datos):
        print(f"{i + 1}. {t}")

def remove_tarea(indice):
    """Elimina una tarea según su índice (1-based)."""
    datos = cargar_datos()
    try:
        idx = int(indice) - 1
        if 0 <= idx < len(datos):
            removida = datos.pop(idx)
            guardar_datos(datos)
            print(f"Tarea eliminada: '{removida}'")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("El índice debe ser un número entero.")

def mostrar_ayuda():
    """Muestra la ayuda de uso de la CLI."""
    print("Uso: python reto.py [comando] [argumentos]")
    print("Comandos disponibles:")
    print("  add <tarea>    - Añade una nueva tarea")
    print("  list           - Lista todas las tareas")
    print("  remove <num>   - Elimina la tarea por número")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        mostrar_ayuda()
    else:
        comando = sys.argv[1]
        try:
            if comando == "add":
                if len(sys.argv) >= 3:
                    add_tarea(" ".join(sys.argv[2:]))
                else:
                    print("Error: Falta la descripción de la tarea.")
            elif comando == "list":
                list_tareas()
            elif comando == "remove":
                if len(sys.argv) >= 3:
                    remove_tarea(sys.argv[2])
                else:
                    print("Error: Falta el número de la tarea a eliminar.")
            else:
                print("Comando desconocido.")
                mostrar_ayuda()
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")
