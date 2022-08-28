list1 = ["hello my friend", "my name is", "house", "cat", "dog"]
list2 = []
for i in list1:
    if i.count(' ') >= 1:
        list2.append(i)
    else:
        continue
print(list2)
