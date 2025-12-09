# 59: Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que 
# intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o 
# menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe 
# mostrarse por pantalla un mensaje y el número de intentos.

import random

num=random.randint(1,1000)
num1=int(input("Introduce un número entre el 0 y el 1000: "))
intentos=0

while num1 != num:
    if num1 > num:
        print("El número que has introducido es mayor.")
        intentos=intentos+1
        num1=int(input("Introduce un número entre el 0 y el 1000: "))
    else:
        print("El número que has introducido es menor.")
        intentos=intentos+1
        num1=int(input("Introduce un número entre el 0 y el 1000: "))

print(f"Has acertado el número {num} con {intentos} intentos.")
    