stroka = input("Пожалуйста, введите текст: ")
if type(stroka) == int or type(stroka) == float:
    print("Это число:", stroka)
else:
    print("Это текст:", stroka)