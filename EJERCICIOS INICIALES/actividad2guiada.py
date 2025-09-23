# Programa que realiza la suma, resta y multiplicación de dos números.

var1=int(input("Introduce un número: "))
var2=int(input("Introduce otro número: "))
print("")

total=var1+var2
print(f"La suma de los números es {total}.")
print("")

total=var1-var2
print(f"La resta de los números es {total}.")
print("")

total=var1*var2
print(f"La multiplicación de los números es {total}.")
print("")

total=var1/var2
print(f"La división de los números es {total}.")
print("")

# El doble asterisco (**) indica la potencia de dos números.

total=var1**var2
print(f"{var1} elevado a {var2} es igual a {total}.")
print("")

# La doble barra (//) divide los dos números y expresa el resultado como un número entero.

total=var1//var2
print(f"La división de los dos números, expresada en un número entero, es {total}.")
print("")

# El signo de porcentaje (%) indica el módulo de los dos números.

total=var1%var2
print(f"El módulo de los dos números es {total}.")
print("")
