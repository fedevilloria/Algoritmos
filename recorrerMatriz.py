matriz = [['a','o','r'],['l','j','e'],['f','a','s']]

for i in range (3):
    print (matriz[i])
concatenarResultado = ''
for i in range (len(matriz)):
    if i % 2 == 0:
        for j in range (len(matriz)):
            concatenarResultado += matriz[j][i]
    elif i % 2 == 1:
        for k in range (len(matriz)-1,-1,-1):
            concatenarResultado += matriz[k][i]

print (concatenarResultado)