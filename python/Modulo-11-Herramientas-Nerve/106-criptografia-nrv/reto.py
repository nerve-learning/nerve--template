import os

print("¡Bienvenido a la Forja de Llaves!")
print("Generando llave de símbolos...")
os.system("nerve genpass --mode random")

print("--------------------------------")

print("Generando frase secreta fácil de recordar...")
os.system("nerve genpass --mode passphrase")
