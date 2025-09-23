# 16: Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El 
# resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un 
# resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso
# (raíz y división).

import math

num=float(input("Introduce un número: "))

print(f"La raíz cuadrada de {num} es igual a {round(math.sqrt(num), 2)}.")
print(f"La raíz cuadrada de {num} dividida entre 2 es igual a {math.sqrt(num)//2}")