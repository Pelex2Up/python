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

