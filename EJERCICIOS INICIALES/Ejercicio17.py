# 17:  Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el 
# peso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado 
# es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso.

peso=float(input("Introduce tu peso (kg): "))
alt=float(input("Introduce tu altura (m): "))
print("")

imc=peso/alt**2

print(f"Si pesas {peso} kg y mides {alt} metros, tu IMC es de {round(imc)} kg por metro al cuadrado.")

if imc == 25 or imc > 25:
    print("Tienes sobrepeso.")