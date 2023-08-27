print('Digite os 3 números: ')
num1 = int(input('1º número: '))
num2 = int(input('1º número: '))
num3 = int(input('1º número: '))
nums = []

nums.append(num1)
nums.append(num2)
nums.append(num3)

maior_valor = max(nums)
print(f'O maior número é {maior_valor}')