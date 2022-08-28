# Написать функцию square, принимающую 1 аргумент — сторону квадрата,
# и возвращающую 3 значения (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.

import math

def square(args):
    per = args * 4
    pl = args ** 2
    diag = float(args * math.sqrt(2))
    return (per, pl, diag)

print(square(int(input('Введите сторону квадрата: '))))