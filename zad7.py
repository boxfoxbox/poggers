def funkcja():
    n = int(input('Podaj liczbę całkowitą nieujemną: '))
    if n < 0:
        print('Liczba musi być nieujemna')
    else:
        x = 1
        for i in range(2, n + 1):
            x *= i
        print(x)

funkcja()