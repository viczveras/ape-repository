
n, r = input().strip().split()
N = int(n)  
R = int(r)  


valores_sensores = input().strip().split()


resultados = []
for valor in valores_sensores:
    valor_sensor = int(valor)
    if valor_sensor <= R:
        resultados.append('1')
    else:
        resultados.append('0')


print(' '.join(resultados))
