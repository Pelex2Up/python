# for i in range(4):
#     print(i)

# for i in range(10, 5, -3):
#     print(i)

# x = int(input("Введите трехзначное число: "))
# for i in range(x):
#     print(i)

# for i in range(15, 0, -1):
#     print(i)

# s1 = input("Введите строку: ")
# s2 = input("Введите символ: ")
# for i in s1:
#     print(s1.replace(s2,""))
#     break

# a = input('Enter string: ')
# b = input('Enter symbol: ')
# c = ''
# for i in a:
#     if i != b:
#         c += i
# print('Result:', c)

# Вводится начало, конец и шаг последовательности, нужно вывести на экран данную последовательность чисел.
# num1 = int(input('Enter 1st number: '))
# num2 = int(input('Enter last number: '))
# step = int(input('Enter step: '))
# c = ''
# for i in range(num1, num2, step):
#     c = c + str(i) + ' '
# print(c)

# for i in range(54, 9185):
#     if i % 5 == 0:
#         print(i)

# У вас есть массив, в котором его элементы – это названия блюд на ужин.
# Вам нужно перебрать этот массив и если название одного из блюд равняется тому, что вы укажете сами.
# Например, вывести сообщение: “Я не ем …” и закончить программу.
# menu = ['eggs','chicken','water','rice','fish']
# print('Today for lunch:',menu)
# hate = input('Which of these do you not like? ')
# hate = hate.lower()
# for i in menu:
#     if i == hate:
#         print("I don't like", hate)
#         print('Lunch is over')
#         break
#     elif i == 'water':
#         print("I'd like to drink", i)
#     else:
#         print("I'd like to eat", i)

# Массив чисел. Найти их сумму и произведение.
# numbers = [1, 2, 3, 4, 5]
# sum = 0
# pr = 1
# for i in numbers:
#     sum += i
#     pr *= i
# print('Сумма чисел равна: ', sum)
# print('Произведение чисел равно: ', pr)


# for i in range(1, 10):
#     for x in range(1, 10):
#         print(x * i, end = ' ')
#     print()
