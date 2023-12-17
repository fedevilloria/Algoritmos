while True:
    F, C = map(int, input().split())
    if F == 0 and C == 0:
        break

    matriz = []
    for _ in range(F):
        fila = list(map(int, input().split()))
        matriz.append(fila)

    puntos_silla = []
    for i in range(F):
        minimo_fila = min(matriz[i])
        columna_minimo = matriz[i].index(minimo_fila)
        if minimo_fila == max([matriz[j][columna_minimo] for j in range(F)]):
            puntos_silla.append((i, columna_minimo))

    if puntos_silla:
        print("SI")
    else:
        print("NO")