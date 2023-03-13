# №1.2[3]. В некоторой школе решили набрать три новых математических класса
# и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся.
# Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.
# Примеры/Тесты:
# 20 21 22(ввод чисел НЕ в одну строку) -> Общее кол-во парт будет 32
# 21 21 21(ввод чисел НЕ в одну строку) -> Общее кол-во парт будет 33

# class1 = 20
# class2 = 21
# class3 = 22
# class1 = int(input('Введите кол-во учеников в 1 классе: '))
# class2 = int(input('Введите кол-во учеников в 2 классе: '))
# class3 = int(input('Введите кол-во учеников в 3 классе: '))

# countDesk1 = class1 // 2 if class1 % 2 == 0 else class1 // 2 + 1
# countDesk2 = class2 // 2 if class2 % 2 == 0 else class2 // 2 + 1
# countDesk3 = class3 // 2 if class3 % 2 == 0 else class3 // 2 + 1

# print (f'Общее кол-во парт будет: {countDesk1 + countDesk1 + countDesk3}')

count_desk = 0
for class_number in range(3):
    childs = int(input(f'Введите кол-во учеников в {class_number + 1} классе: '))
    count_desk += childs // 2 if childs % 2 == 0 else childs // 2 + 1
print(f'Общее кол-во парт будет: {count_desk}')