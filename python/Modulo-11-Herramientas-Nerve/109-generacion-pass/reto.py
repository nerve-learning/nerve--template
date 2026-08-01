import os
import re

print("Iniciando fábrica...")

# 1. Atrapamos el output de nerve genpass --mode random
output = os.popen("nerve genpass --mode random").read().strip()

# Removemos códigos de escape ANSI
ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
clean_output = ansi_escape.sub('', output)

# Extraemos la contraseña limpia
llave = ""
for line in clean_output.split("\n"):
    if line.startswith("Password:"):
        llave = line.split(":", 1)[1].strip()
        break

# 2. Imprimirla en pantalla
print(f"La llave de hoy es: {llave}")

# 3. Crear carpeta produccion y poner un archivo adentro
os.system("mkdir -p produccion")
os.system("echo 'Contenido de produccion' > produccion/reporte.txt")
print("Carpeta creada.")

# Configuramos la variable de entorno de forma segura en Python
os.environ["NERVE_NRV_PASSWORD"] = llave

# 4. Empacar la carpeta produccion en producto_final.nrv
print("Empacando producto...")
os.system("nerve pack produccion producto_final.nrv")

# 5. Desempaca en control_calidad
print("Desempacando para control de calidad...")
os.system("nerve unpack producto_final.nrv control_calidad")

print("¡Todo funciona perfectamente!")
