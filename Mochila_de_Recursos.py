# Calcular la longitud de una cadena sin utilizar la funcion len()
def longitud_cadena(cadena):
    contador = 0

    for i in cadena:
        contador = contador + 1

    return contador

# Determinar la cantidad de vocales, espacios en blanco y consonantes de un texto
def consonantes(cadena):
    contador = 0
    consonantes_validas = "BCDFGHJKLMNÑPQRSTVWXYZ"  # Lista de consonantes validas

    for i in cadena:
        if i.upper() in consonantes_validas:
            contador = contador + 1

    return contador

# Cortar palabras de un texto e ingresarla en un vector
def cortar_palabras(texto):
    palabras = []  # Vector vacio para almacenar las palabras
    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    palabra = ""

    for caracter in texto:
        if caracter.lower() in abecedario:
            palabra = palabra + caracter
        elif palabra:  # Agregar palabra al vector si no esta vacia
            palabras = palabras + [palabra]
            palabra = ""

    if palabra:  # Asegurarse de agregar la última palabra si existe
        palabras = palabras + [palabra]

    return palabras

# Determinar la palabra mas grande
def palabra_mas_grande(palabras):
    palabra_mas_larga = ""

    for palabra in palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra

    return palabra_mas_larga

# Buscar un caracter dentro de una cadena
def busqueda_caracter(cadena):
    caracter_deseado = input("Ingrese el caracter que desea buscar: ")

    for caracter in cadena:
        if caracter == caracter_deseado:
            print("Lo tiene.")

    return
