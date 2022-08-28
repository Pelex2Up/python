# i = 0
# while i < 10:
#     print(i, end=' ')
#     if i == 5:
#         break
#     i += 1

# сумма чисел от 1 до 50

# i = 1
# result = 0
# while i <= 50:
#     result += i
#     print(result, end=" ")
#     i += 1
# print()
# print(result)

#квадраты всех целых чисел от 1 до 10

# i = 1
# q = 1
# arr = []
# while i <= 10:
#     q = i*i
#     arr.append(q)
#     i += 1
# print(arr)

# вывести числа от 1 до 15 в порядке убывания

# i = 15
# while i >= 1:
#     print(i, end=' ')
#     i -= 1

#Пользователь вводит два числа с клавиатуры, необходимо вывести на экран все отрицательные числа, лежащие между ними.
# x = int(input('Введите 1-е число: '))
# y = int(input('Введите 2-е число: '))
# if x < y and x < 0:
#     while x < 0:
#         x += 1
#         if x == 0 or x == y:
#             break
#         print(x, end=' ')
# elif y < x and y < 0:
#     while y < 0:
#         y += 1
#         if y == 0 or x == y:
#             break
#         print(y, end=' ')
# else:
#     print('Между числами нет отрицательных чисел')

# x = int(input('Enter number: '))
# for i in range(x):
#     if i == 0:
#         continue
#     print(i, end=' ')
#     if i == 15:
#         break
# else: # цикл else выполняется если цикл завершается в нормальном режиме (без break)
#     print()
#     print('Done!')

# Необходимо вывести на экран последовательность от 7 до 98 с шагом 7, не используя массив.
# Добавить эту последовательность в массив и найти его длину.
# i = 7
# q = []
# while i <= 98:
#     print(i, end=' ')
#     q.append(i)
#     i += 7
# print()
# print(q)
# print('Длина массива =',len(q), 'значений')

while True:
    num1 = float(input("Введите первое число: "))
    val = input("Введите операцию (+,-,*,/): ")
    num2 = float(input("Введите второе число: "))
    if val == '0':
        print('Ваше выражение неверно!')
        break
    elif num1 != 0 and num2 != 0:
        if val == "+":
            print("Сумма равна: ", num1 + num2)
        elif val == "-":
            print("Разность равна: ", num1 - num2)
        elif val == "*":
            print("Умножение равно: ", num1 * num2)
        elif val == "/":
            if num2 == 0:
                print('Деление на ноль')
            else:
                print("Деление равно: ", num1 / num2)