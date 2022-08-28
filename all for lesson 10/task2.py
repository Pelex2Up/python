# try:
#     a = 100 / 0
# except ZeroDivisionError:
#     a = 0
# print(a)

# my_dict = dict(a=1, b=2, c=3)
# try:
#     value = my_dict['d']
# except IndexError:
#     print('IndexError')
# except KeyError:
#     print('KeyError')
# except:
#     print('Some error in that case')
#
# my_dict = dict(a=1, b=2, c=3)
# try:
#     value = my_dict['c']
# except:
#     print('Some error')
# else:
#     print('All is ok!')
# finally:
#     print('This case would work in other situation!')

n1 = int(input('Enter 1st number: '))
n2 = int(input('Enter 2nd number: '))

try:
    result = n1 / n2
except ZeroDivisionError:
    print('Деление на ноль!')
else:
    print(result ** 2)
finally:
    print('Python лучший язык для разработки!')