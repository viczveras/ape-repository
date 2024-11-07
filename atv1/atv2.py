celsius = 0
# Declara que deve ir até 100, declara a formula de farenheit, e concatena o valor de celsius previamente e o valor de farenheit
for celsius in range(0, 101):
    fahrenheit = celsius * 1.8 + 32
    print(f'{celsius}º Celsius é equivalente a {fahrenheit}º Fahrenheit')


    