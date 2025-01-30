print('Digite a ordem da matriz: ')

nlin = int(input('Digite o número de linhas: '))
ncol = int(input('Digite o número de Colunas: '))

matriz = []

for i in range(nlin):
    matriz.append([None]*ncol)
    
print('Digite os elementos da matriz: ')

for i in range(nlin):
    for j in range(ncol):
        matriz[i][j] = int(input(f'Elemento {i},{j}: '))
        
print('Matriz =', matriz)

soma = 0

for i in range(nlin):
    for j in range(ncol):
        soma += matriz[i][j]
        
print('Soma',soma)