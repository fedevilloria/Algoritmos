TAM = 5
num = [0] * TAM
for i in range(TAM):
    num[i] = int(input(f"Ingrese {i+1}º numero: "))
for i in range(TAM-1):
    for j in range(i+1,TAM):
        if(num[i] < num[j]):
            cambio = num[i]
            num[i] = num[j]
            num[j] = cambio
for i in range(TAM):
    print(num[i])