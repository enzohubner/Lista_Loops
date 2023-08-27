print('Digite de que númeo ate que numero você desja saber quantos primos tem:')
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
par = 0
impar = 0

for i in range(num1, num2+1):
    if i%2 == 0:
        par +=1
    else:
        impar +=1

print(f'Existem {par} números pares.')
print(f'Existem {impar} números impares.')