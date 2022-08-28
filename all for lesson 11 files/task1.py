# f = open('test_text_file.txt', 'r')
# fp = open('C:/python/all for lesson 11 files/xyz.txt', 'r+')
# f.close()
# # print(*f)
# fp.truncate()
# fp.write('\nTHis IS A SUPER TEST TEXT FILE!')
# fp.close()
# # print(*fp)
# try:
#     print(*f)
# finally:
#     f.close()
import os
file_path = 'test_text_file.txt'


def text_red(path, text):
    with open(path, 'a') as f:
        f.write(text)
        f.write('\n')


def open_txt(path):
    with open(path, 'r') as f:
        print(*f)


try:
    open_txt(file_path)
except FileNotFoundError:
    # os.rename('test_text_file.txt', 'test.txt')
    file_path = 'test.txt'
    open_txt(file_path)

print('Current directory: ', os.getcwd())  # вывод пути рабочей директории
# try:
#     os.mkdir('folder')  # создание папки в текущей директории
# except FileExistsError:
#     pass
# os.chdir('folder')  # смена рабочей директории
# print('Current directory: ', os.getcwd())
# os.chdir('..')  # возвращает в предыдущую директорию
# print('Current directory: ', os.getcwd())
# os.makedirs('nested1/nested2/nested3')  # создание вложенных директорий (папка в папке)
# os.remove('xyz.txt')  # удаление файла в текущей директории или с указанием пути (c:/dir...)
# os.rmdir('folder')  # удаление каталога
# os.removedirs('folder/dir1/dir2/dir3')  # удаление каталога со всеми вложенными каталогами
