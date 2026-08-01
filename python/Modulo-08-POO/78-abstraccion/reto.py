from abc import ABC, abstractmethod

class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, cantidad):
        pass

class TarjetaCredito(MetodoPago):
    def procesar_pago(self, cantidad):
        print(f"💳 Cobrando ${cantidad} de la tarjeta de crédito.")

class Paypal(MetodoPago):
    def procesar_pago(self, cantidad):
        print(f"📧 Transfiriendo ${cantidad} desde la cuenta de Paypal.")

tarjeta = TarjetaCredito()
paypal = Paypal()

tarjeta.procesar_pago(150)
paypal.procesar_pago(50)
