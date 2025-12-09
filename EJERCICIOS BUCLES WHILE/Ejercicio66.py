# 66: Repite el ejercicio 63. En lugar de ‘tirar’ 100 veces un dado, modifica el programa para ver cómo 
# se comporta el dado en lanzamientos producidos durante aprox 3 segundos.

import time
import random

tiempo=0
num=0
uno=0
dos=0
tres=0
cuatro=0
cinco=0
seis=0

while tiempo < 3000000:
    tiempo=tiempo+1
    num=random.randint(1,6)

    if num == 1:
        uno=uno+1
    elif num == 2:
        dos=dos+1
    elif num == 3:
        tres=tres+1
    elif num == 4:
        cuatro=cuatro+1
    elif num == 5:
        cinco=cinco+1
    elif num == 6:
        seis=seis+1


print("RESUMEN")
print(f"Tiempo: {tiempo/1000000}")
print(f"El uno ha salido {uno} veces.")
print(f"El dos ha salido {dos} veces.")
print(f"El tres ha salido {tres} veces.")
print(f"El cuatro ha salido {cuatro} veces.")
print(f"El cinco ha salido {cinco} veces.")
print(f"El seis ha salido {seis} veces.")
