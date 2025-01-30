# Inicializa a lista com 7 elementos vazios
semana = [0] * 7

# Loop para preencher a lista com os dias da semana
for i in range(len(semana)):
    semana[i] = int(input('Digite os dias da semana: '))

# Loop para imprimir todos os dias da semana
for dia in semana:
    print(dia)

# Troca os valores nos índices 0 e 6 usando XOR
semana[0] = semana[0] ^ semana[6]
semana[6] = semana[0] ^ semana[6]
semana[0] = semana[0] ^ semana[6]

print('-------------------')
print('Abaixo o índice 0 foi trocado com o índice 6')
print(semana[0], semana[6])
