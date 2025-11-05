# 37: Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado 
# o suspendido.

numnotas=int(input("Introduce el número de notas que quieres introducir: "))
indice=0
print("")

# Igual que antes, hago una variable de índice para saber que nota es cual, solo para que quede más bonito.

for i in range(0,numnotas):
    indice=indice+1
    if float(input(f"Introduce la nota {indice}: ")) < 5:
        print(f"La nota {indice} es un suspenso.") 
        print("")
    else:
        print(f"La nota {indice} está aprobada.") 
        print("")


