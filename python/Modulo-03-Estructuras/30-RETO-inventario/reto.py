import copy

tienda = {
    "nombre": "Pociones Mágicas",
    "coordenadas": (42, 108),
    "productos": ["Poción Roja", "Poción Azul"],
    "clientes_vip": {"Mago Gandalf", "Rey Arturo"}
}

tienda["clientes_vip"].add("Reina Reina")
tienda["productos"].append("Poción Verde")

tienda_franquicia = copy.deepcopy(tienda)
tienda_franquicia["nombre"] = "Pociones Mágicas - Sur"
tienda_franquicia["productos"].remove("Poción Roja")

print(tienda)
print(tienda_franquicia)
