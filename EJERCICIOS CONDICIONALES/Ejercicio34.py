# 34: Corrige los 4 errores o añade el código que necesites para que el siguiente programa se 
# ejecute correctamente.

# Para diferenciar los apuntes que pongo yo y los que había antes, pondré un asterisco en los que escriba yo.

# Inicializo valores a cada variable
# * Pongo "str()" porque el "len()" solo funciona con strings.
var_numero=str(6734)
var_suma=0
# Obtengo su longitud
var_longitud=len(var_numero)
# Sumo cada digito a partir del índice de cada posición
# * Borro el espacio entre "var_numero" y "[1,2,3...]."
# * Además, hay que comenzar con el índice "0".
var_suma = var_numero[0] + var_numero[1]+ var_numero[2] + var_numero[3]
# Utilizo una condición y el operador aritmético // para saber si el resto da 0 y ver si es par
# * Pongo el "int()" antes de var_suma porque si no lo detecta como un string y no puede usar el //.
# * Hay que poner un "else" porque si el valor es par el código no hará absolutamente nada.
if int(var_suma) // 2 == 0:
    print (f"el valor de {var_suma} es impar")
else:
    print (f"el valor de {var_suma} es par")