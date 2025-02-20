palavras = []

contagens = []


while True:
    palavra = input("Digite uma palavra (ou 'fim' para terminar): ").lower()
    if palavra == "fim":
        break
    if palavra in palavras:
  
        indice = palavras.index(palavra)
        contagens[indice] += 1
    else:
        
        palavras.append(palavra)
        contagens.append(1)

for i in range(len(palavras)):
    print(f"{palavras[i]}: {contagens[i]}")
