class Platillo:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

mi_cena = Platillo("Pizza Familiar", 15)
print(mi_cena)
