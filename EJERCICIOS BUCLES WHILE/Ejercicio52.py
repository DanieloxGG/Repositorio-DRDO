# 52: Realiza un programa que sume dos números enteros por teclado y presente el resultado por 
# pantalla. El programa preguntará si deseas o no repetir la operación. Con While

while input("¿Quieres seguir el programa? (S/N): ") == "S":
    print("")
    a=float(input("Introduce el primer número: "))
    b=float(input("Introduce el segundo número: "))
    print(f"El resultado de la suma es {a+b}")
    print("")