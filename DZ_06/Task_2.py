# 6.2[32]: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Напишите функцию
# - Аргументы: список чисел и границы диапазона
# - Возвращает: список индексов элементов (смотри условие)

# Примеры/Тесты:
# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# <function_name>(lst1, 2, 10) -> [1, 3, 7, 9, 10, 13, 14, 19]
# <function_name>(lst1, 2, 9) -> [1, 3, 7, 10, 13, 19]
# <function_name>(lst1, 0, 6) -> [2, 3, 6, 7, 10, 11, 16]
# (*) Усложнение. Для формирования списка внутри функции используйте Comprehension
# (*) Усложнение. Функция возвращает список кортежей вида: индекс, значение

# Примеры/Тесты:
# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# <function_name>(lst1, 2, 10) -> [(1, 9), (3, 3), (7, 4), (9, 10), (10, 2), (13, 8), (14, 10), (19, 7)]


list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_serch = 6
max_serch = 0


def serch_idx(list_1, min_serch, max_serch):
    if min_serch > max_serch:
        min_serch, max_serch = max_serch, min_serch
    new_list = []
    for i in range(len(list_1)):
        if min_serch <= list_1[i] <= max_serch:
            new_list.append(i)
    return new_list
 
def serch_idx_return_el(list_1, min_serch, max_serch):
    # min_serch = 15
    # max_serch = 12
    if min_serch > max_serch:
        min_serch, max_serch = max_serch, min_serch
    new_list = []
    new_list.append([(i, list_1(i)) for i in range(len(list_1)) if (min_serch <= list_1[i] <= max_serch)])
    # for i in range(len(list_1)):
    #     if min_serch <= list_1[i] <= max_serch:
    #         # new_list.append(i)
    return new_list

print(serch_idx_return_el(list_1, min_serch, max_serch))