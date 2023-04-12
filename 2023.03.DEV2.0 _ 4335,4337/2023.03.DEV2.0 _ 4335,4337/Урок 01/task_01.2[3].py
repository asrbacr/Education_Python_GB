"""
В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
Выведите наименьшее число парт, которое нужно приобрести для них.
Примеры/Тесты:
20 21 22(ввод чисел НЕ в одну строку)  >>> Общее кол-во парт будет 32
21 21 21(ввод чисел НЕ в одну строку)  >>> Общее кол-во парт будет 33
"""

# Основной вариант решения
man1, man2, man3 = 21, 21, 21
# [ADD] Используем тернарный оператор
count1 = man1 // 2 if man1 % 2 == 0 else man1 // 2 + 1
count2 = man2 // 2 if man2 % 2 == 0 else man2 // 2 + 1
count3 = man3 // 2 if man3 % 2 == 0 else man3 // 2 + 1

print(f"Общее кол-во парт будет {count1 + count2 + count3}")
