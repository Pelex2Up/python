# import random
# x = tuple([random.randint(0, 5) for i in range(5)])
# y = tuple([random.randint(-5, 0) for e in range(5)])
# print('Первый кортеж:', x)
# print('Второй кортеж:', y)
# z = x + y
# print('Количество нулей в объединённом кортеже', z, 'составляет:', z.count(0))
# print(x)
# print('Минимальное значение кортежа:', min(x), '\nМаксимальное значение кортежа:', max(x))

# x = (1, 2, '3', 'e', 'asw')
# z = ','.join(x)
# print(z)

A = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
B = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)
sum1 = 0
sum2 = 0
print('A:', A, '\nB:', B)
for i in A:
    sum1 += i
for x in B:
    sum2 += x
if sum1 > sum2:
    print('Сумма элементов больше в кортеже А', sum1, '>', sum2)
else:
    print('Сумма элементов больше в кортеже B.', sum2, '>', sum1)
print('Минимальное значение кортежа А:', min(A), '\nМинимальное значение кортежа B:', min(B))