# 20: A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados 
# números entre 0 y 10.

num1=float(input("Introduce el primer número: "))
num2=float(input("Introduce el segundo número: "))

if num1 < 1 or num1 > 10 or num2 < 1 or num2 > 10:
    print("Uno de los números o ambos números están fuera de los límites del programa.")
else: 
    if num1 > num2:
        print(f"El primer número, {num1}, es mayor que el segundo número, {num2}.")
    else:
        if num1 == num2:
            print(f"Los dos números son iguales.")
        else:
            print(f"El primer número, {num1}, es menor que el segundo número, {num2}.")