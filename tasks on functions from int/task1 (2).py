import random
s = [random.randint(15, 25) for i in range(10)]
print(s)


def remove_val(listname, val):
    return [x for x in listname if x != val]


print(remove_val(s, 20))
