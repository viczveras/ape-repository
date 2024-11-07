# Inicializa contadores para os votos
votos_sim = 0
votos_nao = 0
votos_invalidos = 0

# Total de pessoas que votaram
total_votos = 80

# Loop para ler os votos das 80 pessoas
for i in range(total_votos):
    voto = input(f'Digite o voto da pessoa {i+1} (SIM ou NAO): ')

    if voto == "SIM" or voto == "sim" or voto == "Sim":
        votos_sim += 1
    elif voto == "NAO" or voto == "nao" or voto == "Nao":
        votos_nao += 1
    else:
        votos_invalidos += 1

# Calcula as porcentagens
percentual_sim = (votos_sim / total_votos) * 100
percentual_nao = (votos_nao / total_votos) * 100
percentual_invalidos = (votos_invalidos / total_votos) * 100

# Exibe os resultados
print(f'Porcentagem de votos SIM: {percentual_sim:.2f}%')
print(f'Porcentagem de votos NAO: {percentual_nao:.2f}%')
print(f'Porcentagem de votos inválidos: {percentual_invalidos:.2f}%')
