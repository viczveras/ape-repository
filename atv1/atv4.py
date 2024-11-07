n = int(input('Digite o primeiro número: '))
x = int(input('Deseja saber os múltiplos entre quanto a quanto? (Digite o 1º número) '))
y = int(input('Deseja saber os múltiplos entre quanto a quanto? (Digite o 2º número) '))

# Variável para contar os múltiplos
multiplos = 0

# Cria uma sequência de números começando em x e terminando em y (inclusive y, por isso +1)
for num in range(x, y + 1):
    # Verifica se o número é múltiplo de n
    if num % n == 0:
        multiplos += 1

print(f'A quantidade de múltiplos de {n} entre {x} e {y} é: {multiplos}')
