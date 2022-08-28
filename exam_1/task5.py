m = int(input('Введите число "m": '))
n = int(input('Введите число "n": '))
s = []
if m < n:
    for i in range(m, n + 1):
        if i == n:  # добавлено только для красоты.
            print(i, end='.')
        else:
            print(i, end=', ')
else:
    for i in range(n, m + 1):
        s.append(i)
    s = s[::-1]
    for x in s:
        if x == s[-1]:  # добавлено только для красоты.
            print(x, end='.')
        else:
            print(x, end=', ')