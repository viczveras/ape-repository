# Recebe a quantidade de alunos que foram aprovados e reprovados
quantidade_aprovados = int(input('Quantos alunos foram aprovados na matéria? '))
quantidade_reprovados = int(input('Quantos alunos foram reprovados na matéria? '))

# Calcula a quantidade total de alunos da turma
quantidade_alunos = quantidade_aprovados + quantidade_reprovados 
# Calcula primeiramente a quantidade de aprovados vezes 100 para receber um valor int e não um float
porcentagem_aprovados = (quantidade_aprovados * 100) // quantidade_alunos
# Printa o resultado.
print(f'A porcentagem de alunos aprovados na turma de APE é de : {porcentagem_aprovados}%')

# Victor Véras