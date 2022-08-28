while True:
    m = int(input('Введите число "m": '))
    n = int(input('Введите число "n": '))
    if m <= n:
        for i in range(m, n + 1):
            if i == n:  # добавлено только для красоты.
                print(i, end='.')
            else:
                print(i, end=', ')
        break
    else:
        print('Число "m" должно быть меньше числа "n"!')
