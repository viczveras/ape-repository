# contador das medidas válidas
medidas = 0

# loop para ler medidas de 6 pirâmides
for i in range(6):
    print(f'Pirâmide {i+1}:')
    a = float(input('Digite o valor do lado a: '))
    b = float(input('Digite o valor do lado b: '))
    c = float(input('Digite o valor do lado c: '))

    # verifica a condição de existência do triangulo
    if a + b > c and a + c > b and b + c > a:
        # encrementa 1, contando essa medida como válida.
        medidas += 1

# exibe a quantidade de medidas válidas
print(f'O número de medidas válidas é: {medidas}')
