import pytest

def calcular_total(precio: float, impuesto: float) -> float:
    return precio + (precio * impuesto)

@pytest.fixture
def impuesto_estandar() -> float:
    return 0.15

@pytest.mark.parametrize("precio_base", [100.0, 50.0, 200.0])
def test_calcular_total(precio_base: float, impuesto_estandar: float):
    total = calcular_total(precio_base, impuesto_estandar)
    assert total > precio_base
