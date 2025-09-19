# 12:  Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor 
# y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.

lado=float(input("Introduce el lado del trapecio: "))
bmenor=float(input("Introduce la base menor del trapecio: "))
bmayor=float(input("Introduce la base mayor del trapecio: "))
altura=float(input("Introduce la altura del trapecio: "))
print("")

if bmenor > bmayor:
    print("Error, la base menor no puede ser mayor que la base mayor.")
else:
    print(f"El perímetro del trapecio es {bmayor+bmenor+lado*2}.")
    print(f"El área del trapecio es {(bmayor+bmenor)/2*altura}.")