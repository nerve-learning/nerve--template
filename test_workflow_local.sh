#!/usr/bin/env bash
# ============================================================
# Simula localmente el workflow de evaluación de retos
# Uso:
#   ./test_workflow_local.sh <carpeta_del_reto> [reto.py_de_prueba]
#
# Ejemplos:
#   ./test_workflow_local.sh python/Modulo-01-Fundamentos/01-hola-mundo
#   ./test_workflow_local.sh python/Modulo-01-Fundamentos/05-aritmetica
# ============================================================

set -e

NERVE_COMMUNITY="/media/alejandro/D/tool/nerve-community"

if [ -z "$1" ]; then
  echo "Uso: $0 <carpeta_del_reto>"
  echo "Ejemplo: $0 python/Modulo-01-Fundamentos/01-hola-mundo"
  exit 1
fi

CARPETA="$1"
nivel=$(basename "$CARPETA")
modulo=$(basename "$(dirname "$CARPETA")")

echo ""
echo "======================================================"
echo "  TEST LOCAL — $modulo / $nivel"
echo "======================================================"

# Verificar que la carpeta existe
if [ ! -d "$CARPETA" ]; then
  echo "Error: carpeta '$CARPETA' no encontrada"
  exit 1
fi

# Buscar el test_main.py oficial en nerve-community
TEST_OFICIAL="$NERVE_COMMUNITY/$CARPETA/test_main.py"
if [ ! -f "$TEST_OFICIAL" ]; then
  echo "Sin test_main.py oficial para este nivel en nerve-community."
  echo "Ruta buscada: $TEST_OFICIAL"
  exit 1
fi

echo "test_main.py oficial encontrado."
echo ""

# Copiar temporalmente
cp "$TEST_OFICIAL" "$CARPETA/test_main.py"

# Instalar dependencias si hay requirements.txt
if [ -f "$CARPETA/requirements.txt" ]; then
  echo "Instalando dependencias..."
  pip3 install -q -r "$CARPETA/requirements.txt"
fi

# Ejecutar
echo "--- Ejecutando pytest ---"
python3 -m pytest "$CARPETA/test_main.py" -v --tb=short

EXIT_CODE=$?

# Borrar el test (igual que en CI)
rm "$CARPETA/test_main.py"

echo ""
if [ $EXIT_CODE -eq 0 ]; then
  echo "RESULTADO: APROBADO"

  # Simular detección de desbloqueo
  declare -A DESBLOQUEOS=(
    ["10-RETO-ficha"]="Modulo-02-Flujo"
    ["20-RETO-portero"]="Modulo-03-Estructuras"
    ["30-RETO-inventario"]="Modulo-04-Bucles + Modulo-04.5-Iteracion-Avanzada"
    ["40-RETO-analizador"]="Modulo-05-Funciones"
    ["50-RETO-calculadora"]="Modulo-05.5-Calidad-de-Codigo + Modulo-06-OS"
    ["60-RETO-organizador"]="Modulo-07-Web-APIs + Modulo-07.5-Programacion-Asincrona"
    ["70-RETO-monitor"]="Modulo-08-POO"
    ["80-RETO-ecosistema"]="Modulo-09-Data-IA"
    ["90-RETO-predictor"]="Modulo-10-Nerve"
    ["100-topologia-red"]="Modulo-11-Herramientas-Nerve"
    ["110-asociacion-archivos"]="Modulo-12-Arquitectura-Avanzada"
    ["120-RETO-FINAL-DISTRIBUIDO"]="COMPLETADO"
  )

  if [ -n "${DESBLOQUEOS[$nivel]+_}" ]; then
    echo ""
    echo "Este reto desbloquea: ${DESBLOQUEOS[$nivel]}"
    echo "(En CI real, el siguiente modulo apareceria automaticamente en tu repo)"
  fi
else
  echo "RESULTADO: REPROBADO — revisa los errores arriba"
fi

exit $EXIT_CODE
