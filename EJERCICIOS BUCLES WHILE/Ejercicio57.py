# 57: Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa 
# controlar si el usuario introduce un número no comprendido entre 1 y 5

import random

num=random.randint(1,5)
num1=int(input("Introduce un número: "))

while num1 != num:
    if num1 < 1 or num1 > 5:
        print("Valor no válido.")
    else:
        print("Valor no acertado.")
    num1=int(input("Introduce un número: "))
print("Valor acertado.")