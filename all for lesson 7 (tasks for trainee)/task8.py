# Даны два целых числа m и n (m≤n). Напишите программу, которая  выводит все числа от m до n включительно.
while True:
    m = int(input('Введите первое число: '))
    n = int(input('Введите второе число: '))
    if n > m:
        for x in range(m, n+1):
            print(x, end=' ')
        break
    else:
        print('Второе число меньше первого, введите числа заново!')