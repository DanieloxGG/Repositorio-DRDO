# Código de juego de Black Jack

import random
from time import sleep

juego=0
dinero=10
numjug=0
elegcrup=0
numcrupier=0

print("--------------------------------")
print("¡Bienvenido a Black Jack!")
print("")
input("Escribe cualquier cosa para comenzar: ")
print("")

juego=1

while juego==1:
    numjug=0
    numcrupier=0
    elegir=1
    print(f"Tienes {dinero} monedas antes de apostar.")
    sleep(1)
    apostar=1
    while apostar == 1:
        apuesta=float(input("¿Cuantas monedas quieres apostar?: "))
        if round(apuesta) == apuesta:
            if apuesta == dinero or apuesta < dinero:
                print("")
                apostar=0
                sleep(1)
            else:
                print("No puedes apostar dinero que no tienes.")
                print("")
        else:
            print(f"{apuesta} no es una apuesta válida.")
            print("")
    print(f"Tanto tú como el crupier apostais {round(apuesta)} monedas.")
    dinero=dinero-round(apuesta)
    sleep(1)
    print(f"Te quedan {dinero} monedas.")
    while elegir==1:
        numjug=numjug+random.randint(1, 11)
        print(f"La suma de tus cartas es {numjug}")
        print("")
        if numjug > 21:
            print(f"Tienes un {numjug}, te has pasado de 21. Has perdido. (-{apuesta} monedas)")
            elegir=0
            juego=0
        elif input("¿Quieres robar? S/N: ").upper() == "N":
            print("")
            print(f"Te has plantado con un {numjug}")
            print("")
            elegir=0
            juego=0
    
    if numjug < 22:
        print("Turno del crupier...")
        print("")
        elegcrup=1
 
    while elegcrup == 1:
        sleep(1.5)
        numcrupier=numcrupier+random.randint(1,11)
        if numcrupier > 17 and numcrupier < 22 or numcrupier > numjug:
            print(f"El crupier ha robado y se ha plantado con un {numcrupier}")
            print("")
            elegcrup=0
            if numcrupier < numjug:
                print(f"Has sacado un {numjug} y el crupier un {numcrupier}")
                print(f"Has ganado. (+{apuesta*2} monedas)")
                print("")
                dinero=dinero+4
            elif numcrupier == numjug:
                print(f"Has sacado un {numjug} y el crupier un {numcrupier}")
                print("Habeis empatado. Se te devuelven las monedas.)")
                print("")
                dinero=dinero+2
            else:
                print(f"Has sacado un {numjug} y el crupier un {numcrupier}")
                print(f"Has perdido. (-{apuesta} monedas)")
                print("")
        elif numcrupier > 21:
            print(f"El crupier tiene un {numcrupier}, se ha pasado de 21. Has ganado. (+{apuesta*2} monedas)")
            elegcrup=0
            dinero=dinero+apuesta*2
        else:
            print(f"El crupier ha robado y tiene un {numcrupier}")
            print("")

    if dinero > 0:
        print("")
        opcion=input("¿Quieres jugar otra ronda? S/N: ")
        print("")
        if opcion.upper() == "S":
            print("Iniciando siguiente partida...")
            print("")
            sleep(2)
            juego=1
        elif opcion.upper() == "N":
            print(f"Te has retirado con {dinero} monedas. Fin del juego.")
            print("")
            juego=0
        else:
            print(f"La opción {opcion} no es válida. Fin del juego.")
            print("")
            juego=0
    else:
        print("Te has quedado sin dinero. Fin de la partida.")
        print("")
        juego=0




    

    
