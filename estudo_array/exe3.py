# Programa para ler 06 (seis) números distintos. Exibir os números lidos ordenadamente.

numeros = []

while (len(numeros) < 6):
    
    num = int(input(''))
    
    if (not num in numeros):
        
        numeros.append(num)

numeros.sort(reverse=False)
print(numeros)

