n = int(input('Quantos números você quer checar?: '))

soma = 0

while True:
    numero = int(input('Qual número deseja somar? (digite 0 para parar): '))

    if numero == 0:
        break

    soma += numero

    if soma > 100:
        break

print(f'A soma de todos os números lidos é {soma}.')
