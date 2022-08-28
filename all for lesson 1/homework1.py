import random
num1 = random.randint(100, 999)
print("Случайно сгенерированное число:", num1)
summa = 0
while num1 > 0:
    num2 = num1 % 10
    summa += num2
    num1 = num1 // 10
print("Сумма цифр данного числа равняется:", summa)
