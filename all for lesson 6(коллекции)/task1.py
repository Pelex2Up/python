# import random
# c = [random.randint(1,100) for i in range(10)] #создание строки со случайными 10 цифрами от 1 до 100(пример)
# print(c)
#
# print(c[0],end=' ')
# print(c[-1],end=' ')
# print(c[5],end=' ')
# print(c[-4])
# print(list(c))
# y = str('Я люблю пайтон')
# y = list(y)
# y.append(c)
# c = list(y)
# print(c)

# b = 1000
# mas1 = [1, 3, 'a', 6, 'b']
# mas1.insert(3, b)  # Добавление в массив элементов без замены существующих!!!
# # insert(a,b) а - индекс нового элемента, b - сам элемент
# print(mas1)
# print(mas1[3])
# mas1[2] = 'kekw'  # замена элемента в массиве.
# print(mas1)
# mas1.remove(1)  # удаление элемента в списке (только первое вхождение элемента в список!).
# print(mas1)
# del mas1[3]  # удаление по индексу из массива
# print(mas1)

# my_list = ['hello', 'world']
# list1 = [0, 1, 2, my_list, 4, 5, 6]
# print(list1[3][0])  # обращение к вложенному массиву my_list в массиве list
# del list1[3][1]  # удаление элемента с индексом 1 из вложенного массива my_list через массив list
# print(list1)
# my_list.append('world')  # добавлять элементы во вложенный массив можно только обращаясь ко вложенному массиву
# print(list1)

# import random
# mas1 = [random.randint(1, 10) for i in range(3)]
# print(mas1)
# if 1 in mas1:
#     print('Wassup!')

# d = [0, 1, 2, 3, 4]
# e = [5, 6, 7, 8]
# c = d + e
# print(d, e)
# print(c)
# d.extend(e)  # добавление в массив другого массива, не делая его вложенным!!!
# и не создавая новый массив как при сложении
# print(d)
# print(id(c))
# print(id(d))

# a = [0, 1, 2, 3, [0, 1, 2]]
# b = a
# print(a, id(a))
# print(b, id(b))
# b = a.copy()  # правильное копирование массивов без сохранения адреса к изначальному массиву
# print(b, id(b))
# b.append(4)
# print(b, id(b))

# Дан список. Представьте его в обратном порядке.
# a = [0, 1, 2, 3]
# print(a[::-1])
# a.reverse()
# print(a)

import random
a = [random.randint(1,21) for i in range(10)]
if 20 in a:
    ind = a.index(20)
    a[ind] = 200
print(a)

