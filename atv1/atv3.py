n = int(input('Digite o primeiro número: '))
x = int(input('Deseja saber os múltiplos entre quanto a quanto? (Digite o 1º número) '))
y = int(input('Deseja saber os múltiplos entre quanto a quanto? (Digite o 2º número) '))

# Cria uma sequência de números começando em x e terminando em y (inclusive y, por isso +1)
for num in range(x, y + 1):
    #se o número for múltiplo de n, % = 0, 
    if num % n == 0:
        print(f'{num}', end=' ')
