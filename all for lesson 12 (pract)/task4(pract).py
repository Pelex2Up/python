some_str = 'hellomynameis'
arr_lit = list(some_str)
arr_num = []
for i in arr_lit:
    arr_num.append(arr_lit.count(i))
result = dict(zip(arr_lit, arr_num))
print(result)