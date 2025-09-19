# 7: Programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes 
# forzar que el resultado de la división tenga 2 decimales?

var1=float((input("Escribe el primer número: ")))
var2=float((input("Escribe el segundo número: ")))
print("")

total=var1+var2
print(f"La suma de {var1} y {var2} es igual a {total}")
total=var1-var2
print(f"La resta de {var1} y {var2} es igual a {total}")
total=var1*var2
print(f"La multiplicación de {var1} y {var2} es igual a {total}")
total=var1/var2
print(f"La división de {var1} y {var2} es igual a {total}")
total=var1**var2
print(f"{var1} elevado a {var2} es igual a {total}.")
total=var1//var2
print(f"La division en número entero de {var1} y {var2} es igual a {total}")
total=var1%var2
print(f"El módulo de {var1} y {var2} es igual a {total}")

# Se puede redondear usando "Round(n, m)":
# "n" es el resultado de la división, "m" es el número de decimales deseados.

total=round(var1/var2, 2)
print(f"La división redondeada de {var1} y {var2} es igual a {total}")