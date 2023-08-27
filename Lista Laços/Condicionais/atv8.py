print('Escreva 3 números')
num = []
num1 = int(input('Escreva o primeiro número: '))
num2 = int(input('Escreva o segundo número: '))
num3 = int(input('Escreva o terceiro número: '))

num.append(num1)
num.append(num2)
num.append(num3)

maior_num = max(num)
print(f'O maior número é {maior_num}')