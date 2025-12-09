# 63:  Realiza un programa que permita tirar 100 veces un dado y nos presente por pantalla el número
# de veces que se repite cada número.

import random
indice=1
num=0
uno=0
dos=0
tres=0
cuatro=0
cinco=0
seis=0

while indice <= 100:
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
    indice=indice+1

print(f"El uno ha salido {uno} veces.")
print(f"El dos ha salido {dos} veces.")
print(f"El tres ha salido {tres} veces.")
print(f"El cuatro ha salido {cuatro} veces.")
print(f"El cinco ha salido {cinco} veces.")
print(f"El seis ha salido {seis} veces.")