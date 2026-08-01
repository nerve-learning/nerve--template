# Copyright (C) 2026 Alenia Studios
# SPDX-License-Identifier: GPL-3.0-or-later

from sklearn.tree import DecisionTreeClassifier

X = [[0, 2], [1, 5], [10, 50], [15, 80]]
y = ["Normal", "Normal", "Spam", "Spam"]

modelo = DecisionTreeClassifier()
modelo.fit(X, y)

prediccion = modelo.predict([[12, 60]])
print(prediccion)
