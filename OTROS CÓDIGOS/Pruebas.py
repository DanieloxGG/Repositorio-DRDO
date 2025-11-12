# Prueba listas.

lista=[]
n=int(input("¿Cuantos valores quieres introducir en la lista?: "))

for i in range(1,n+1):
    valor=input(f"Introduce el valor {i}: ")
    lista.append(valor)
print("")
for i in range(0,len(lista)):
    print(f"El valor {i+1} de la lista es '{lista[i]}'.")
print("")

if input("¿Quieres añadir algún valor? (S/N): ") == "S":
    pos=int(input("¿En qué posición?: "))
    valor=input("Escribe el valor: ")
    lista.insert(pos, valor)
    print("")
else:
    print("Programa finalizado.")