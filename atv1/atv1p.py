
Questão 1
# Recebe o valor de n1, número inteiro que vai ser checado se é par.
n1 = int(input('Digite um número maior que 0: '))
# checa, se n1 for divisivel por 2 e o resto for 0, o número é par, caso contrário, não é par.
if n1 % 2 == 0:
    print(f'O seu número {n1} é par!')
else:
    print(f'O seu número {n1} não é par :/')