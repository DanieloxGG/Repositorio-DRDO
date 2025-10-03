# 33: Programa un código que permita contar el número de vocales de la siguiente frase: No 
# hay mal que dure cien años.

frase="No hay mal que dure cien años."
vocales= "aeiouAEIOU"
num=0

for vocales in frase:
    num=num+1

print(f"La frase tiene {num} vocales.")