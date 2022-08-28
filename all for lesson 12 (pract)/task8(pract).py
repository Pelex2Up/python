some_dict = dict(some_key1=1,
                 some_key2=2,
                 some_key3=10,
                 some_key4=13,
                 some_key5=4,
                 some_key6=5)
pr = 1
for i in some_dict:
    pr *= some_dict[i]
print(pr)