
idade_maxima = 0
idade_minima = 100 

numero_de_pessoas = 40

for i in range(numero_de_pessoas):
    idade = int(input(f'Digite a idade da pessoa {i + 1}: '))
    
    if idade > idade_maxima:
        idade_maxima = idade

    if idade < idade_minima:
        idade_minima = idade

print(f'A idade da pessoa mais velha é: {idade_maxima} anos')
print(f'A idade da pessoa mais nova é: {idade_minima} anos')
