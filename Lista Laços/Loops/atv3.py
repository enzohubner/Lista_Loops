numero = int(input('Você quer a tabuada de qual número? '))

for i in range(1, 11):
    resultado = numero * i
    print(f'{i} x {numero} = {resultado}')