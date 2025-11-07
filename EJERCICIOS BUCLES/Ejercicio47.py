# 47: Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe 
# mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b 
# la secuencia en descenso. Respeta el formato de salida.

num1=int(input("Introduce el primer número: "))
num2=int(input("Introduce el segundo número: "))
numsalida=""

if num1 < num2:
    indice=num1
    for i in range(num1,num2+1):
        numsalida=str(numsalida)+"-"+str(indice)
        indice=indice+1
print(f"{numsalida}")
