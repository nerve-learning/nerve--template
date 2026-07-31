# Nerve — Tu espacio de aprendizaje

Este repositorio fue generado para ti. Aquí resolverás los retos
de cada módulo de Python a tu ritmo.

## Cómo funciona

1. Ve a la carpeta del nivel que te toca (ej. `python/Modulo-01-Fundamentos/01-hola-mundo/`)
2. Lee `README.md` y `teoria.md` para entender el concepto
3. Estudia `ejemplo.py` para ver cómo funciona
4. Lee `reto.md` — ahí está tu misión
5. Crea el archivo `reto.py` y resuélvelo
6. Entrégalo con una Pull Request (ver abajo)

## Cómo entregar un reto (Pull Request)

Tus retos **no se evalúan con un push directo a `main`** — se entregan
con una Pull Request. Usas **una sola rama de trabajo para todo el
curso** (no una rama nueva por cada nivel — con 135 retos eso sería un
desastre). La llamamos `trabajo`, pero puedes ponerle el nombre que
quieras, siempre y cuando sea siempre la misma.

### La primera vez (una sola vez, al inicio del curso)

```
git checkout -b trabajo
```

### Para cada nivel, repite este ciclo

1. **Sincroniza tu rama con `main`** antes de empezar — esto trae
   cualquier módulo o glosario que se haya desbloqueado desde tu
   último reto:
   ```
   git checkout trabajo
   git pull origin main
   ```
2. **Resuelve el reto**, guarda el archivo, y sube tu rama:
   ```
   git add .
   git commit -m "resuelvo 01-hola-mundo"
   git push origin trabajo
   ```
3. **Abre el Pull Request**: GitHub te muestra un aviso con el botón
   "Compare & pull request" apenas hagas push — dale clic y confirma.
   Esto pasa de nuevo en cada nivel, aunque ya hayas abierto y
   mergeado un PR desde esta misma rama antes; es normal, cada push
   nuevo habilita un PR nuevo.
4. **Espera el comentario del bot**: en unos segundos el bot va a
   comentar directo en tu Pull Request si tu reto pasó o no —
   no necesitas revisar logs. Si algo falló, el comentario te dice
   exactamente qué.
5. **Corrige si hace falta**: si el comentario dice que reprobaste,
   corrige `reto.py` en la misma rama (`trabajo`), vuelve a hacer
   commit y push — el mismo Pull Request se vuelve a evaluar solo,
   sin que tengas que abrir uno nuevo.
6. **Mergea el Pull Request** cuando el comentario diga que aprobaste.
   Ahí es cuando se desbloquea el siguiente módulo o glosario, si
   corresponde.
7. **Vuelve al paso 1** para el siguiente nivel — sincroniza `trabajo`
   con `main` de nuevo antes de empezar. Ese `pull` es el que te trae
   el módulo nuevo a tu carpeta local (el bot lo crea directo en
   GitHub, no aparece solo en tu copia local hasta que haces pull).

> ⚠️ **Importante:** no todos los niveles desbloquean algo — solo el
> **RETO final de cada módulo**. Cuando mergees ese RETO final, el
> bot crea el módulo siguiente (y a veces un glosario nuevo)
> **directo en GitHub, en la nube** — ahí lo vas a ver de inmediato
> en la pestaña "Code" del repo. Tu carpeta local **no se entera
> sola**: siempre que termines el RETO final de un módulo, haz
> `git pull origin main` en tu rama `trabajo` antes de seguir, o vas
> a estar buscando una carpeta que en tu computadora todavía no existe.

> Guía visual paso a paso de todo este flujo (rama, push, PR,
> comentario del bot, merge) en el repo
> [nerve-community](https://github.com/nerve-learning/nerve-community),
> carpeta `Assets/`.

## Reglas

- Solo crea/edita el archivo que pide el `reto.md` (casi siempre es `reto.py`)
- Los tests se descargan del servidor en el momento del Pull Request — no tienes acceso a ellos
- Un reto está aprobado cuando el bot comenta ✅ APROBADO en tu Pull Request
- Un push directo a `main` no se evalúa y no desbloquea nada — siempre usa Pull Request
- Usa siempre la misma rama de trabajo (`trabajo`) para todos los niveles —
  no crees una rama nueva por cada reto
- **No borres la rama `trabajo` después de mergear** — GitHub te va a
  ofrecer un botón "Delete branch" apenas el PR se mergea; ignóralo,
  la necesitas para el siguiente nivel
- Cuando termines el **RETO final** de un módulo y mergees el Pull Request,
  el siguiente módulo aparecerá automáticamente en tu repositorio de GitHub —
  haz `git pull origin main` en tu rama `trabajo` para verlo ahí también

## Estructura de cada nivel

```
01-hola-mundo/
  README.md     ← portada del nivel
  teoria.md     ← explicación del concepto
  ejemplo.py    ← código de demostración (solo leer)
  reto.md       ← tu misión
  reto.py       ← lo creas tú aquí
```

## Progreso de módulos

Al inicio solo tienes **Módulo 01**. Cada módulo nuevo se desbloquea
cuando apruebas el reto final del módulo anterior.

| Módulo | Desbloquea con |
|--------|----------------|
| Módulo 01 — Fundamentos | disponible desde el inicio |
| Módulo 02 — Flujo | aprobar `10-RETO-ficha` |
| Módulo 03 — Estructuras | aprobar `20-RETO-portero` |
| Módulo 04 — Bucles + 04.5 Iteración | aprobar `30-RETO-inventario` |
| Módulo 05 — Funciones | aprobar `40-RETO-analizador` |
| Módulo 05.5 — Calidad + 06 OS | aprobar `50-RETO-calculadora` |
| Módulo 07 — Web APIs + 07.5 Async | aprobar `60-RETO-organizador` |
| Módulo 08 — POO | aprobar `70-RETO-monitor` |
| Módulo 09 — Data & IA | aprobar `80-RETO-ecosistema` |
| Módulo 10 — Nerve | aprobar `90-RETO-predictor` |
| Módulo 11 — Herramientas | aprobar `100-topologia-red` |
| Módulo 12 — Arquitectura Avanzada | aprobar `110-asociacion-archivos` |