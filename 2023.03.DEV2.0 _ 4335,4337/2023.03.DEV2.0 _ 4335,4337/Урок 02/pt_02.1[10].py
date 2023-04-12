"""
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть. Количество монет и их положение (0 или 1) пользователь вводит с клавиатуры.

    Примеры/Тесты:
    Введите кол-во монет>? 5
    Положение монеты 0: 0 или 1>? 1
    ...
    1 0 1 1 0
    Кол-во монет, чтобы перевернуть: 2
"""

# Основной вариант решения
count = int(input("Введите кол-во монет"))
pos0 = 0
pos1 = 0
for i in range(count):
    pos = int(input(f"Положение монеты {i}: 0 или 1"))
    if pos == 0:
        pos0 +=1
    else:
        pos1 +=1
print(f"Кол-во монет, чтобы перевернуть: {min(pos0, pos1)} ")


