import os

# Averigua en qué dirección estás parado y guárdala en una variable llamada ruta_secreta
ruta_secreta = os.getcwd()

# Imprime tu ruta secreta para confirmar dónde estás
print("Mi ruta secreta es:", ruta_secreta)

# Usa la herramienta para ver qué cosas hay a tu alrededor y guárdalas en una lista llamada inventario
inventario = os.listdir(ruta_secreta)

# Crea una función (usando def) llamada inspeccionar_tesoros(lista_de_cosas) que reciba una lista como parámetro
def inspeccionar_tesoros(lista_de_cosas):
    # Dentro de la función, usa un bucle for para analizar cada cosa de la lista
    for cosa in lista_de_cosas:
        # La regla del tesoro: verifica si la primera letra del nombre del objeto es la letra "e"
        if cosa[0] == "e":
            print("¡Tesoro especial encontrado:", cosa + "!")
        else:
            print("Solo es basura:", cosa)

# Finalmente, llama a tu función pasándole tu lista inventario como parámetro
inspeccionar_tesoros(inventario)
