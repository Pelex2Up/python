inp = input('Введите строку со словами и числами через пробел или " _ ": ')
sum = 0
if len(inp.split('_')) > len(inp.split(' ')):
    arr = inp.split('_')
    for i in arr:
        if i.isdigit():
            i = int(i)
            sum += i
        else:
            continue
else:
    arr = inp.split(' ')
    for i in arr:
        if i.isdigit():
            i = int(i)
            sum += i
        else:
            continue
print(sum)