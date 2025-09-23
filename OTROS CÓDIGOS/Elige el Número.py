
# Juego de adivinar un número del 1 al 10 o algun otro número que el jugador elija.

import random

print("")

juego=1
nummax=0
win=0
print("¡Bienvenido a adivina el número!")
print("")
print("Elige con A, B, C, D o E cual quieres que sea el número máximo.")
print("")
print("  a) 10       (FÁCIL)")
print("  b) 100      (NORMAL)")
print("  c) 1.000    (DIFÍCIL)")
print("  d) 10.000   (EXTREMO)")
print("  e) 100.000  (IMPOSIBLE)")
print("")

# Elección del número máximo:

while nummax == 0:
    opc=input("Elige el número máximo: ")
    print("")
    if opc == "A":
        nummax=10
        inten=int(3)
        print("Tienes 3 intentos para adivinar un número del 1 al 10.")
        print("")
    
    else:
        
        if opc == "B":
            nummax=100
            inten=int(5)
            print("Tienes 5 intentos para adivinar un número del 1 al 100.")
            print("")
        else:
            if opc == "C":
                nummax=1000
                inten=int(10)
                print("Tienes 10 intentos para adivinar un número del 1 al 1.000.")
                print("")
            else:
                if opc == "D":
                    nummax= 10000
                    inten=int(15)
                    print("Tienes 15 intentos para adivinar un número del 1 al 10.000.")
                    print("")
                else:
                    if opc == "E":
                        nummax= 100000
                        inten=int(20)
                        print("Tienes 20 intentos para adivinar un número del 1 al 100.000, buena suerte...")
                        print("")
                    else:
                        print("Opción no válida.")
                        print("")

# Hacer que el número sea entre el 1 y el número máximo escogido:

numero=random.randint(1, nummax)

# El loop del juego:

while inten > 0:
    numelegido=int(input("Elige un número: "))
    print("")
    if numelegido == numero:
        print("")
        win=1
        break
    if numelegido > nummax or numelegido < 1:
        print(f"El número {numelegido} no es válido...")
        print("")
    else:
        if numelegido < numero:
            print("El número que he escogido es mayor al que has dicho.")
            inten=inten-1
            print(f"{inten} intento(s) restante(s).")
            print("")
        if numelegido > numero:
            print("El número que he escogido es menor al que has dicho.")
            inten=inten-1
            print(f"{inten} intento(s) restante(s).")
            print("")

# El mensaje que se muestra al final del juego:

print("FIN DEL JUEGO.")
print("")

# Se comprueba si el jugador ha ganado o no:

if win == 1:
    print(f"¡Has ganado con {inten} intento(s) restante(s)!")
    print("")
else:
    print("¡Has perdido!")
    print("")

# Se muestra cuál era el número.
    
print(f"El número era el {numero}.")



    



