# Copyright (C) 2026 Alenia Studios
# SPDX-License-Identifier: GPL-3.0-or-later

import pandas as pd

boleta_calificaciones = {
    "Alumno": ["Juan", "Maria", "Pedro"],
    "Matematicas": [85, 95, 70],
    "Historia": [90, 88, 75]
}

registro_oficial = pd.DataFrame(boleta_calificaciones)
print(registro_oficial)
