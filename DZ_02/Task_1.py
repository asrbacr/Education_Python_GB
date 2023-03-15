# 2.1[10]: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть. 
# Количество монет и их положение (0 или 1) пользователь вводит с клавиатуры.
# Примеры/Тесты:
# Введите кол-во монет>? 5
# Положение монеты 0: 0 или 1>? 1
# ...
# 1 0 1 1 0
# Кол-во монет, чтобы перевернуть: 2

count_money = int(input('Введите кол-во монет: '))
current_position = 0
summ_negativ_money = 0

for i in range(count_money):
    current_position = int(input('Положение монеты 0: 0 или 1: '))
    if current_position == 0:
        summ_negativ_money += 1
    
print(f'Кол-во монет, чтобы перевернуть: {summ_negativ_money}')