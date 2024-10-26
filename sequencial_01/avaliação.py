# Recebe a duração da avaliação em minutos
tempo_minutos = int(input('Qual a duração da prova realizada? (Responda em minutos!)'))

# Transforma o tempo em minutos para segundos
tempo_segundos = tempo_minutos * 60

# Cada aula possui 50 minutos, o código abaixo transforma em segundos
aula_em_segundos = 50 * 60

# Calcula a quantidade de aulas necessárias para realizar a avaliação e recebe em inteiro e não float
aulas_necessarias = int(tempo_segundos / aula_em_segundos)

# Exibe os resultados
print(f"O Tempo para realizar a prova em segundos é: {tempo_segundos} segundos")
print(f"A quantidade de aulas necessárias para realizar a avaliação foi de: {aulas_necessarias} aulas")

# Victor Véras