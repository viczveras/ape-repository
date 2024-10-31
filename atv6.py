
jan = 1
fev = 2
mar = 3
abr = 4
mai = 5
jun = 6
jul = 7
ago = 8
set = 9
out = 10
nov = 11
dez = 12

num_mes = int(input('Qual o número do mês que você quer saber quantos dias tem? (1 à 12) '))

if num_mes == 1 or num_mes == 3 or num_mes == 5 or num_mes == 7 or num_mes == 8 or num_mes == 10 or num_mes == 12:
    print(f'O seu mês tem 31 dias!')
elif num_mes == 2:
    print(f'O seu mês tem 29 dias!')
else:
    print('O seu mês tem 30 dias!')
