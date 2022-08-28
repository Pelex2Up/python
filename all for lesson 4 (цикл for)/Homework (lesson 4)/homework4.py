arr = [5, 2, 3, 4, 5, 6, 7, 8, 2, 6]
arr2 = []
for i in arr:
    if arr.count(i) >= 2:
        arr2.append(i)
print(arr2)