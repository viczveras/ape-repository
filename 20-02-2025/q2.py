palavra = input('Digite uma palavra: ')
for i in range(len(palavra)):
    print(palavra[i].ord())
    print(palavra[i].bin())
    print(palavra[i].hex())
    print(palavra[i].oct())
