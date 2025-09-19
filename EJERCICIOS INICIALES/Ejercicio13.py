# 13: Realiza un programa que, a partir introducir el lado de un cubo, presente por pantalla el 
# área y para calcular el volumen utiliza el operador de exponente.

lado=float(input("Introduce el lado del cubo: "))
print("")

print(f"El área del cubo es {6*lado**2}.")
print(f"El volumen del cubo es {lado**3}.")