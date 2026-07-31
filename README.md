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
con una Pull Request. Es más trabajo escribir esto que hacerlo: son 4
comandos y un botón.

1. **Crea una rama** para el reto (puedes nombrarla como quieras, por
   ejemplo el nombre del nivel):
   ```
   git checkout -b 01-hola-mundo
   ```
2. **Resuelve el reto**, guarda el archivo, y sube tu rama:
   ```
   git add .
   git commit -m "resuelvo 01-hola-mundo"
   git push origin 01-hola-mundo
   ```
3. **Abre el Pull Request**: GitHub te va a mostrar un aviso con un
   botón "Compare & pull request" apenas hagas push — dale clic y
   confirma. También puedes abrirlo manualmente desde la pestaña
   "Pull requests" del repo.
4. **Espera el comentario del bot**: en unos segundos el bot va a
   comentar directo en tu Pull Request si tu reto pasó o no —
   no necesitas revisar logs. Si algo falló, el comentario te dice
   exactamente qué.
5. **Corrige si hace falta**: si el comentario dice que reprobaste,
   corrige `reto.py` en tu misma rama, vuelve a hacer commit y push
   — el mismo Pull Request se vuelve a evaluar solo, sin que tengas
   que abrir uno nuevo.
6. **Mergea el Pull Request** cuando el comentario diga que aprobaste.
   Ahí es cuando se desbloquea el siguiente módulo o glosario, si
   corresponde.

> Guía visual paso a paso de todo este flujo (rama, push, PR,
> comentario del bot, merge) en el repo
> [nerve-community](https://github.com/nerve-learning/nerve-community),
> carpeta `Assets/`.

## Reglas

- Solo crea/edita el archivo que pide el `reto.md` (casi siempre es `reto.py`)
- Los tests se descargan del servidor en el momento del Pull Request — no tienes acceso a ellos
- Un reto está aprobado cuando el bot comenta ✅ APROBADO en tu Pull Request
- Un push directo a `main` no se evalúa y no desbloquea nada — siempre usa Pull Request
- Cuando termines el **RETO final** de un módulo y mergees el Pull Request,
  el siguiente módulo aparecerá automáticamente en tu repositorio

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
