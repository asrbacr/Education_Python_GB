# №7.1[###]. Дан текстовый csv файл. Разделитель данных #.
# Каждая строка файла представляет собой запись вида ФИО
# Например:
# Иванов#Иван#Иванович
# Петров#Петр#Петрович
# Соколов#Илья#Григорьевич

# 1) Необходимо вывести эти данные на экран построчно в виде:
# Иванов Иван Иванович
# Петров Петр Петрович

# 2) записать эти данные в список вида: [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]
# [*] Усложнение. Файл находится в поддиретории data текущей директории. Сформировать путь к нему с использованием
# os.path и pathlib

from os.path import join, abspath
#----
# datapath = join(".",  "data")
# filename = join(datapath, 'data.txt' )
#----

# datapath = join(".", "Education_Python_GB")
# filename = join( datapath, 'data.txt')
# file = open(filename, mode='r', encoding='UTF-8')

# file = open('C:\Users\User\Desktop\Education\Education_Python_GB\data.txt', mode='r', encoding='UTF-8')
file = open('Education_Python_GB/data.txt', mode='r', encoding='utf-8')

list_ = [el.strip().split('#') for el in file]
print(list_)

# for el in file:
#     print(el)
# print(*list_) # Иванов Иван Иванович
# print(list_[0][0]) # И в а н о в

file.close()

