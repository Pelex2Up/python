for i in range(1, 51):
    if i == 35:
        continue
    else:
        if i == 50:  # добавлено только для красоты.
            print(i, end='.')
        else:
            print(i, end=', ')