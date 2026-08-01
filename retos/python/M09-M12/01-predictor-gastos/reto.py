import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def cargar_datos(archivo):
    meses = []
    gastos = []
    try:
        with open(archivo, mode='r', encoding='utf-8') as f:
            lector = csv.reader(f)
            next(lector) # Saltar el encabezado
            for fila in lector:
                if len(fila) == 2:
                    meses.append(float(fila[0]))
                    gastos.append(float(fila[1]))
    except Exception as e:
        print(f"Error al cargar datos: {e}")
    return np.array(meses).reshape(-1, 1), np.array(gastos)

def entrenar_modelo(X, y):
    modelo = LinearRegression()
    modelo.fit(X, y)
    return modelo

def predecir_siguiente_mes(modelo, ultimo_mes):
    siguiente_mes = np.array([[ultimo_mes + 1]])
    prediccion = modelo.predict(siguiente_mes)
    return siguiente_mes[0][0], prediccion[0]

def graficar_tendencia(X, y, modelo, mes_pred, gasto_pred):
    plt.figure(figsize=(8, 5))
    plt.scatter(X, y, color='blue', label='Gastos históricos')
    
    # Línea de tendencia
    x_tendencia = np.linspace(1, mes_pred, 100).reshape(-1, 1)
    y_tendencia = modelo.predict(x_tendencia)
    plt.plot(x_tendencia, y_tendencia, color='red', linestyle='--', label='Tendencia (Regresión Lineal)')
    
    # Punto de predicción
    plt.scatter([mes_pred], [gasto_pred], color='green', s=100, zorder=5, label=f'Predicción Mes {int(mes_pred)}')
    
    plt.title('Proyección de Gastos Mensuales')
    plt.xlabel('Mes')
    plt.ylabel('Gasto ($)')
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("Iniciando Predictor de Gastos...")
    archivo_csv = "gastos.csv"
    X, y = cargar_datos(archivo_csv)
    
    if len(X) == 0:
        print("No se encontraron datos en el CSV.")
    else:
        print(f"Se cargaron {len(X)} meses de datos históricos.")
        modelo = entrenar_modelo(X, y)
        
        ultimo_mes = X[-1][0]
        mes_pred, gasto_pred = predecir_siguiente_mes(modelo, ultimo_mes)
        
        print("\n=== RESULTADOS DE PREDICCIÓN ===")
        print(f"Último mes registrado: {int(ultimo_mes)}")
        print(f"Predicción para el mes {int(mes_pred)}: ${gasto_pred:.2f}")
        print("================================\n")
        
        print("Generando gráfica de tendencia...")
        graficar_tendencia(X, y, modelo, mes_pred, gasto_pred)
