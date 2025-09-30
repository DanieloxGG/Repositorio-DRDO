# 24: Corrige los errores del siguiente código y comprueba que se ejecuta correctamente.1var=float(input("Introduce el peso: "))

# En vez de nombrar a las variables como "1var" y "2var" es mejor nombrarlas "var1" y var2".
var1=float(input("Introduce el peso: "))
# Aquí falta el "float()".
var2=float((input("Introduce la altura: ")))
# Aquí tendríamos que poner solo un "="
var_imc=var1/var2**2
# Este "print" necesita una "f" al principio, y la variable 1 está en mayúsculas.
print(f"Si pesas {var1} kilos y mides {var2}, tu IMC es: {var_imc}.")
# Faltan los ":" al final del condicional.
if var_imc>25:
 print("Hay sobrepeso")
else:
 print("Estás dentro de los parámetros normales")
