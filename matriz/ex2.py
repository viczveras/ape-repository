import random

nlin = int(input('Digite o número de linhas: '))
ncol = int(input('Digite o número de colunas: '))

matriz = [[None]*ncol for _ in range(nlin)]
        
for i in range(nlin):
    for j in range(ncol):
        matriz[i][j] = random.randint(1,20)
        
for linha in matriz:
    print(linha)

maior = matriz[0][0]

for i in range(nlin):
    for j in range(ncol):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            
print('Maior =',maior)