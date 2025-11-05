# 36:  Programa que sume los n primeros números naturales. n Lo introduce el usuario.

print("Se sumarán los primeros n números naturales.")
n=int(input("Introduce el valor de n: "))
indice=0
suma=0
print("")

# Uso una variable de índice para saber que numero se le tiene que sumar a la variable suma.

for i in range(0,n):
    indice=indice+1
    suma=suma+indice

print(f"La suma de los primeros {n} números naturales es igual a {suma}")
    
