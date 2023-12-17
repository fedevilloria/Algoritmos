from random import *
matriz = [[1,2],[3,4],[5,6]]

for fila in range(3):
    for columna in range(2):
        print(matriz[fila][columna], end=" ")
    print()

#Otro ejemplo
matriz = []
m = 3
n = 2
for fila in range(m):
    matriz.append([])
    for columna in range(n):
        matriz[fila].append(None)

fila = 3
columna = 3
a = [[randint(1,100) for i in range(fila)] for j in range(columna)]
for f in a:
    print(f)

columna_obtenida = int(input("Columna a obtener: "))
b = []
for f in range(len(a)):
    b.append(a[f][columna_obtenida])
print(b)