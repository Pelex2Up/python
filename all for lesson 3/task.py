# while True:
#     name = input("Как Вас зовут? ")
#     name = name.title()
#     if len(name) > 1:
#         print("Привет,", name)
#         print(name * 3)
#         break
#     else:
#         print("Вы не сказали как к Вам обращаться :(")


# while True:
#     s = input("Введите трехзначное число: ")
#     if len(s) == 3:
#         sum = int(s[0]) + int(s[1]) + int(s[2])
#         print('Сумма цифр числа равна:', sum)
#         break
#     else:
#         print("Вы ввели не трехзначное число")

while True:
    s = input("Введите строку: ")
    if len(s) > 0:
        n = s.replace(' ', '')
        print(n[::3])
        print(s[0] + s[-1])
        print(s.upper())
        print(s[::-1])
        if n.isdigit():
            print(n.isdigit())
        else:
            print(n.isdigit())
        if n == n[::-1]:
            print("Данная строка является палиндромом")
        else:
            print("Данная строка не является палиндромом")
        break
    else:
        print('Вы не ввели строку!')
