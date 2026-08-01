texto = """En un lugar de la Mancha de cuyo nombre no quiero acordarme no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero adarga antigua rocín flaco y galgo corredor
Una olla de algo más vaca que carnero salpicón las más noches duelos y quebrantos los sábados lentejas los viernes algún palomino de añadidura los domingos consumían las tres partes de su hacienda
El resto della concluían sayo de velarte calzas de velludo para las fiestas con sus pantuflos de lo mismo los días de entre semana se honraba con su vellorí de lo más fino
Tenía en su casa una ama que pasaba de los cuarenta y una sobrina que no llegaba a los veinte y un mozo de campo y plaza que así ensillaba el rocín como tomaba la podadera"""

palabras_crudas = texto.lower().split()
palabras = [p for p in palabras_crudas if p.isalpha()]

total_palabras = len(palabras)
unicas = set(palabras)
total_unicas = len(unicas)
repetidas = total_palabras - total_unicas

mas_larga = ""
mas_corta = "x" * 100
for p in unicas:
    if len(p) > len(mas_larga): mas_larga = p
    if len(p) < len(mas_corta): mas_corta = p

frecuencias = {}
stop_words = {"el", "la", "de", "que", "y", "los", "las", "un", "una", "en", "con", "a", "su", "no", "se"}
for p in palabras:
    if p not in stop_words:
        frecuencias[p] = frecuencias.get(p, 0) + 1

def val(x): return x[1]
ordenadas = sorted(frecuencias.items(), key=val, reverse=True)
top_5 = ordenadas[:5]

es_rico = total_unicas > (total_palabras / 2)
tipo_texto = "Rico" if es_rico else "Repetitivo"

print("=== REPORTE DE TEXTO ===")
print(f"Total de palabras: {total_palabras}")
print(f"Palabras únicas: {total_unicas}")
print(f"Palabras repetidas: {repetidas}")
print(f"Palabra más larga: '{mas_larga}'")
print(f"Palabra más corta: '{mas_corta}'")
print("\nTop 5 palabras más frecuentes (sin stop words):")
for p, c in top_5:
    print(f"- {p}: {c} veces")
print(f"\nEl texto es: {tipo_texto}")
