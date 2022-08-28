print('Давайте сформулируем таблицу Фибоначчи :)')
num1 = int(input('Введите первое число в таблице: '))
num2 = int(input('Введите второе число в таблице: '))
fib = []
fib.append(num1)
fib.append(num2)
for x in range(2,11):
    i1 = x - 1
    i2 = x - 2
    fib1 = fib[i1] + fib[i2]
    fib.append(fib1)
print(fib)
