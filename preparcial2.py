import math
#declaración de vectores y variables necesarios 

numeros=[0]*100
numeros2=[0]*100
contador=0
suma = 0

#Ingreso los datos y realizo el encriptado, guardando los valores en un 2do vector 
for i in range (100):
    numeros[i]= int(input())
    suma = suma + numeros[i]
    contador = contador + 1
    if numeros[i]<=0 or numeros[i]>255: #verifico las condiciones, que sea entre 0 y 255 y en caso de ser 0 o mayor a 255, sale del ciclo. 
        break
numeros2[0]=numeros[0]

#Ignorando la primera posición, a las demás las resto con su posición anterior. 
for i in range (contador):
    if i!=0:
        numeros2[i]= numeros[i] - numeros[i-1] 

#verifico qué numeros son menores que 0, y en esos caso les sumo 255 
for i in range (contador):
    if numeros2[i]<0:
        numeros2[i] = numeros2[i]+255       

contador = contador - 1 #ignoro la posición del ultimo digito, el cero. 


#sacar el promedio y colocarlo en la ultima penultima posición
promedio = math.trunc(suma/(contador))
numeros2[contador+1] = promedio
numeros2[contador+2]=0

for i in range(contador+3): #sumo dos posiciones a la impresión para que se muestre el promedio y el cero del final. 
    print(numeros2[i])




