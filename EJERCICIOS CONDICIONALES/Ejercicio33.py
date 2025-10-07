# 33: Programa un código que permita contar el número de vocales de la siguiente frase: No 
# hay mal que dure cien años.

frase1="No hay mal que dure cien años."

# ".casefold" sirve para transformar todo el texto en minúsculas.

frase=frase1.casefold()

# ".count" sirve para contar cuantas veces aparece algo en un string.

numa=frase.count("a")
nume=frase.count("e")
numi=frase.count("i")
numo=frase.count("o")
numu=frase.count("u")

print("La frase es: No hay mal que dure cien años.")
print("")

print(f"En la frase aparece la letra a {numa} veces.")
print(f"En la frase aparece la letra e {nume} veces.")
print(f"En la frase aparece la letra i {numi} veces.")
print(f"En la frase aparece la letra o {numo} veces.")
print(f"En la frase aparece la letra u {numu} veces.")