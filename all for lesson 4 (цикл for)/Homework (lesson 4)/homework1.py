pr = 1
for i in range(1,501):
    if i % 2 > 0:
        pr *= i
    else:
        continue
print('Произведение нечетных чисел от 1 до 500 равно:', pr)