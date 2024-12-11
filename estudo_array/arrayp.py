# Inicializa a lista com 7 elementos vazios
semana = [0] * 7

# Loop para preencher a lista com os dias da semana
for i in range(7):
    semana[i] = input('Digite os dias da semana: ')

# Loop para imprimir todos os dias da semana
for dia in semana:
    print(dia)

aux = semana[0]
semana[0] = semana[6]
semana[6] = aux 
print('-------------------')
print('Abaixo o índice 0 foi trocado com o índice 6')
print(semana[0],semana[6])