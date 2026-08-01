# Copyright (C) 2026 Alenia Studios
# SPDX-License-Identifier: GPL-3.0-or-later

import pandas as pd

inventario_sucio = {
    "Zapato": ["Tenis", "Bota", "Sandalia", "Mocasín"],
    "Precio": [50, None, 15, None]
}

tabla_inventario = pd.DataFrame(inventario_sucio)
tabla_salvada = tabla_inventario.fillna(10)
print(tabla_salvada)
