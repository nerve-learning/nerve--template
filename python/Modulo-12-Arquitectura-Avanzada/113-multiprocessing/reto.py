import nerve
import multiprocessing
import time

def cargar_y_disparar():
    print("Cargando cañon laser...")
    time.sleep(4)
    print("💥 ¡BOOM! Nave destruida.")

if __name__ == '__main__':
    clon1 = multiprocessing.Process(target=cargar_y_disparar)
    clon2 = multiprocessing.Process(target=cargar_y_disparar)
    
    clon1.start()
    clon2.start()
    
    clon1.join()
    clon2.join()
    
    print("🏆 Base salvada, buen trabajo comandante.")
