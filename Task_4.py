# №64.4[45] Два различных натуральных числа n и m называются дружественными, 
# если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот.
# Например, 220 и 284 – дружественные числа.
# 220: 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110, — их сумма равна 284.
# 284: 1, 2, 4, 71 и 142, — их сумма равна 220.
# Первые пары дружественных чисел:
# 220, 284; 1184, 1210; 2620, 2924; 5020, 5564; 6232, 6368

# Для заданного числа number выведите все пары дружественных чисел, каждое из которых не превосходит number.
# Напишите функцию:
# Аргументы: целое число
# Печатает все пары дружественных чисел, не превосходящих аргумент.
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
# Примечание:
# 1. Выделите значимые куски алгоритма и оформите их в виде функций
# 2. Задокументируйте созданные функции
# 3. Используйте type hinting

# Примеры/Тесты:
# <function_name>(300)
# 220 284

# <function_name>(10000)
# 220 284
# 1184 1210
# 2620 2924
# 5020 5564
# 6232 6368

def get_dividers(number: int): # -> list:
    return (x for x in range(1, (number // 2) + 1) if number % x == 0)
    # result = list()
    # i = 1
    # while i <= number // 2:
    #     if number % i == 0:
    #         result.append(i)
    #     i += 1
    # return result

# print(get_dividers(220), sum(get_dividers(220)))
# print(get_dividers(284), sum(get_dividers(284)))
print(sum(get_dividers(220)))
print(sum(get_dividers(284)))


# input_number = 10000
# j = 0

# while j < input_number:
#     pair_number = sum(get_dividers(j))
#     if pair_number < input_number and j == sum(get_dividers(pair_number)) and j < pair_number:
#         print(j, sum(get_dividers(j)))
#     j += 1

# ------ код из чата ↓

def get_dividers(number: int):
    """
    Красивое описание функции 
    :param number: int
    :return: generator
    """
    return (x for x in range(1, (number // 2) + 1) if number % x == 0)

input_number = 10000

j = 1
while j < input_number:
    pair_number = sum(get_dividers(j))
    if pair_number < input_number and j == sum(get_dividers(pair_number)) and j < pair_number:
        print(j, sum(get_dividers(j)))
    j += 1