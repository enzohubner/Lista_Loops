import random

print('ESTE É UM PROGRAMA QUE ESCOLHE UM NÚ,ERO DE 1 A 10 E VOCÊ TEM QUE ADIVINHAR...')

numero_aleatorio = random.randint(1, 10)
print("O número aleatório é:", numero_aleatorio)

while True:
    tent = float(input('Tente adivinhar o número: '))
    if tent == numero_aleatorio:
        print('Você descobriu, Parabéns!')
        break