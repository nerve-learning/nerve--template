from abc import ABC, abstractmethod

class CentroControl:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def iniciar_lanzamiento(self):
        print("🎙️ Centro de Control: Iniciando secuencia de despegue...")

class Nave(ABC):
    _naves_creadas = 0

    def __init__(self, nombre, combustible):
        self.nombre = nombre
        self.__combustible = combustible
        Nave._naves_creadas += 1

    @classmethod
    def total_naves(cls):
        return cls._naves_creadas

    @property
    def combustible(self):
        return self.__combustible

    @abstractmethod
    def despegar(self):
        pass

    def __str__(self):
        return f"🛸 Nave {self.nombre} - Combustible: {self.combustible}%"

class Explorador(Nave):
    def despegar(self):
        print(f"🛰️ {self.nombre} encendiendo motores ligeros. ¡Hacia las estrellas!")

class Carguero(Nave):
    def despegar(self):
        print(f"🚀 {self.nombre} encendiendo propulsores pesados. ¡Levantando carga!")

centro = CentroControl()
centro.iniciar_lanzamiento()

voyager = Explorador("Voyager", 100)
titan = Carguero("Titan", 80)

print(f"Total de naves listas: {Nave.total_naves()}")
print(voyager)
print(titan)

voyager.despegar()
titan.despegar()
