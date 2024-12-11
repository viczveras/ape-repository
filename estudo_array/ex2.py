# Ler 40 números inteiros positivos (distintos) e informar o maior e sua respectiva posição.

notas = []
maior = 0

for i in range(3):
    nota = int(input(''))
    notas.append(nota) #adiciona o valor da variavel nota a lista notas
    if (nota > maior): #se nota maior que maior, maior recebe nota, 
        maior = nota
print(f'Maior:{maior}, Posição: {notas.index(maior)}') # printa a maior nota, e notas.index(maior) mostra a posição na tabela da maior nota.