# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
# и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).

def season(month):
    if month > 0:
        if month <= 2 or month == 12:
            month = 'Зима'
            return month
        elif month >= 3 and month <= 5:
            month = 'Весна'
            return month
        elif month >= 6 and month <= 8:
            month = 'Лето'
            return month
        elif month >= 9 and month <= 11:
            month = 'Осень'
            return month
    else:
        return 'Отрицательный месяц'

print(season(11))