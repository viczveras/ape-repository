
n1 = int(input('Qual sua primeira nota? '))

n2 = int(input('Qual sua segunda nota? '))

n3 = int(input('Qual sua terceira nota? '))

n4 = int(input('Qual sua quarta nota? '))

media_semestral = (n1 + n2 + n3 + n4) / 4 

nota_final = int(input('Qual foi a sua nota da prova final? '))

#MF = 60% da MS + 40% da NF

media_final = (6 * media_semestral / 10) + (4 * nota_final / 10)

#Printa o resultado das operações
print(f'A Sua média final é de: {media_final}')

# Victor Véras
