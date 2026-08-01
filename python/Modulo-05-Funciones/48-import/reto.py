from random import choice

def predecir_futuro():
    presagios = [
        "Lloverá oro mañana.",
        "Un dragón atacará al mediodía.",
        "Encontrarás la paz en tu interior.",
        "No salgas de casa hoy."
    ]
    return choice(presagios)

for _ in range(3):
    resultado = predecir_futuro()
    print("El oráculo ha hablado:", resultado)
