import random
list_1 = [random.randint(1, 20) for x in range(10)]
list_res = []
for i in list_1:
    if list_1.count(i) > 1:
        list_res.append(i)
    else:
        continue

list_res = set(list_res)

if len(list_res) > 1:
    print(f'В списке {list_1} найдено {len(list_res)} повторений. Это числа: {list(list_res)}')
elif len(list_res) == 1:
    print(f'В списке {list_1} найдено {len(list_res)} повторение.')
else:
    print(f'В списке {list_1} не найдено повторений.')
