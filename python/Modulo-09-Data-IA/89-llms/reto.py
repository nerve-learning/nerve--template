# Copyright (C) 2026 Alenia Studios
# SPDX-License-Identifier: GPL-3.0-or-later

import time

def oraculo_clima(prompt):
    time.sleep(1)
    prompt_limpio = prompt.lower()
    if "madrid" in prompt_limpio:
        return "En Madrid hará sol, 25 grados."
    elif "londres" in prompt_limpio:
        return "En Londres lloverá, no olvides tu paraguas."
    else:
        return "Lo siento, mis satélites no llegan ahí aún."

print("Consultando a los astros por Madrid...")
print(f"🤖 Oráculo: {oraculo_clima('Madrid')}")
print()

print("Consultando a los astros por Londres...")
print(f"🤖 Oráculo: {oraculo_clima('Londres')}")
print()

print("Consultando a los astros por Bogotá...")
print(f"🤖 Oráculo: {oraculo_clima('Bogotá')}")
