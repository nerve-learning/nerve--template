salud_optima = True
puntuacion_psicologica = 85

if salud_optima:
    if puntuacion_psicologica >= 90:
        print("¡Felicidades! Eres el nuevo astronauta para ir a Marte.")
    else:
        print("Rechazado en fase 2: Excelente físico, pero no pasó el test psicológico.")
else:
    print("Rechazado en fase 1: No cumple los requisitos físicos.")
