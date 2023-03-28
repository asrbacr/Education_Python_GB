# 6.1[30]: Напишите программу, генерирующую элементы арифметической прогрессии
# Программа принимает от пользователя три числа:

# Первый элемент прогрессии, Разность (шаг) и Количество элементов
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

# Напишите функцию
# - Аргументы: три указанных параметра
# - Возвращает: список элементов арифмитической прогрессии.

# Примеры/Тесты:
# Ввод: 7 2 5
# Вывод: [7 9 11 13 15]
# Ввод: 2 3 12
# Вывод: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]

# (*) Усложнение. Для формирования списка внутри функции используйте Comprehension
# (**) Усложнение. Присвоение значений переменным a1,d,n запишите, 
# используя только один input, в одну строку, вам понадобится распаковка и Comprehension или map

temp = input('Введите 3 числа по маске\nНачальное_значение Шаг Сколько_элементов\n')
input_user = int(temp.strip(" "))
print(input_user)
# input_user = [7, 2, 5]
# start_progression = 7
# step_progression = 2
# count_progression = 5
# start_progression, step_progression, count_progression = input_user

def summ_progression(start_progression, step_progression, count_progression):
    list_progression = []
    i = 0
    while i < count_progression:
        list_progression.append(start_progression)
        start_progression += step_progression
        i += 1
    return list_progression

# print(summ_progression(start_progression, step_progression, count_progression))