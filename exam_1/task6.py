name_str = input('Введите имя и фамилию через пробел: ')
name_str = name_str.split(' ')
name_str = name_str[::-1]
name_str = ' '.join(name_str)
print('Ваши фамилия и имя: ',name_str)