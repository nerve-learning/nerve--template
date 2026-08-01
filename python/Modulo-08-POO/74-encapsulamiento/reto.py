class CajaFuerte:
    def __init__(self, contraseña):
        self.__contraseña = contraseña
        self.__dinero = 1000

    def abrir_caja(self, intento):
        if intento == self.__contraseña:
            print(f"🔓 Caja abierta. Tienes {self.__dinero} dólares.")
        else:
            print("🚨 ¡Alarma! Intruso detectado.")

mi_caja = CajaFuerte("secreto123")
mi_caja.abrir_caja("0000")
mi_caja.abrir_caja("secreto123")
