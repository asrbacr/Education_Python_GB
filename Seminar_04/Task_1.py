# №4.1[25]. Напишите программу, которая принимает на вход строку,
# и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Примеры/Тесты:
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Input: a b c d a a a a a a a
# Output: a b c d a_1 a_2 a_3 a_4 a_5 a_6 a_7
# Строку не обязательно вводить с клавиатуры

string_ = "a b c d a a a a a a a"
new_list = string_.split(" ")
# print(new_list)
new_set = set(new_list)
dict_ = {}
dict_ = dict_.fromkeys(new_set, 0)
new_string = ""

for element in new_list:
    if dict_[element] == 0:
        new_string += f'{element} '
    else:
        new_string += f'{element}_{dict_[element]} '
    dict_[element] += 1
print(new_string)
