class CuentaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Depositaste {cantidad}. Saldo actual: {self.saldo}")

cuenta_batman = CuentaBancaria("Batman")
cuenta_batman.depositar(500)
cuenta_batman.depositar(1000)
