class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def arrancar(self):
        print(f"El vehículo {self.marca} está encendido.")

class Coche(Vehiculo):
    def arrancar(self):
        print(f"¡Brum brum! El coche {self.marca} ha arrancado.")

class Bicicleta(Vehiculo):
    def arrancar(self):
        print(f"¡Ring ring! La bicicleta {self.marca} está en marcha.")

mi_coche = Coche("Toyota")
mi_bici = Bicicleta("Trek")

mi_coche.arrancar()
mi_bici.arrancar()
