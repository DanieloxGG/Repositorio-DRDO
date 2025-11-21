# 42b: Version alternativa que he hecho yo donde se introduce el número máximo de asteriscos.

n=int(input("Introduce el número máximo de asteriscos: "))
print("")

for i in range(0,n):
    print("*"*i)
for x in range(n,0,-1):
    print("*"*x)