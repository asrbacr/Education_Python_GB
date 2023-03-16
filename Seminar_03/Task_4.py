# №3.4[23]. Дан список, состоящий из целых чисел. Напишите программу, 
# которая сформирует список из тех элементов, которые больше предыдущего 
# (элемента с предыдущим номером)
# Примечание: Пользователь может вводить значения списка или список задан изначально.
# Примеры/Тесты:
# Input: [0, -1, 5, 2, 1]
# Output: [5]
# Input: [-2, -1, 5, 2, 3]
# Output: [-1, 5, 3]
# [*] Усложнение: Запишите алгоритм в одну строку, используйте Comprehension

element = [-2, -1, 5, 2, 3]

# max_element = []
# for index in range(len(element)):
#     if element[index] > element[index - 1]:
#         max_element.append(element[index])
# print(max_element)

print([element[index] for index in range(len(element)) if element[index] > element[index -1]])
# print([тут записывается тело цикла] for index in range(len(element)) if element[index] > element[index -1]])
# может быть и тернарный оператор