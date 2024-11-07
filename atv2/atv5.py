aliquota01 = 0.04
aliquota02 = 0.06
aliquota03 = 0.08
aliquota04 = 0.1

valor_compra = float(input('Qual o valor da sua compra? '))

if valor_compra <= 100:
    print(f'O valor do seu cashback é de {aliquota01 * 100}%')
elif valor_compra > 100 and valor_compra <= 200:
    print(f'O valor do seu cashback é de {aliquota02 * 100}%')
elif valor_compra > 200 and valor_compra <= 400:
    print(f'O valor do seu cashback é de {aliquota03 * 100}%')
else:
    print(f'O valor do seu cashback é de {aliquota04 * 100}%')
