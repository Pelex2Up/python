s = input("Введите строку: ")
if len(s) > 0:
    print(s[2])
    print(s[-2])
    print(s[:6])
    print(s[:-2])
    print(s[::2])
    print(s[1::2]) #нечетные индексы, не знаю как убрать из них числа вроде 6, 12, 18 и т.д. (кратные и 2 и 3)
