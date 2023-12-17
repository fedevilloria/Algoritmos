#Recibir un valor de punto flotante con dos números decimales. 
#Este valor representa un valor monetario. 
#Luego de esto, calcular el menor numero posible de billetes y monedas en los cuales su valor puede ser descompuesto. 
#Los billetes a tener en cuenta son de 100, 50, 20, 10, 5, 2. Las monedas posibles son de 1, 0.50, 0.25, 0.10, 0.05 y 0.01. 
#Mostrar el mensaje "NOTAS:" seguido de una lista de billetes y el mensaje "MOEDAS:" seguido de una lista de monedas.

valor = float(input())
cant_100 = 0
cant_50 = 0
cant_20 = 0
cant_10 = 0
cant_5 = 0
cant_2 = 0

#billetes 
if valor/100 >= 1:
    cant_100 = int(valor/100)
    valor = valor - (cant_100*100)

if valor/50 >=1:
    cant_50 = int(valor/50)
    valor = valor - (cant_50*50)

if valor/20 >=1:
    cant_20 = int(valor/20)
    valor = valor - (cant_20*20)

if valor/10 >=1:
    cant_10 = int(valor/10)
    valor = valor - (cant_10*10)  

if valor/5 >=1:
    cant_5 = int(valor/5)
    valor = valor - (cant_5*5) 

if valor/2 >=1:
    cant_2 = int(valor/2)
    valor = valor - (cant_2*2)


#monedas 
cant_1 = 0
cant_050 = 0
cant_025 = 0
cant_010 = 0
cant_005= 0
cant_001 = 1

if valor/1 >=0:
    cant_1 = int(valor/1)
    valor = valor - (cant_1)
if valor/0.5>=0:
    cant_050 = int(valor/0.5)
    valor = valor - (cant_050*0.5)
if valor/0.25>=0:
    cant_025 = int(valor/0.25)
    valor = valor - (cant_025*0.25)
if valor/0.1>=0:
    cant_010 = int(valor/0.1)
    valor = valor - (cant_010*0.1)
if valor/0.05>=0:
    cant_005 = int(valor/0.05)
    valor = valor - (cant_005*0.05)
if valor/0.01>=0:
    cant_001 = int(valor/0.01)
    valor = valor - (cant_001*0.01)

if valor >= 0.001:
    cant_001 = cant_001 +1


print('NOTAS:')
print (f'{cant_100} nota(s) de R$ 100.00')
print(f'{cant_50} nota(s) de R$ 50.00')
print(f'{cant_20} nota(s) de R$ 20.00')
print(f'{cant_10} nota(s) de R$ 10.00')
print(f'{cant_5} nota(s) de R$ 5.00')
print(f'{cant_2} nota(s) de R$ 2.00')

print('MOEDAS:')
print(f'{cant_1} moeda(s) de R$ 1.00')
print(f'{cant_050} moeda(s) de R$ 0.50')
print(f'{cant_025} moeda(s) de R$ 0.25')
print(f'{cant_010} moeda(s) de R$ 0.10')
print(f'{cant_005} moeda(s) de R$ 0.05')
print(f'{cant_001} moeda(s) de R$ 0.01')
    
