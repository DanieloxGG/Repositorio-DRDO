# 53: A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las 
# sumas y el número de repeticiones. Con While

rep=0
suma=0

while input("¿Quieres seguir el programa? (S/N): ") == "S":
    rep=rep+1
    print("")
    a=float(input("Introduce el primer número: "))
    b=float(input("Introduce el segundo número: "))
    print(f"El resultado de la suma es {a+b}")
    suma=suma+a+b
    print("")
print("Programa finalizado.")
print(f"Has repetido el programa {rep} veces, y la suma total es de {suma}")