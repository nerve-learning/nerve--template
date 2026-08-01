import time
from nerve import NexusClient

# Conectarse a Nerve bajo el nombre "robot_mascota"
robot = NexusClient()
robot.connect("robot_mascota")

# Bucle for que envíe 10,000 mensajes sin parar al destino "caja_de_arena"
for i in range(10000):
    paquete = {"ping": 1}
    robot.send("caja_de_arena", paquete)

# Una vez termine el bucle de 10,000, dormir por 15 segundos
time.sleep(15)
