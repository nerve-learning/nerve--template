# Copyright (C) 2026 Alenia Studios
# SPDX-License-Identifier: GPL-3.0-or-later

from sklearn.feature_extraction.text import CountVectorizer

resenas = [
    "La comida es excelente",
    "La comida es terrible",
    "Excelente servicio"
]

traductor = CountVectorizer()
matriz_numeros = traductor.fit_transform(resenas)
print(matriz_numeros.toarray())
