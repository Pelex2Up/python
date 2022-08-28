import random

x = int(input('Введите длину требуемого списка: '))
int_list = [random.randint(1, 50) for x in range(x)]
print(int_list)
