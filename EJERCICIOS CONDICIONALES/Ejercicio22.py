# 22:  Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. 
# Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.

print("")
nota=float(input("Introduce la nota que has sacado: "))
print("")

if nota >= 5:
    if nota <= 10:
        print(f"Has sacado un {round(nota, 2)} y has aprobado.")
    else:
        print(f"El número introducido no está entre 0 y 10.")

if nota < 5:
    if nota >= 0:
        print(f"Has sacado un {round(nota, 2)} y has suspendido.")
    else:
        print(f"El número introducido no está entre 0 y 10.")

print("")
    