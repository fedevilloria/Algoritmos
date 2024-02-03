categoria = input()
contador = 0

archivo = open('datos.csv', 'r')

for linea in archivo:
    campos = linea.split(',')
    if len(campos) >= 2 and campos[1].strip() == categoria:
        contador += 1

archivo.close()

print(contador)