import string
list_alpha = list(x for x in string.ascii_lowercase)
list_num = list(x for x in range(1,27))
result = dict(zip(list_alpha, list_num))
print(result)