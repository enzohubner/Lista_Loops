lado1 = int(input('Digite o valor do 1º lado do triângulo: '))
lado2 = int(input('Digite o valor do 2º lado do triângulo: '))
lado3 = int(input('Digite o valor do 3º lado do triângulo: '))

if lado1 == lado2 and lado1 == lado3:
    print('Este é um triângulo equilátero')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('Este é um triângulo isóceles')
else:
    print('Este é um triângulo escaleno')