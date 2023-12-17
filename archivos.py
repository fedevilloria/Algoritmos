archivo = open("localidades.txt", "r") # Se abre en modo de lectura
print(archivo.read()) # Lee TODO el contendio del archivo.

archivo.seek(0) # El puntero regresa a la linea 0.
linea1 = archivo.readline()
print(linea1)

# Mostrar el registro 4 de un archivo
archivo.seek(0) # Vuelvo a la linea 0 del puntero
rengolnes = archivo.readline() # Guarda las lineas en posiciones de vectores
print(rengolnes[3])

# Mostrar la primer columna
archivo.seek(0)
for i in archivo:
    campo = i.split(";") # Divide los campos y lo guarda en la variable
    if len(campo) >= 2:
        cod_postal = campo[0].strip() # Strip quita los espacios en blanco
                    # el 0 representa la columna
        print(cod_postal)

# Mostrar el contenido de un solo campo
archivo.seek(0)
bandera = int(0)
for i in archivo:
    campo = i.split(";")
    if campo[0] == "5186":
        bandera = 1
if bandera == 1:
    print("Existe.")
else:
    print("No existe.")