# Copyright (C) 2026 Alenia Studios
# SPDX-License-Identifier: GPL-3.0-or-later

from sklearn.linear_model import LinearRegression

print("Entrenando al tasador automático...")
tamaños = [[50], [80], [100], [150]]
precios = [100, 160, 200, 300]

modelo = LinearRegression()
modelo.fit(tamaños, precios)
print("¡Entrenamiento completado!")

print("Calculando precio para una casa de 120 metros cuadrados...")
prediccion = modelo.predict([[120]])

print(f"🔮 El precio sugerido es: ${prediccion[0]} miles de dólares.")
