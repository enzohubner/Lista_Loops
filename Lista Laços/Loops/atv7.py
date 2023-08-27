num = int(input('Digite o número que você deseja calcular o fatorial: '))

i = num - 1
res = 1

res *= num*i
while i > 1:
    i -= 1
    res *= i

print(f'O fatorial de {num} é {res}')