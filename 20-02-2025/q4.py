codigo = input('Digite um código alfanumérico: ')

for numero in '0123456789':
    codigo = codigo.replace(numero, '*')

print('Nova string:', codigo)
