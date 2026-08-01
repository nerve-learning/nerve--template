# Copyright (C) 2026 Alenia Studios
# SPDX-License-Identifier: GPL-3.0-or-later

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

temperaturas = [[15], [20], [25], [30]]
vasos_reales = [10, 22, 35, 48]

modelo = LinearRegression()
modelo.fit(temperaturas, vasos_reales)

predicciones = modelo.predict(temperaturas)

plt.scatter(temperaturas, vasos_reales)
plt.plot(temperaturas, predicciones)
plt.show()
