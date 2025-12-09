# 62:  Realiza un programa que pida dos números por teclado y presente por pantalla qué números 
# hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo.

num1=int(input("Introduce el primer valor: "))
num2=int(input("Introduce el segundo valor: "))
par=""
impar=""
numsalida=""

if num1 < num2:
    indice=num1
    for i in range(num1,num2+1):
        # Si es el primer número, no escribe un guión antes.
        if indice == num1:
            numsalida=str(numsalida)+str(indice)
            indice=indice+1
        else:
            numsalida=str(numsalida)+"-"+str(indice)
            indice=indice+1
else:
    indice=num1
    for i in range(num2,num1+1):
        if indice == num1:
            numsalida=str(numsalida)+str(indice)
            indice=indice-1
        else:
            numsalida=str(numsalida)+"-"+str(indice)
            indice=indice-1
print(f"{numsalida}")

print(f"Los números pares son: {par}")
print(f"Los números impares son: {impar}")
