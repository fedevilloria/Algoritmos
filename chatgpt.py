def tiene_puntos_silla(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    for i in range(filas):
        minimo_fila = min(matriz[i])
        columna_minimo = matriz[i].index(minimo_fila)
        if minimo_fila == max([matriz[j][columna_minimo] for j in range(filas)]):
            return True

    return False


# Matriz 1
F1, C1 = map(int, input().split())
matriz1 = []
for _ in range(F1):
    fila = list(map(int, input().split()))
    matriz1.append(fila)

# Matriz 2
F2, C2 = map(int, input().split())
matriz2 = []
for _ in range(F2):
    fila = list(map(int, input().split()))
    matriz2.append(fila)

# Matriz 3
F3, C3 = map(int, input().split())
matriz3 = []
for _ in range(F3):
    fila = list(map(int, input().split()))
    matriz3.append(fila)

# Verificar si las matrices tienen puntos de silla
tiene_puntos1 = tiene_puntos_silla(matriz1)
tiene_puntos2 = tiene_puntos_silla(matriz2)
tiene_puntos3 = tiene_puntos_silla(matriz3)

# Imprimir "Si" o "No" según corresponda
if tiene_puntos1:
    print("Si")
else:
    print("No")

if tiene_puntos2:
    print("Si")
else:
    print("No")

if tiene_puntos3:
    print("Si")
else:
    print("No")
