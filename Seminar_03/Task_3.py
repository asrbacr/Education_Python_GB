# №3.3[21]. Напишите программу для печати всех уникальных значений в списке словарей.
# Примечание: Список словарей задан изначально. Пользователь его не вводит
# Обратите внимание, что в словарях может быть один или несколько элементов
# Примеры/Тесты:
# Input: [{"V": "S001", "X": "D009"}, {"V": "S002"}, {"VI": "S001"}, 
#         {"VI": "S005", "XI": "D011"}, {"VII": " S005 "}, {" V ":" S009 "}, 
#         {" VIII ":" S007 ", "XII": "D001"}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

my_list = [{"V": "S001", "X": "D009"}, 
          {"V": "S002"}, 
          {"VI": "S001"}, 
        {"VI": "S005", "XI": "D011"}, 
        {"VII": " S005 "}, 
        {" V ":" S009 "}, 
        {" VIII ":" S007 ", "XII": "D001"}
]

# my_set = set()

# for element in my_dist:
#     for elem in element.values():
#     # my_set.append(elem)
#         my_set.add(elem.strip())

# print(my_set)

# print([element for element in my_list])
# print({elem.strip(): elem.strip() for element in my_list for elem in element.values()})
