# Recebe os valores das aulas assistidas e perdidas
aulas_assistidas = int(input('Quantas aulas você assistiu? '))
aulas_perdidas = int(input('Quantas aulas você perdeu? '))

# Calcula o total de aulas
total_aulas = aulas_assistidas + aulas_perdidas

# Calcula a frequência e converte para inteiro
freq = int((aulas_assistidas / total_aulas) * 100)

# Exibe a frequência
print(f'A sua frequência é de {freq}%')

# Victor Véras