
matriz = [[int() for ind0 in range(100)] for ind1 in range(100)]
mayor_fila=[0]*100
menor_columna = [0]*100


filas = int(input('Ingrese el número de filas: '))
columnas = int(input('Ingrese el número de columnas: '))

#Se ingresan los datos de la matriz y se elige el mayor elemento 
for i in range (filas):
    for j in range (columnas):
        matriz[i][j]=int(input())


mayor_elemento = matriz[0][0]
for i in range (filas):
        for j in range(columnas):
              if matriz[i][j] > mayor_elemento:
                mayor_elemento = matriz[i][j]
        

#el vector de menor_columna lo lleno con el elemento mayor de la matriz para así poder compararlo después
for j in range (columnas):
      menor_columna[j]=mayor_elemento

#comparo cada elemento con su fila y obtengo el mayor de cada fila 
for i in range (filas):
      for j in range (columnas):
            if matriz[i][j] > mayor_fila[i]:
                  mayor_fila[i] = matriz[i][j]

#comparo cada elemento con su columna y obtengo el menor de cada columna 
for i in range (filas):
      for j in range (columnas):
            if matriz [i][j] < menor_columna[j]:
                  menor_columna[j] = matriz[i][j]

#comparo los vectores entre si para asi ver si coinciden y guardar las coordenadas 

for i in range (filas):
      for j in range (columnas):
            if mayor_fila[i] == menor_columna[j]:
                  fila_silla = i 
                  columna_silla = j




for i in range(filas):
    for j in range(columnas):
        print(matriz[i][j], end="")
    print("")
        
for i in range (filas):
     print(mayor_fila[i], end="")
print(" ")
for j in range (columnas):
     print(menor_columna[j],end="")
print("")
print(fila_silla, columna_silla)

