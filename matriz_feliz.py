filas = int(input("Filas: "))
columnas = int(input("Columnas: "))
matriz = []
vocales = "aeiou"
palabras_felices = 0

for i in range(filas):
    fila = []
    for j in range(columnas):
        palabra = input(f"Ingrese palabra para la posición ({i + 1}, {j + 1}): ")
        fila.append(palabra)
        for letra in range(len(palabra) - 1):
            if palabra[letra] == palabra[letra + 1] and palabra[letra] in vocales:
                palabras_felices = palabras_felices + 1
    matriz.append(fila)

print("\nMatriz resultante:")
for fila in matriz:
    print(fila)

print(f"Cantidad de palabras felices: {palabras_felices}")