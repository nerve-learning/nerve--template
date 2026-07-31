puntos = 150
tiempo_segundos = 45
enemigos_derrotados = True

supero_nivel = puntos > 100 and tiempo_segundos < 60

if supero_nivel and enemigos_derrotados:
    print("¡Trofeo Dorado desbloqueado!")
