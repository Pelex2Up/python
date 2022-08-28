# Написать функцию date, принимающую 3 аргумента — день, месяц и год. Вернуть True, если такая дата есть в
# нашем календаре, и False иначе.

def date():
    day = int(input('Введите день: '))
    month = int(input('Введите номер месяца: '))
    year = int(input('Введите год: '))
    thirty_days_month = [4, 6, 9, 11]
    thirtyone_days_month = [1, 3, 5, 7, 8, 10, 12]
    if day > 0 and month > 0 and year > 0:
        if day <= 31 and month <= 12 and year <= 2022:
            if year % 4 == 0 and day <= 29:
                return True
            elif month == 2 and day <= 28:
                return True
            else:
                def max_month_days():
                    if month in thirty_days_month:
                        return 30
                    elif month in thirtyone_days_month:
                        return 31
                    else:
                        return 28
                max_days = max_month_days()
                if day <= max_days:
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False

print(date())