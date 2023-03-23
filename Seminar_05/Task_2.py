# №5.2[33]. Хакер Василий получил доступ к классному журналу 
# и хочет заменить все свои минимальные оценки на максимальные.
# Напишите функцию, которая заменяет оценки, переданные в виде списка, 
# но наоборот: все максимальные – на минимальные.
# Функция должна возвращать новый список оценок

# Примечание: Обратите внимание на side effects функции.

# Примеры/Тесты:
# <function_name>([1, 3, 3, 3, 4, 2, 5, 5, 2]) -> [1, 3, 3, 3, 4, 2, 1, 1, 2]

# [*] Усложненение: Если ни одна оценка не была заменена, функция должна вернуть None
# Примеры/Тесты:
# <function_name>([3, 3, 3, 3, 3, 3, 3, 3, 3]) -> None

# [**] Усложненение: Добавьте параметр в функцию, который определит как будут заменены оценки:
# Друзьям минимальные на максимальные, Врагам - наоборот.
# Примеры/Тесты:
# grades = [1, 3, 3, 3, 4, 2, 5, 5, 2]
# <function_name>(grades, "friend") -> [5, 3, 3, 3, 4, 2, 5, 5, 2]
# <function_name>(grades, "enemy") -> [1, 3, 3, 3, 4, 2, 1, 1, 2]



def change (grades):
    min_grades = min(grades)
    max_grades = max(grades)
    grades_new = []
    for i in grades:
        if i == max_grades:
            grades_new.append(min_grades)
        else:
            grades_new.append(i)
    return grades_new

def change_copy (grades):
    tmp_list = grades.copy()
    min_grades = min(tmp_list)
    max_grades = max(tmp_list)
    if min_grades == max_grades:
        return None
    for i in range(len(tmp_list)):
        if tmp_list[i] == max_grades:
             tmp_list[i] = min_grades
    return tmp_list

list_1 = [1, 3, 3, 3, 4, 2, 5, 5, 2]

print(list_1)
print(change_copy(list_1))
print(list_1)