import math

a = float(input('Введите первый катет треугольника: '))
b = float(input('Введите второй катет треугольника: '))
c = math.sqrt(b**2 + a**2)
pl = 0.5 * (a * b)
print('Длина гипотенузы равна: ', c, '/n Площадь треугольника равна: ', pl)