n = int(input('Quantos números você deseja checar?: '))

contador = 0 

while contador < n:
    numero = int(input('Digite um número: '))
    
    if numero % 2 == 0:
        print(f'Seu número {numero} é par')
    else:
        print(f'Seu número {numero} é ímpar')
    # Garante que não haja um loop infinito.
    contador += 1
