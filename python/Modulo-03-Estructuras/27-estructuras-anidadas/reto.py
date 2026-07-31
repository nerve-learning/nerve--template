servidor = [
    {"id": 1, "datos": ["basura", "basura"]},
    {"id": 2, "datos": ["basura", "CONTRASEÑA_SECRETA"]}
]

print("--- INICIANDO HACKEO ---")
clave_extraida = servidor[1]["datos"][1]
print(clave_extraida)
