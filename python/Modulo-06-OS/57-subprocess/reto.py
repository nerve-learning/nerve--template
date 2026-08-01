import subprocess
import sys

# Imprimimos mensaje inicial
print("Solicitando un cálculo al subproceso...")

# Usamos sys.executable para que funcione correctamente tanto en Windows como en Linux (donde 'python' no existe y se usa 'python3')
comando = [sys.executable, "-c", "print(100 + 150)"]

# Ejecutamos el subproceso capturando la salida como texto
resultado = subprocess.run(comando, capture_output=True, text=True)

# Imprimimos la respuesta
print("El subproceso respondió que el resultado es:")
print(resultado.stdout.strip())
