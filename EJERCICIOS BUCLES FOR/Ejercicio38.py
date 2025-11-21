# 38:  A partir del programa anterior, establece los rangos para que el usuario no pueda introducir 
# notas inferiores a 0 y superiores a 10.

numnotas=int(input("Introduce el número de notas que quieres introducir: "))
indice=0
print("")

for i in range(0,numnotas):
    indice=indice+1
    nota=float(input(f"Introduce la nota {indice}: "))
    if nota <= 10 and nota >= 0:
        if nota < 5:
            print(f"La nota {indice} es un suspenso.") 
            print("")
        else:
            print(f"La nota {indice} está aprobada.") 
            print("")
    else:
        print(f"La nota {indice} no es válida.") 
        print("")