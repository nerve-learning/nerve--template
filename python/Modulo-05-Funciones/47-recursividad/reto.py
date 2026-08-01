def hacer_eco(palabra, veces):
    if veces == 0:
        print("...")
        return
    print(palabra)
    hacer_eco(palabra, veces - 1)

hacer_eco("¡Hola!", 3)
