# Copyright (C) 2026 Alenia Studios
# SPDX-License-Identifier: GPL-3.0-or-later

from sklearn.linear_model import LinearRegression

grados_pasado = [[10], [20], [30]]
ventas_pasado = [20, 40, 60]

modelo = LinearRegression()
modelo.fit(grados_pasado, ventas_pasado)

prediccion = modelo.predict([[40]])
print(prediccion)
