opcion_teclado = 2

match opcion_teclado:
    case 1:
        print("Lo estamos comunicando con el departamento de Ventas.")
    case 2:
        print("Lo estamos comunicando con Soporte Técnico.")
    case 3:
        print("Lo estamos comunicando con Cobranza.")
    case 4:
        print("Gracias por llamar. Colgando la llamada...")
    case _:
        print("Opción inválida. Por favor, marque un número del 1 al 4.")
