# 24: Corrige los errores del siguiente código y comprueba que se ejecuta correctamente.1var=float(input("Introduce el peso: "))

# En vez de nombrar a las variables como "1var" y "2var" es mejor nombrarlas "var1" y var2".
# Tambien vendría bien concretarle al usuario que unidades se usan para evitar confusión.
var1=float(input("Introduce el peso (Kg): "))
# Aquí falta el "float()".
var2=float((input("Introduce la altura (m): ")))
# Aquí tendríamos que poner solo un "="
var_imc=var1/var2**2
# Este "print" necesita una "f" al principio, y la variable 1 está en mayúsculas.
# También sería conveniente poner un "round()" para que el resultado quede más bonito.
print(f"Si pesas {var1} kilos y mides {var2}, tu IMC es: {round(var_imc, 2)}.")
# Faltan los ":" al final del condicional.
if var_imc>25:
 print("Hay sobrepeso")
else:
 print("Estás dentro de los parámetros normales")
