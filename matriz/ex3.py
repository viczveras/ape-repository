n = int(input('Digite a ordem da matriz: '))

matriz = []

for i in range(n):
    matriz.append([None]*n)

for i in range(n):
    for j in range(n):
        matriz[i][j] = i + j 
        
for i in range(n):
    for j in range(n):
        print(f'{matriz[i][j]:4}',end='')
    print()