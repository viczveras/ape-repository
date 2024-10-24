# Obtenção dos valores das notas
n1 = int(input('Qual sua primeira nota?: '))

n2 = int(input('Qual sua segunda nota?: '))

n3 = int(input('Qual sua terceira nota?: '))

# Realiza a soma primeiro, depois a divisão e transforma o resultado que seria float em int
soma = int((n1 + n2 + n3 ) / 3)
# Printa o resultado.
print(f"A sua média do semestre é: {soma}")

# Victor Véras