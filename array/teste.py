a = 50
b = 100000
print(a,b)
print('------')

a = a ^ b
b = a ^ b 
a = a ^ b 

print(a,b)