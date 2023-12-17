# modulo que va a permitir elegir números aleatoriamente
import random

# el conjunto de símbolos válidos en el código
digitos = ('0','1','2','3','4','5','6','7','8','9')

# "elegimos" el código
codigo = ''
for i in range(4):
    candidato = random.choice(digitos)
    # vamos eligiendo digitos no repetidos*
    while candidato in codigo:
        candidato = random.choice(digitos)
    codigo = codigo + candidato

# iniciamos interaccion con el usuario*
print("Bienvenido/a al Mastermind!")
print("Tenés que adivinar un número de 4 cifras distintas")
propuesta = input("Que número proponés?: ")

# procesamos las propuestas e indicamos aciertos y coincidencias
intentos = 1
while propuesta != codigo:
    intentos = intentos + 1
    aciertos = 0
    coincidencias = 0

    # recorremos la propuesta y verificamos en el código
    for i in range(4):
        if propuesta[i] == codigo[i]:
            aciertos = aciertos + 1
        elif propuesta[i] in codigo:
            coincidencias = coincidencias + 1
    print(f"Tu propuesta ( {propuesta} ) tiene {aciertos} aciertos y {coincidencias} coincidencias.")
    # pedimos siguiente propuesta*
    propuesta = input("Proponga otro número: ")

print(f"Felicitaciones! Adivinaste el número en {intentos} intentos.")