class Cine:
    def __init__(self):
        self.__edad_cliente = 0

    @property
    def edad(self):
        return self.__edad_cliente

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad < 18:
            print("Acceso denegado. Eres menor de edad.")
        else:
            self.__edad_cliente = nueva_edad
            print("Acceso concedido. Disfruta la película.")

mi_cine = Cine()
mi_cine.edad = 15
mi_cine.edad = 20
