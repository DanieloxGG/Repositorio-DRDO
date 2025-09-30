# 23: Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un 
# notable (>=6.5 -<8.5), satisfactorio (<6.5 a 5) o insuficiente (<5). Controla que la nota 
# introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.

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
