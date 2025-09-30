# 19: Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son 
# iguales

num1=float(input("Introduce el primer número: "))
num2=float(input("Introduce el segundo número: "))

if num1 > num2:
    print(f"El primer número, {num1}, es mayor que el segundo número, {num2}.")
else:
    if num1 == num2:
        print(f"Los dos números son iguales.")
    else:
        print(f"El primer número, {num1}, es menor que el segundo número, {num2}.")