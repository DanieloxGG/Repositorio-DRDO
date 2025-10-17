# 25: Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.

print("")
nota=float(input("Introduce la nota que has sacado: "))
print("")

if nota > 10 or nota < 0:
    print("El número introducido no está entre 0 y 10.")
elif nota >= 5:
    if nota >= 6.5:
        if nota >= 8.5:
            print(f"Has sacado un {round(nota, 2)}, has aprovado con un excelente.")
        else:
            print(f"Has sacado un {round(nota, 2)}, has aprovado con un notable.")
    else:
        print(f"Has sacado un {round(nota, 2)}, has aprovado con un suficience.")
else:
    print(f"Has sacado un {round(nota,2 )}, has suspendido, insuficiente.")

print("")