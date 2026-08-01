coleccion = [
    {"titulo": "The Legend of Zelda", "genero": "Aventura", "año": 1986},
    {"titulo": "Super Mario Bros", "genero": "Plataformas", "año": 1985},
    {"titulo": "Final Fantasy VII", "genero": "RPG", "año": 1997},
    {"titulo": "Minecraft", "genero": "Sandbox", "año": 2011},
    {"titulo": "Chrono Trigger", "genero": "RPG", "año": 1995},
    {"titulo": "Tetris", "genero": "Puzzle", "año": 1984},
    {"titulo": "Portal", "genero": "Puzzle", "año": 2007},
    {"titulo": "Skyrim", "genero": "RPG", "año": 2011}
]

def f_año(item): return item["año"]
def f_gen(item): return item["genero"]

todos_titulos = [item["titulo"] for item in coleccion]
rpgs = [item["titulo"] for item in coleccion if item["genero"] == "RPG"]
ordenados_año = sorted(coleccion, key=f_año)

print("--- TODOS LOS ITEMS ---")
print(", ".join(todos_titulos))
print("\n--- SOLO JUEGOS RPG ---")
print(", ".join(rpgs))
print("\n--- ORDENADOS POR AÑO ---")
for j in ordenados_año:
    print(f"{j['titulo']} ({j['año']})")

total = len(coleccion)
mas_antiguo = min(coleccion, key=f_año)

conteo_generos = {}
for item in coleccion:
    g = item["genero"]
    conteo_generos[g] = conteo_generos.get(g, 0) + 1

max_g, max_c = "", 0
for g, c in conteo_generos.items():
    if c > max_c:
        max_c = c
        max_g = g

print("\n--- ESTADÍSTICAS ---")
print(f"Total de items: {total}")
print(f"Género más común: {max_g} ({max_c} juegos)")
print(f"Item más antiguo: {mas_antiguo['titulo']} ({mas_antiguo['año']})")
