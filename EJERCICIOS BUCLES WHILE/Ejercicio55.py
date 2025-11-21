# 55: A partir del programa anterior haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y 
# cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While

suma=0
rep=0

while suma == 0 or suma <= 50 and not suma // 2 == suma / 2:
    a=float(input("Introduce el primer número: "))
    b=float(input("Introduce el segundo número: "))
    print(f"La suma de los dos números es {a+b}")
    rep=rep+1
    suma=suma+a+b
    print("")
    if rep == 1:
        print(f"El total acumulado es {suma}, y llevas 1 operación realizada.")
    else:
        print(f"El total acumulado es {suma}, y llevas {rep} operaciones realizadas.")
    print("")
print("El total acumulado es mayor a 50 o es par, programa finalizado.")