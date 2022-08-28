# Необходимо удалить пробелы в элементах массива.

s = [' asd sd ', ' saad', 'asd as dsss ']
s1 = []

def removeSymbol(listname, symbol):
    for x in listname:
        j = x.replace(symbol, '')
        s1.append(j)
    return s1

print(removeSymbol(s, ' '))


