# 1) Cargar los datos basicos (apellido, nombre, numero de documento) de 10 clientes diferentes y grabarlos en un
# archivo denominado cliente.txt

archivo = open("cliente.txt", "a+")

vacio = True
for linea in archivo.read():
    if len(linea) > 0:
        vacio = False
    else:
        archivo.write("Documento     Apellido     Nombre     Legajo\n")

if archivo.read() == "":
    archivo.write("Documento     Apellido     Nombre     Legajo\n")

for i in range(2):
    dni = input("Ingrese el DNI: ")
    apellido = input("Ingrese el Apellido: ")
    nombre = input("Ingrese el Nombre: ")
    legajo = input("Ingrese el legajo: ")
    registro = f"{dni}     {apellido}     {nombre}     {legajo}\n"
    archivo.write(registro)
archivo.close()
