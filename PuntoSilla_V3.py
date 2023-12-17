matriz = [[int() for ind0 in range(300)] for ind1 in range(300)]
mayor_fila=[0]*300
menor_fila=[99999]*300
mayor_columna=[0]*300
menor_columna = [99999]*300
punto_silla=[0]*300
filas=1
columnas=1
contador_matrices = 0

while filas != 0 and columnas != 0:
    #establezco la dimensión de las matrices y corroboro que no sean 0 
    filas = int(input())
    columnas = int(input())

    if filas == 0 and columnas == 0:
         break
    else:
        #cargo los datos de la matriz
        for i in range (filas):
            for j in range (columnas):
                matriz[i][j] = int(input())
        
        #comparo cada elemento con su fila y obtengo el MAYOR de cada fila 
        for i in range (filas):
            for j in range (columnas):
                    if matriz[i][j] >= mayor_fila[i]:
                        mayor_fila[i] = matriz[i][j]
 
        #comparo cada elemento con su columna y obtengo el MENOR de cada columna 
        for i in range (filas):
            for j in range (columnas):
                    if matriz [i][j] <= menor_columna[j]:
                        menor_columna[j] = matriz[i][j]
     
        #comparo cada elemento con su fila y obtengo el MENOR de cada fila 
        for i in range (filas):
            for j in range (columnas):
                    if matriz[i][j] <= menor_fila[i]:
                        menor_fila[i] = matriz[i][j]
        
        #comparo cada elemento con su columna y obtengo el MAYOR de cada columna 
        for i in range (filas):
            for j in range (columnas):
                    if matriz [i][j] >= mayor_columna[j]:
                        mayor_columna[j] = matriz[i][j]
        
        #comparo los vectores entre si para asi ver si coinciden y guardar la respuesta
        for i in range (filas):
            for j in range (columnas):
                if mayor_fila[i] == menor_columna[j]:
                    punto_silla[contador_matrices] = 1
                else:
                    punto_silla[contador_matrices] = 0
        for i in range (filas):
            for j in range (columnas):
                if menor_fila[i] == mayor_columna[j]:
                    punto_silla[contador_matrices] = 1
                else:
                    punto_silla[contador_matrices] = 0
       
        #vuelvo cada vector a sus iniciaciones iniciales. 
        mayor_fila=[0]*300
        menor_fila=[99999]*300
        mayor_columna=[0]*300
        menor_columna = [99999]*300
        contador_matrices = contador_matrices + 1



for i in range(contador_matrices):
    if punto_silla[i] == 1:
        print('SI')
    else:
        print ('NO')
