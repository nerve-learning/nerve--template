noticias_brutas = [
    "  DEPORTES: el equipo local gano el campeonato  ",
    "  POLITICA: nueva ley aprobada por el congreso  ",
    "  DEPORTES: jugador estrella firma contrato millonario  ",
    "  ECONOMIA: el peso se fortalece ante el dolar  ",
    "  DEPORTES: el torneo comienza el proximo lunes  ",
    "  POLITICA: candidatos debaten temas de seguridad  ",
    "  ECONOMIA: inflacion baja por tercer mes consecutivo  ",
    "  DEPORTES: seleccion nacional convoca 23 jugadores  ",
]

def limpiar_noticia(noticias):
    for noticia in noticias:
        yield noticia.strip().title()

def filtrar_categoria(noticias_limpias, categoria):
    for noticia in noticias_limpias:
        if noticia.startswith(categoria):
            yield noticia

def formatear_titular(noticias_filtradas):
    for noticia in noticias_filtradas:
        yield f"🏆 {noticia.upper()} → publicada"

pipeline = formatear_titular(filtrar_categoria(limpiar_noticia(noticias_brutas), "Deportes:"))

print("=== Titulares de Deportes — Edición de Hoy ===\n")
contador = 0
for titular in pipeline:
    print(titular)
    contador = contador + 1

print(f"\nTotal de titulares de Deportes publicados hoy: {contador}")
