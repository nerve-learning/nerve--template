import pytest

def transferir_dinero(saldo_origen: float, cantidad: float, funcion_cobro) -> str:
    """
    Transfiere dinero desde un saldo de origen llamando a una funcion de cobro.

    Args:
        saldo_origen: El saldo disponible en la cuenta origen.
        cantidad: La cantidad de dinero a transferir.
        funcion_cobro: La funcion encargada de procesar el cobro.

    Returns:
        Un mensaje indicando el estado del proceso.
    """
    if cantidad > saldo_origen:
        return "Saldo insuficiente"
    
    resultado = funcion_cobro(cantidad)
    
    if resultado == True:
        return "Transferencia exitosa"
    else:
        return "Error en el banco"

@pytest.fixture
def saldo_rico() -> float:
    return 1000.0

@pytest.mark.parametrize("monto_gigante", [1500.0, 5000.0, 1000.1])
def test_fondos_insuficientes(monto_gigante: float, saldo_rico: float):
    def cobro_falso(monto):
        return False
    
    resultado = transferir_dinero(saldo_rico, monto_gigante, cobro_falso)
    assert resultado == "Saldo insuficiente"

def test_transferencia_correcta(saldo_rico: float):
    def cobro_falso_exitoso(monto):
        return True
    
    resultado = transferir_dinero(saldo_rico, 100.0, cobro_falso_exitoso)
    assert resultado == "Transferencia exitosa"
