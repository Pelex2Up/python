# dict1 = {"dict": 1,
#          "dictionary": 2}
# print(dict1)

# d = dict(short='dict', long='dictionary')
# d_2 = dict([(1, 1), (2, 4)])
# print(d)
# print(d_2)
# import string
#
# d = dict.fromkeys([x for x in string.ascii_lowercase], 5)
# print(d)

# d = {1: 2, 'as': 4, 3: 9}
# d[4] = 4 ** 2
# print(d)
# print(d['as'])  # вызов по имени ключа! не по индексу
# import random
# fear = input('Enter animal which you are fear the most: ')
# dict1 = dict(strong=('people', 'dogs', 'elephants', 'lions', 'wolfs', 'panther'),
#              sweet=('honey', 'marshmallow', 'icecream', 'sugar', 'lollipop'))
# # print(dict1)
# # del dict1['strong']  # удаление ключа с его элементами из словаря
# # print(dict1)
# # print(random.choice(dict1['sweet']))
# # if 'strong' in dict1:
# #     del dict1['strong']
# #     print(dict1)
# for i in dict1['strong']:
#     if i == fear:
#         del dict1['strong']
#         print(random.choice(dict1['sweet']))
#         break
# else:
#     print(random.choice(dict1['strong']))

# функция zip()

# import string
#
# num = dict(zip([x for x in string.ascii_lowercase], [i for i in range(1, 100)]))
# print(num)
# for i in num:
#     print(f'{i}: {num[i]}')

# dict1 = {'f': 10, 'a': 2, 'c': 17}
# ak = dict1.keys()
# print(ak)
# list = list(ak)
# print(list)
# list.sort()
# print(list)
# dict2 = dict(zip(list, [dict1[list[0]], dict1[list[1]], dict1[list[2]]]))
# print(dict2)
# name = input('Enter your name: ')
# age = input('Enter your age: ')
# city = input('Where are you from? ')
# person = {'name': name, 'age': age, 'city': city}
# print(f"Добрый день, {person['name']}! Вам {person['age']} лет.\nКак погодка в {person['city']}?")
#
# cars = dict(BMW=['x1', 'x2', 'x3'],
#             Tesla=['Model X', 'Model 3', 'Model S'])
# print(f"First car on BMW lib it's {cars['BMW'][0]}, last car it's {cars['BMW'][-1]}")
# print(f"First car on Tesla lib it's {cars['Tesla'][0]}, last car it's {cars['Tesla'][-1]}")
n1 = 'pythonist'
list1 = []
list2 = []
for i in n1:
    list1.append(i)
    list2.append(n1.count(i))
print(f"{list1}\n{list2}")
dict1 = dict(zip(list1, list2))
print(dict1)
