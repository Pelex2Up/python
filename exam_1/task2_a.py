import math

a = int(input('Введите число а: '))
s1 = (1 + a + a**2) / (2 * a + a**2)
s2 = (1 - a + a**2) / (2 * a - a**2)
y1 = math.pow(s1 + 2 - s2, -1) * (5 - 2 * math.pow(a, 2))
print('Результат вычисления =', y1)