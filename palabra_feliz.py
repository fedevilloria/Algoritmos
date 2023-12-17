# El usuario va a ingresar un texto por teclado y debemos determinar cual es la palabra “feliz”.
# Una palabra feliz se la considera aquella que tiene dos vocales iguales seguidas en dicha palabra. Por
# ejemplo: cooperativa, booleano.


# UNA PALABRA
#palabra = input().lower()
#vocales = "aeiou"
#bandera = 0
#for i in range(len(palabra)-1):
#    if palabra[i] == palabra[i+1]:
#        bandera = 1

#if bandera == 1:
#    print("Feliz")
#else:
#    print("Triste")


# UN TEXTO
texto = input().lower()
vocales = "aeiou"

palabras = texto.split()
palabras_felices = []

for palabra in palabras:
    for i in range(len(palabra) - 1):
        if palabra[i] == palabra[i+1] and palabra[i] in vocales:
            palabras_felices.append(palabra)

print(palabras_felices)