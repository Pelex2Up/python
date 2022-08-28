with open('this_file.txt', 'w') as f:
    pass
file_path = 'this_file.txt'


def add_text(path, text):
    with open(path, 'a') as f:
        f.write(text)


def open_txt(path):
    with open(path, 'r') as f:
        print(f.read())


arr = [1, 2, 'arr', 'fuzzyy', '23', 26, 'wuzz']
arr_str = []
arr_num = []
for i in arr:
    if type(i) is int:
        arr_num.append(i)
    else:
        if i.isalpha():
            arr_str.append(i)
        elif i.isdigit():
            arr_num.append(int(i))
arr_str.sort(key=len)
arr_num.sort()
print(arr_str, arr_num)
for i in arr_str:
    add_text(file_path, f'{i}, ')
add_text(file_path, '\n')
for num in arr_num:
    add_text(file_path, f'{num}, ')
open_txt(file_path)
