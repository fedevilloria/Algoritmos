#EJERCICIO F

n = int(input())

for _ in range(n):
    frase = input()
    i = 0
    palabra_actual = ""
    palabra_minuscula = ""
    salida = ""
    while i < len(frase):
        if frase[i] != ' ' and frase[i] != '.':
            palabra_actual += frase[i]
            caracter = frase[i].lower()
            palabra_minuscula += caracter
        else:
            if len(palabra_actual) == 10:
                cadena = ""
                for j in range(1, 9):
                    cadena += palabra_minuscula[j]
                if cadena == "oulupukk":
                    salida += "Joulupukki"
                else:
                    salida += palabra_actual
            else:
                salida += palabra_actual

            palabra_actual = ""
            palabra_minuscula = ""

            if frase[i] == ' ':
                salida += ' '
            if frase[i] == '.':
                salida += '.'
        i += 1

    if palabra_actual:
        if len(palabra_actual) == 10:
            cadena = ""
            for j in range(1, 9):
                cadena += palabra_minuscula[j]
            if cadena == "oulupukk":
                salida += "Joulupukki"
            else:
                salida += palabra_actual
        else:
            salida += palabra_actual

    print(salida)