# 54: Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total 
# de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta 
# preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la 
# operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el 
# mensaje del acumulado es singular o plural. Con While

suma=0
rep=0

while suma <= 50:
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
print("El total acumulado es mayor a 50, programa finalizado.")