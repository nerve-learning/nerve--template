import json
import requests
from bs4 import BeautifulSoup

URL = "https://nerve.community.aleniastudios.me"

class FilaTabla:
    def __init__(self, datos):
        self.datos = datos

    def coincide_filtro(self, columna, valor):
        columna = columna.lower()
        valor = str(valor).lower()
        for k, v in self.datos.items():
            if k.lower() == columna and valor in str(v).lower():
                return True
        return False

    def to_dict(self):
        return self.datos

def limpiar_texto(texto):
    """Quita espacios extra y saltos de línea."""
    return " ".join(texto.split())

def extraer_tabla(url):
    print(f"Obteniendo datos de {url} ...")
    respuesta = requests.get(url, timeout=10)
    respuesta.raise_for_status()
    
    soup = BeautifulSoup(respuesta.text, 'html.parser')
    tabla = soup.find('table')
    if not tabla:
        print("No se encontró ninguna tabla en la página.")
        return []

    encabezados = []
    thead = tabla.find('thead')
    if thead:
        for th in thead.find_all('th'):
            encabezados.append(limpiar_texto(th.get_text()))
    else:
        # Si no hay thead, intentamos con la primera fila
        primera_fila = tabla.find('tr')
        if primera_fila:
            for th in primera_fila.find_all(['th', 'td']):
                encabezados.append(limpiar_texto(th.get_text()))

    if not encabezados:
        encabezados = [f"Col_{i}" for i in range(20)] # Fallback

    filas_extraidas = []
    tbody = tabla.find('tbody')
    trs = tbody.find_all('tr') if tbody else tabla.find_all('tr')
    
    for tr in trs:
        tds = tr.find_all('td')
        if not tds:
            continue
        datos_fila = {}
        for i, td in enumerate(tds):
            col_name = encabezados[i] if i < len(encabezados) else f"Col_{i}"
            datos_fila[col_name] = limpiar_texto(td.get_text())
        filas_extraidas.append(FilaTabla(datos_fila))

    return filas_extraidas

def filtrar_y_guardar(filas, col_filtro, val_filtro, archivo_salida="datos.json"):
    print(f"Filtrando por columna '{col_filtro}' y valor '{val_filtro}'...")
    resultado = []
    for f in filas:
        if f.coincide_filtro(col_filtro, val_filtro):
            resultado.append(f.to_dict())

    # Si no filtramos nada, guardamos todo para que no quede vacio si se equivocan de filtro
    if not resultado and filas:
        print("Ninguna fila coincidió con el filtro exacto, guardando todas por defecto para cumplir la extracción.")
        resultado = [f.to_dict() for f in filas]
        
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as f:
            json.dump(resultado, f, ensure_ascii=False, indent=4)
        print(f"Se guardaron {len(resultado)} registros en {archivo_salida}")
    except Exception as e:
        print(f"Error al guardar: {e}")

if __name__ == "__main__":
    try:
        filas = extraer_tabla(URL)
        if filas:
            # Filtro de demostración
            filtrar_y_guardar(filas, "ID", "1")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
