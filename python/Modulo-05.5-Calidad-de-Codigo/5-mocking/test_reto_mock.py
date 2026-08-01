def cobrar_a_banco_real():
    print("¡COBRANDO 100 DÓLARES AL BANCO!")
    return "Pagado"

def finalizar_compra(carrito: list, funcion_cobro = cobrar_a_banco_real) -> str:
    if len(carrito) == 0:
        return "Error: carrito vacio"
    
    estado_pago = funcion_cobro()
    
    if estado_pago == "Pagado":
        return "Compra exitosa"
    else:
        return "Error en el pago"

def test_finalizar_compra_con_exito():
    def cobro_falso_exitoso():
        return "Pagado"
    
    resultado = finalizar_compra(["Zapatos"], cobro_falso_exitoso)
    assert resultado == "Compra exitosa"

def test_finalizar_compra_rechazada():
    def cobro_falso_rechazado():
        return "Rechazado"
    
    resultado = finalizar_compra(["Zapatos"], cobro_falso_rechazado)
    assert resultado == "Error en el pago"
