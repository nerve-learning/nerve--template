monedas_totales = 0

def encontrar_cofre(cantidad):
    global monedas_totales
    monedas_totales += cantidad
    print(f"¡Encontraste {cantidad} monedas!")

def comprar_pocion(costo):
    global monedas_totales
    if monedas_totales >= costo:
        monedas_totales -= costo
        print(f"Poción comprada por {costo} monedas.")
    else:
        print("No tienes suficiente oro para la poción.")

encontrar_cofre(50)
comprar_pocion(20)
comprar_pocion(40)
print(f"Oro restante: {monedas_totales}")
