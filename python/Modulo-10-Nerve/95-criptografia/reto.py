import os
from nerve import pack_nrv

print("Iniciando protocolo de seguridad...")

base_dir = os.path.dirname(os.path.abspath(__file__))
archivo_txt = os.path.join(base_dir, "codigos_nucleares.txt")
caja_fuerte = os.path.join(base_dir, "boveda.nrv")
password = "alenia_secreto"

pack_nrv(archivo_txt, caja_fuerte, password)

print("Archivos encriptados con éxito en boveda.nrv")

if os.path.exists(archivo_txt):
    os.remove(archivo_txt)
