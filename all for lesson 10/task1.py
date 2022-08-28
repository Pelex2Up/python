# string_set = {'Nicolas', 'Michelle', 'John', 'Mercy'}
# print(string_set)
# mix_set = {2.0, 'Nicolas', (1, 2, 3)}
# print(mix_set)
# arr = [1, 2, 3, 4, 3, 6, 2, 1]
# s1 = set(arr)  # присвоение типа "множество" через команду set (множество удаляет все дубликаты из списка)
# print(s1)
# x = {}  # так создается пустой словарь!
# print(type(x))
# y = set()  # создание пустого множества
# print(type(y))
#
# month = {'Jan', 'Feb', 'March', 'April'}
#
# for i in month:
#     print(i, end=' ')
#
# print(f"\n{'May' in month}")
# month.add('May')  # добавление элемента в множество
#
# for i in month:
#     print(i, end=' ')
#
# print(f"\n{'May' in month}")
# month.discard('May')  # удаление элемента из множества, если эл-та не будет, не выдает ошибку и код работает дальше
# print(f"{'May' in month}")
# month.remove('Feb')  # еще одно удаление элемента как в списках, только, если эл-та не будет в множестве, выдаст ошибку
# print(month)

# num_set = {1, '1', '2', '3'}
# print(num_set)
# print(f"{num_set.pop()}, {num_set}")
# # num_set.clear()  # полностью очищает множество от элементов
# # print(num_set)
#
# num_set_1 = {2, 3, 4}
# n1 = num_set_1.union(num_set)  # объединение двух (a и b) множеств в одно "a.union(b)"
# print(n1)
# num_set_2 = {5, 6}
# n1 = num_set.union(num_set_2, num_set_1)  # метод .union() может объединять неограниченное количество множеств

# n1 = {1, 2, 3, 4, 5}
# n2 = {2, 3, 4, 5, 6}
# print(n1 | n2)  # метод | объединяет множества точно так же, как .union()
# print(n1 & n2)  # метод & возвращает повторяемые элементы из двух множеств
# # так же вывод повторяемых элементов множеств (а и b) можно писать через a.intersection(b)
# a = {1, 2, 3}
# b = {4, 3, 6}
# print(a - b)  # через вычитание, вычитаются элементы списка b из списка a. Результат: 1, 2
# print(b - a)  # Результат: 4, 6

# cоздание полностью неизменяемого множества через frozenset()
# a = frozenset([1, 2, 3, -40, 10])
# print(type(a))
#
# num = [1, 2, 3, 4, 2, 1, 2, 3]
# num_set = set(num)
# num_set1 = list(num_set)
# if num == num_set1:
#     print('Дубликатов нет')
# else:
#     print("Дубликаты есть")

num_set_1 = set([1, 2, 3, 4, 5, 6])
num_set_2 = frozenset([2, 3, 4, 5, 6, 7])
print(num_set_1 | num_set_2)
print(num_set_1 & num_set_2)