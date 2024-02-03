# Leer el archivo palabras.txt y mostrar los siguientes resultados en un archivo nuevo.
# a. Cantidad total de palabras
# b. Cantidad de palabras comenzadas con consonante
# c. Cantidad de palabras palíndromas
# d. Palabra con la mayor longitud
# e. Palabra con menor longitud

palabras_totales = 0
palabras_consonantes = 0
palabras_palindromas = 0
palabra_larga = ""
palabra_corta = ""
consonantes = "bcdfghjklmnñpqrstvwxyz"

archivo = open("palabras.txt", "r")

for linea in archivo:
    palabras = linea.strip().split()

    for palabra in palabras:
        palabras_totales += 1

        if palabra[0].lower() in consonantes:
            palabras_consonantes += 1

        if palabra.lower() == palabra.lower()[::-1]:
            palabras_palindromas += 1

        if len(palabra) > len(palabra_larga):
            palabra_larga = palabra

        if not palabra_corta or len(palabra) < len(palabra_corta):
            palabra_corta = palabra

archivo2 = open("palabras2.txt", "a+")
archivo2.write(f"Palabras totales: {palabras_totales}\nPalabras comenzadas en consonante: {palabras_consonantes}\nPalabras palindromas: {palabras_palindromas}\nPalabra mas larga: {palabra_larga}\nPalabra mas corta: {palabra_corta}")

archivo.close()
archivo2.close()