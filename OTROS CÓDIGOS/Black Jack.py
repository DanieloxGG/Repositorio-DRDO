# Código de juego de Black Jack

import random
juego=0
dinero=10
numjug=0

print("¡Bienvenido a Black Jack!")
print("")
input("Escribe cualquier cosa para comenzar: ")
print("")

juego=1

while juego==1:
    elegir=1
    while elegir==1:
        numjug=numjug+random.randint(1, 11)
        print(f"La suma de tus cartas es {numjug}")
        print("")
        if numjug > 21:
            print(f"Tienes un {numjug}, te has pasado de 21. Has perdido.")
            print("")
            elegir=0
            juego=0
        elif input("¿Quieres robar? S/N: ") == "N":
            print("")
            print(f"Te has plantado con un {numjug}")
            print("")
            elegir=0
            juego=0




    

    
