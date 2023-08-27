print('ESTE É UM PROGRAMA QUE CALCULA A NOTA DE QUANTOS ALUNOS QUISER...')
print('Quando quiser parar, digite no campo NOME a palavra >[parar]<')

continuar = True
nomeTot = []
notaTot = []
soma_media = 0
media = 0

while continuar:
    nome = input('Digite o nome do aluno: ')
    if nome == 'parar':
        break
    nota = int(input(f'Digite o nome de {nome}: '))
    nomeTot.append(nome)
    notaTot.append(nota)

cont = 0
for i in notaTot:
    soma_media += i
    cont += 1

media = soma_media/cont
print(f'A média das notas é igual a {media}')