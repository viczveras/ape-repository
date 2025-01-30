matriz = [
    [10, 20, 30, 40],  
    [50, 60, 70, 80],  
    [90, 100, 110, 120]   
]

print(matriz[0][2])

matriz[2][2] = 200

for i in range (len(matriz[1])):
    matriz[1][i] *= 2 
############################################################    
soma = 0 

for j in range (len(matriz[0])):
        soma += matriz[0][j]
        
print(soma)
############################################################
sum2 = 0

for i in range(len(matriz)):
    sum2 += matriz[i][3]

print(sum2)

sum_valores = 0
num_elementos = 0
############################################################

for i in range(len(matriz)):
    for j in range(len(matriz)):
        sum_valores += matriz[i][j]
        num_elementos += 1
        
media = sum_valores / num_elementos
print(f'A média é {media}')

############################################################

new_line = [130,140,150,160]

matriz.append(new_line)

for linha in matriz:
    print(linha)
    
############################################################


soma_diagonal_principal = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i == j:
            soma_diagonal_principal += matriz[i][j]

print(soma_diagonal_principal)

    
############################################################

 
acima_media = 0 

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] > media:
            acima_media += 1
print(acima_media)