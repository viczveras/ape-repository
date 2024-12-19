a = 3 # 0 1 1 
b = 4 # 1 0 0 


print(a,b)




a = a ^ b 
# a | 0 1 1
# b | 1 0 0
# primeiro xor (SOMA BINÁRIOS)
# a | 1 1 1 

b = a ^ b 
# a | 1 1 1 
# b | 1 0 0 
# b | 0 1 1 RESULTADO XOR


a = a ^ b
# a | 1 1 1 
# b | 0 1 1 
# a | 1 0 0 


print(a,b)