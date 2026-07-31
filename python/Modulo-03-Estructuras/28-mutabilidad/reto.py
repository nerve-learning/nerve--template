sospechosos_fbi = ["Zorro", "Halcón", "Cuervo"]
copia_novato = sospechosos_fbi

copia_novato.remove("Halcón")
print("¡Desastre! La base del FBI ahora es:")
print(sospechosos_fbi)

sospechosos_fbi = ["Zorro", "Halcón", "Cuervo"]
copia_experto = sospechosos_fbi[:]

copia_experto.remove("Halcón")
print("Base de datos segura:")
print(sospechosos_fbi)
