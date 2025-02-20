palavra = input('Digite uma plavra: ')
palavra_python = 'PYTHON'
caracteres_iguais = 0 
for i in range(len(palavra)):
    for j in range(len(palavra_python)):
        if palavra[i].upper() == palavra_python[j]:
            caracteres_iguais += 1 
            break
print(caracteres_iguais)
