def contar_palabras(texto):
    contador = 0
    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    palabra = ""

    for caracter in texto:
        if caracter.lower() in abecedario:
            palabra = palabra + caracter
        elif caracter == " " and palabra != "": # Se verifica si el caracter actual es un espacio en blanco y si la variable palabra no esta vacia.
            contador = contador + 1 # Si ambas condiciones son verdaderas se incrementa el contador en 1 y se reinicia la variable palabra
            palabra = ""

    if palabra != "":
        contador = contador + 1 # Agrego una comprobacion adicional para verificar que la variable palabra este vacia, si no lo esta
                                # quiere decir que no conto la ultima palabra.

    return contador

def total_caracteres(texto):
    contador_caracteres = 0
    for caracteres in texto:
        contador_caracteres = contador_caracteres + 1 # Suma el contador cuando lee un caracter cualquiera
                                                      # Ya sea caracter vacio o de cualquier tipo

    return contador_caracteres

def caracteres_sin_espacio(texto):
    contador_caracteres_sin_espacio = 0

    for caracteres in texto:
        if caracteres != " ": # Cuento cada caracter salvo los caracteres en blanco o lo que vendria a ser un espacio
            contador_caracteres_sin_espacio = contador_caracteres_sin_espacio + 1

    return contador_caracteres_sin_espacio

def contar_parrafos(texto):
    contador_parrafos = 0
    en_parrafo = False # Utilizo esta variable como bandera para determinar si estamos dentro de un parrafo o no.
                       # Lo inicializo con false suponiendo que no lo estamos.
    for caracter in texto:
        if caracter == '\n': # Cuando encuentra un salto de linea, verifica si ya estabamos dentro de un parrafo
                             # "en_parrafo == True". Si es asi se incrementa el contador en 1 y se vuelve a establecer
                             # el parrafo en False.
            if en_parrafo:
                contador_parrafos += 1
                en_parrafo = False
        else:
            en_parrafo = True

            # en_parrafo es como un interruptor que nos dice si estamos actualmente dentro de un
            # parrafo o no. Cuando encontramos un salto de linea, si el interruptor esta activado
            # (True), sabemos que hemos encontrado un párrafo completo y lo contamos.
            # Luego, apagamos el interruptor (False) para estar listos para contar el siguiente
            # parrafo si lo encontramos.

    # Me aseguro de contar el ultimo parrafo si el texto no termina con salto de linea
    if en_parrafo:
        contador_parrafos += 1

    return contador_parrafos

def contar_lineas(texto):
    contador = 0

    for caracter in texto:
        if caracter == '\n': # Cuando se encuentre un salto de linea el contador aumenta en 1, ya que esto indica el fin de una linea
            contador += 1

    # Me aseguro de contar la última línea si el texto no termina con salto de línea
    if texto and texto[-1] != '\n':
        contador += 1

    return contador

print("Bienvendio al programa de estadisticas de texto.")
texto = input("Por favor ingrese su texto: ")
print(f"Estadisticas:\nPalabras: {contar_palabras(texto)}\nCaracteres (sin espacio): {caracteres_sin_espacio(texto)}\nCaracteres (con espacios): {total_caracteres(texto)}\nParrafos: {contar_parrafos(texto)}\nLineas: {contar_lineas(texto)}")