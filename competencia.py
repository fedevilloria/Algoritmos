def invertir_palabra(palabra):
    palabra = list(palabra)
    for i in range(len(palabra) // 2):
        temp = palabra[i]
        palabra[i] = palabra[len(palabra) - i - 1]
        palabra[len(palabra) - i - 1] = temp
    return ''.join(palabra)


n = int(input())
input()  # Ignorar la línea en blanco

for i in range(n):
    linea = input()

    linea = [chr(ord(caracter) + 3) if (ord(caracter) >= 65 and ord(caracter) <= 90) or (
                ord(caracter) >= 97 and ord(caracter) <= 122) else caracter for caracter in linea]

    linea = ''.join(linea)

    linea = invertir_palabra(linea)

    mitad = len(linea) // 2
    linea = [chr(ord(caracter) - 1) if caracter.isalpha() and indice >= mitad else caracter for indice, caracter in
             enumerate(linea)]

    linea = ''.join(linea)  # Convertir de nuevo a una cadena

    print(linea)