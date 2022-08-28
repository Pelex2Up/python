# Учитывая строку, заменить каждую букву ее позицией в алфавите.
# Если что-то в тексте не является буквой, игнорируйте это.
import string

a_str = "The sunset sets at twelve o'clock."
a_str = a_str.lower()
arr = dict(zip([x for x in string.ascii_lowercase], [x for x in range(1, 100)]))
str1 = str()
for i in a_str:
    if i in arr:
        j = str(arr[i])
        str1 += ' ' + j
    else:
        continue
print(f'"{str1.lstrip()}"')