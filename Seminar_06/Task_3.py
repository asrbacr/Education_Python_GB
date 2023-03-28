# №6.3[43] Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу, образуют одну пару, которую необходимо посчитать.
# Напишите функцию
# Аргументы: список целых чисел
# Возвращает: кол-во пар

# Примеры/Тесты:
# <function_name>([1, 2, 3, 2, 3]) -> 2
# <function_name>([1, 2, 3, 2, 3, 3, 2, 4]) -> 6

def get_list (list_1):
    count = 0
    for i in range(len(list_1)):
        elem = list_1[i]
        for j in range(i + 1, len(list_1)):
            if elem == list_1[j]:
                count += 1
    return count

list_1 = [1, 2, 3, 2, 3, 3, 2, 4, 2, 2]  
print(get_list(list_1))   