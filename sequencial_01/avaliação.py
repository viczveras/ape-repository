# Recebe o tempo da avaliação em minutos
tempo_avaliacao = int(input('Qual a duração da prova realizada? (Responda em minutos!)' ))
                      
# Declara o tempo da aula no ifpb
tempo_aula = 50 

aulas_necessarias = int(tempo_avaliacao / tempo_aula)

# Mostra a quantidade de aulas que são necessárias para realizar a prova

print(f"A quantidade de aulas necessárias para realizar a avaliação é: {aulas_necessarias} aulas")

                     
# Victor Véras