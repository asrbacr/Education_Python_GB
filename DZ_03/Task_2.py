# 3.2[18]: Требуется найти в списке целых чисел самый близкий
# по величине элемент к заданному числу X.
# Пользователь вводит это число с клавиатуры, список можно считать заданным.
# Введенное число не обязательно содержится в списке.
# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9
# Output: 10

elements = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8, 6]
# elements = [1, 2, 3, 4, 6, 7, 8, 9, 10]

serch_number = int(input('Введите число для поиска в списке\nX = '))
near_number = len(elements) # спросить на семинаре про начальное значение
near_index = 0

if elements.count(serch_number) == 0:
    for i in range(len(elements)):
        if serch_number < elements[i]:
            difference = elements[i] - serch_number
            if near_number > difference:
                near_number = difference
                near_index = i

print(f'Ближайший больший к {serch_number} это {elements[near_index]}' if elements.count(serch_number) == 0 else f'Число {serch_number} есть в списке')
