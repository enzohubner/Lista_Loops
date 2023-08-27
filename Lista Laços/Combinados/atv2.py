print('ESTE É UM PROGRAMA QUE TE DIZ O MENOR NÚMERO DOS QUE VOCÊ DIGITAR...')

numTot = []

while True:
    contuniar = input('Deseja continuar? [s] ou [n]')
    if contuniar == 'n':
        break
    num = float(input('Digite um número: '))
    numTot.append(num)

menor = min(numTot)
print(f'O menor número é o {menor}')