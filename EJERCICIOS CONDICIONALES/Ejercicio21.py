# 21: Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz 
# cuadrada no de un valor negativo

import math

num1=float(input("Introduce el valor del primer número: "))
num2=float(input("Introduce el valor del segundo número: "))
num3=float(input("Introduce el valor del tercer número: "))
num=float(num2**2-4*num1*num3)
print("")

if num > 0:
    resultadopos=(num2*-1+math.sqrt(num))/2*num1
    resultadoneg=(num2*-1-math.sqrt(num))/2*num1

    print(f"El valor de x1 es {round(resultadopos, 2)}.")
    print(f"El valor de x2 es {round(resultadoneg, 2)}.")
else:
    print("Error, el valor de la raíz cuadrada es negativo.")