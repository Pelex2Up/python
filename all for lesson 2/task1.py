# num1 = int(input("Введите целое число: "))
# if num1 % 2 == 0 and num1 != 0:
#     print("Вы ввели четное число")
# elif num1 == 0:
#     print("Вы ввели ноль")
# else:
#     print("Число нечетное")

# c = bool(False)
# if not c:
#     print("Not")

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))
print("")
if num1 > num2 and num1 > num3:
    print("Первое число наибольшее", num1)
elif num2 > num1 and num2 > num3:
    print("Второе число наибольшее", num2)
else:
    print("Третье число наибольшее", num3)