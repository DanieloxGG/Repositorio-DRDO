# 58: Modifica el programa anterior para que tengas 3 intentos. Utiliza while

import random

num=random.randint(1,5)
num1=int(input("Introduce un número: "))
intentos=3

while num1 != num and intentos > 0:
    if num1 < 1 or num1 > 5:
        print("Valor no válido.")
    else:
        print("Valor no acertado.")
        intentos=intentos-1
    if intentos > 0:
        num1=int(input("Introduce un número: "))

if intentos > 0:
    print("Valor acertado.")
else:
    print("Has perdido, te has quedado sin intentos.")
    