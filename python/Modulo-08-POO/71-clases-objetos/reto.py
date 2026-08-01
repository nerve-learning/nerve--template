class Monstruo:
    def __init__(self, nombre, asustador):
        self.nombre = nombre
        self.asustador = asustador

    def rugir(self):
        if self.asustador:
            print(f"¡ROAAAR! Soy {self.nombre} y doy mucho miedo.")
        else:
            print(f"Grrr... Soy {self.nombre} pero soy amigable.")

sulley = Monstruo("Sulley", True)
mike = Monstruo("Mike", False)

sulley.rugir()
mike.rugir()
