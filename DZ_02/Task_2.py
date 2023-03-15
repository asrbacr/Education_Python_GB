# 2.2[12]: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

# Примеры/Тесты:
# 4 4 -> 2 2
# 5 6 -> 2 3

summ_number = 374
proizv_number = 9048

Discrim = summ_number ** 2 - 4 * proizv_number

if Discrim > 0:
    x1 = int((summ_number + (Discrim ** 0.5)) // 2)
    x2 = int((summ_number - (Discrim ** 0.5)) // 2)
    y1 = summ_number - x1
    y2 = summ_number - x2

    if x1 == y2 and x2 == y1:
        print(f'Задуманы числа {x1} и {y1}')
    else:
        print('Решений нет')

elif Discrim == 0:
    x = int((summ_number + Discrim ** 0.5) // 2)
    y = summ_number - x
    print(f'Задуманы числа {x} и {y}')
else:
    print('Решений нет')
