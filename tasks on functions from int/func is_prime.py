# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое,
# и False - иначе.

def is_prime(arg):
    if arg > 0:
        if arg != 3 and arg != 5 and arg != 2:
            if arg % 3 == 0 or arg % 2 == 0 or arg % 5 == 0:
                return False
            else:
                return True
        else:
            return True


print(is_prime(int(input('Введите любое число и я определю простое оно или нет: '))))
