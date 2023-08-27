qt_numeros_fibonacci_total = int(input('Quantos números Fibonacci você quer gerar?'))

qt_numeros_fibonacci = 1
x = 1
y = 1
r = 0

z = 0

if qt_numeros_fibonacci_total == 1:
    print(y)
else:
    print(y)

    while True:
        r = x + y
        print(f'{r}, ')
        y = x
        x = r
        qt_numeros_fibonacci += 1

        if qt_numeros_fibonacci == qt_numeros_fibonacci_total:
            break