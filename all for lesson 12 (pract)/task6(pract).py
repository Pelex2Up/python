import random
list_1 = [random.randint(1,10) for x in range(10)]
list_2 = [random.randint(1,10) for y in range(10)]
print(list_1)
print(list_2)
result = set(list_1) & set(list_2)
print(f'Количество повторяемых чисел: {len(result)}. Эти числа: {list(result)}')
