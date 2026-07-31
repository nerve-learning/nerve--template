def maquina_turnos(inicio):
    turno = inicio
    while True:
        yield turno
        turno = turno + 1

consultorio = maquina_turnos(1)
print("🏥 Sistema de Turnos — Consultorio 1\n")
print(f"Llamando al paciente con turno: {next(consultorio)}")
print(f"Llamando al paciente con turno: {next(consultorio)}")
print(f"Llamando al paciente con turno: {next(consultorio)}")
print(f"Llamando al paciente con turno: {next(consultorio)}")
print(f"Llamando al paciente con turno: {next(consultorio)}")
