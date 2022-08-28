# kort = (1, 2, 3, 4, 5, 6)
# kort1 = (1,)
# a = [1, 2, 3, 4, 5, 6]
# kort2 = (1) # без запятой выводится не как кортеж, а как переменная (типа int в данном случае)
# print(kort, kort1, kort2)
# print(kort.__sizeof__()) # кортеж занимает меньше ОЗУ, и защищен от случайных изменений
# print(a.__sizeof__())
# print(a, id(a))
# b = tuple(a)
# print(b, id(b))
# c = list(b)
# print(c, id(c))

# Списки внутри кортежей можно изменять!!!
n = (1, 'do', ['par1', 1, 2])
n[2][0] = 15
print(n, id(n))
n1 = (2, 3, 4)
print(n1, id(n1))
print(n + n1, id(n + n1)) # кортежи так же можно складывать, умножать и они образуют новый кортеж.
# !!!! НЕЛЬЗЯ СКЛАДЫВАТЬ КОРТЕЖ С ДРУГИМИ ТИПАМИ ДАННЫХ (массив, строка, список и т.д.) !!!! #
print(n * 3, id(n * 3))
n2 = n * 3
# count(х)  считает количество повторений элемента "x" внутри кортежа
# len(x) считает длину (или количество элементов) кортежа "х"
print(n2.count(1), len(n2))
# max(x) или min(x) возвращает максимальное или минимальное значение в кортеже "х"
print()
print()
s1 = ('a', 'ab', 'e', 'gsaaw01')
s2 = (1, 2, 5, 7, 100)
print(max(s2), "\n", min(s2))
print(max(s1), "\n", min(s1))
