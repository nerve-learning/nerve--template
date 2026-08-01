def calcular_dano(ataque, armadura):
    dano_final = ataque - armadura
    if dano_final < 0:
        dano_final = 0
    return dano_final

golpe_orco = calcular_dano(50, 30)
print(f"El Orco ataca! Daño infligido: {golpe_orco}")

golpe_duende = calcular_dano(10, 50)
print(f"El Duende ataca! Daño infligido: {golpe_duende}")
