# nombre_de_la_tabla = [["Juan", "Laura"],[21, 32]]
#   nombre_de_la_tabla FILA:[1] COLUMNA:[0]
# print(nombre_de_la_tabla[1][1])

mi_tabla = [['Juan', 'Laura'], [21, 32]]

# Recorriendo los elementos

# Accedemos a cada fila (que es una lista)
for fila in mi_tabla:
    # Accedemos a cada columna dentro de la fila
    for columna in fila:
        print(columna)

# Recorriendo los índices
# i serían las filas
for i in range(len(mi_tabla)):
    for j in range(len(mi_tabla[i])):
        print(mi_tabla[i][j])

# Con while y los índices
fila = 0

while fila < len(mi_tabla):
    columna = 0
    while columna < len(mi_tabla[fila]):
        print(mi_tabla[fila][columna])
        columna += 1
    fila += 1


# Creamos la tabla con listas vacías al comienzo
usuarios = [[], []]

# Definimos un tamaño para las listas de la tabla
# Lo puedes cambiar si quieres
tamaño = 3

# Leemos los datos y los agregamos a la tabla
for i in range(tamaño):
    print("Ingrese los datos de la persona", i + 1)
    nombre = input("Nombre: ")
    identificación = input("Identificación: ")

    # La primera lista es para los nombres
    usuarios[0].append(nombre)

    # La segunda lista es para las identificaciones
    usuarios[1].append(identificación)

# Ahora mostremos los valores en la tabla
for i in range(tamaño):
    print("Mostrando los datos de la persona", i + 1)

    print("Nombre:", usuarios[0][i])
    print("Identificación:", usuarios[1][i])