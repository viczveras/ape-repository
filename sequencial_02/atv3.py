#Recebe os nomes e as idades
first_person = input('Primeira pessoa, digite seu nome: ')
fp_age = int(input('Primeira pessoa, digite sua idade: '))
second_person = input('Segunda pessoa, digite seu nome: ')
sp_age = int(input('Segunda pessoa, digite sua idade: '))
# Se a idade 1 for maior que a idade 2, printe, caso contrario, print2
if fp_age > sp_age:
    print(f'Olá {first_person}, você é o mais velho!')
if sp_age > fp_age:
    print(f'Olá {second_person}, você é o mais velho!')
if sp_age == fp_age:
    print(f'{first_person},{second_person}, vocês tem a mesma idade!')

    