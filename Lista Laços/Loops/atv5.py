quantidade_num = int(input('Digite a quantidade de números que voce quer escrever: '))
num = []

for i in range(1, quantidade_num+1):
    val = int(input(f'Digite o {i}º número: '))
    num.append(val)

maior_valor = max(num)
print(f'O maior número é {maior_valor}')