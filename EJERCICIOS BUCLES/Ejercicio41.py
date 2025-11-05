# 41: Imprime el patrón utilizando "for".

indice=1
num=0

for i in range(0,5):
    num=str(num)+str(indice)
    indice=indice+1
    print(str(num))