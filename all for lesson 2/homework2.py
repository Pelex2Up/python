a = float(input("Введите длину первой стороны треугольника: "))
b = float(input("Введите длину второй стороны треугольника: "))
c = float(input("Введите длину третьей стороны треугольника: "))
sum1 = a + b
sum2 = b + c
sum3 = a + c
pif1 = bool(c**2 == a**2 + b**2)
pif2 = bool(a**2 == c**2 + b**2)
pif3 = bool(b**2 == c**2 + a**2)
if sum1 > c and sum2 > a and sum3 > b:
    if a == b == c:
        print("Данный треугольник является равносторонним")
    elif a == b or b == c or a == c:
        print("Данный треугольник является равнобедренным")
    elif pif1 == True or pif2 == True or pif3 == True:
        if a != b and b != c and a != c:
            print("Это разносторонний прямоугольный треугольник")
        else:
            print("Данный треугольник является прямоугольным")
    elif a != b and b != c and a != c:
        print("Это разносторонний треугольник")
else:
    print("Невозможно построить такой треугольник")