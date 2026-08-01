class BovedaCentral:
    _unica_boveda = None

    def __new__(cls):
        if cls._unica_boveda is None:
            cls._unica_boveda = super().__new__(cls)
        return cls._unica_boveda

    def __init__(self):
        if not hasattr(self, 'dinero_total'):
            self.dinero_total = 0

    def depositar(self, cantidad):
        self.dinero_total += cantidad

sucursal_norte = BovedaCentral()
sucursal_sur = BovedaCentral()

sucursal_norte.depositar(500)
sucursal_sur.depositar(300)

print("Dinero en la sucursal sur:", sucursal_sur.dinero_total)
