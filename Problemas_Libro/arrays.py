nombres = []
identificaciones = []
tamano = 3
for i in range(tamano):
    print("Ingrese los datos de la persona", i+1)
    nombre = input("Nombre: ")
    identificacion = input("Identificacion: ")
    nombres.append(nombre)
    identificaciones.append(identificacion)

for i in range(tamano):
    print("Mostrando los datos de la persona", i+1)
    print("Nombre: ", nombres[i])
    print("Identificacion: ", identificaciones[i])