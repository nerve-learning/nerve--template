def guardar_progreso(personaje, *objetos, **estadisticas):
    print("Guardando progreso de:", personaje)
    print("--- Objetos en la mochila ---")
    for objeto in objetos:
        print("-", objeto)
    print("--- Estadísticas ---")
    for etiqueta in estadisticas:
        print(etiqueta, ":", estadisticas[etiqueta])

guardar_progreso("Geralt", "Espada de Plata", "Poción Curativa", "Cabeza de Grifo", fuerza=150, magia=50, agilidad=80)
