# Programa para ler as notas [0,100] de 30 (trinta) alunos. Calcule e exiba, para cada nota múltiplo de 10, quantas pessoas
# tiveram a respectiva nota.

notas = []

for i in range(30):
    notas.append(int(input('Digite as notas: ')))
    
for i in range(10,101,10):
    print(i, notas.count(i))