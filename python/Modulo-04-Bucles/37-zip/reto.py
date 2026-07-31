panes = ["blanco", "integral", "con ajonjolí"]
carnes = ["res", "pollo", "vegetariana"]
print("¡Ensamblando pedidos!")
for tipo_pan, tipo_carne in zip(panes, carnes):
    print("Hamburguesa lista de:")
    print(tipo_carne)
    print("en pan")
    print(tipo_pan)
print("¡Todos los pedidos entregados!")
