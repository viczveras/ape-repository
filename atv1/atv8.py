
valor_total = 0
total_cashback = 0
numero_de_vendas = 400

# loop para ler os valores das compras e calcular o cashback
for i in range(numero_de_vendas):
    valor_compra = float(input(f'Digite o valor da compra {i+1}: '))

    # Acumula o valor total arrecadado
    valor_total += valor_compra

    # Calcula o cashback com base no valor da compra
    if valor_compra <= 100:
        cashback = valor_compra * 0.04
    elif valor_compra <= 200:
        cashback = valor_compra * 0.06
    elif valor_compra <= 400:
        cashback = valor_compra * 0.08
    else:
        cashback = valor_compra * 0.10

    # Acumula o valor do cashback total
    total_cashback += cashback

# Exibe o valor total arrecadado e o valor total do cashback gerado
print(f'Valor total arrecadado: R$ {valor_total:.2f}')
print(f'Valor total do cashback gerado: R$ {total_cashback:.2f}')
