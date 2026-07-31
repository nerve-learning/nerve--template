registro_temperaturas = [22, 25, 31, 15, 29, 50, 20, 22]
reporte_maquina = {"Normal": 0, "Alerta": 0, "Peligro": 0}
print("--- Iniciando análisis del motor ---")
for temp in registro_temperaturas:
    if temp <= 29:
        reporte_maquina["Normal"] = reporte_maquina["Normal"] + 1
    elif temp <= 49:
        reporte_maquina["Alerta"] = reporte_maquina["Alerta"] + 1
    elif temp == 50:
        print("¡FUSIÓN DEL NÚCLEO DETECTADA! Apagando...")
        reporte_maquina["Peligro"] = reporte_maquina["Peligro"] + 1
        break
print("--- Análisis finalizado ---")
print(reporte_maquina)
