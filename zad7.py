def funkcja():
    n = int(input('Podaj liczbę: '))

    x = 1
    for i in range(2, n + 1):
        x *= i
    print(x)

funkcja()