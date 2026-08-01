import os
import sys
import subprocess
import time

def mostrar_instrucciones():
    print("========================================")
    print("    RED DE SCRIPTS CON NERVE (RETO 02)  ")
    print("========================================")
    print("Este reto consta de 4 componentes que deben ejecutarse simultáneamente:")
    print("1. hub.py        (El servidor central de Nerve)")
    print("2. monitor.py    (El dashboard en tiempo real)")
    print("3. procesador.py (El nodo que transforma los datos)")
    print("4. productor.py  (El nodo que genera los datos)")
    print("")
    print("INSTRUCCIONES PARA PROBAR:")
    print("Para ver la resiliencia del sistema, abre 4 terminales diferentes y ejecuta:")
    print("Terminal 1: python hub.py")
    print("Terminal 2: python monitor.py")
    print("Terminal 3: python procesador.py")
    print("Terminal 4: python productor.py")
    print("")
    print("Prueba cerrar (Ctrl+C) el productor o el procesador, espera unos")
    print("segundos, y vuelve a iniciarlos. ¡El sistema se reconectará automáticamente!")
    print("========================================")

if __name__ == "__main__":
    mostrar_instrucciones()
