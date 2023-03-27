# №6.2[41] Дан список, целых чисел.
# Напишите функцию, которая определит те элементы списка, 
# у которых два соседних и, при этом, оба соседних элемента меньше данного.

# Функция
# Аргументы: список целых чисел
# Возвращает: список элементов (смотри условие)

# Примеры/Тесты:
# <function_name>([1, 3, 3, 3, 5]) -> [5]
# <function_name>([1, 5, 1, 6, 1]) -> [5,6]
# <function_name>([7, 5, 1, 6, 8]) -> [8]
# <function_name>([8, 1, 5, 4, 5]) -> [8,5]

data = [1, 5, 1, 6, 1]

def super_func(numbers: list) -> list:
    result = list()
    for idx, element in enumerate(numbers):
        prev_idx = idx - 1
        next_idx = idx + 1 if idx < len(numbers)-1 else 0
        if numbers[prev_idx] < element and numbers[next_idx] < element:
            result.append(element)
    return result

print(super_func(data))