edad_cliente = 19
dia_actual = "viernes"
es_vip = False
ropa = "deportiva"

if edad_cliente < 18:
    print("Rechazado: Eres menor de edad.")
else:
    if dia_actual == "lunes" or dia_actual == "martes" or dia_actual == "miércoles":
        print("Rechazado: El club está cerrado hoy.")
    else:
        if es_vip:
            print("¡Bienvenido, VIP! Pase usted.")
        else:
            if ropa == "elegante" or ropa == "casual":
                print("Bienvenido. Son 20 dólares de cover.")
            else:
                print("Rechazado: No cumples el código de vestimenta.")
