import math
x = int(input('Введите x: '))
y = int(input('Введите y: '))
z = (math.fabs(x) - math.fabs(y)) / (1 + math.fabs(x * y))
print('Результат вычисления: ', z)
