# 2.2[12]: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# Примеры/Тесты:
# 4 4 -> 2 2
# 5 6 -> 2 3

summ_number = 5
proizv_number = 6

# x + y = summ_number }
# x * y = proizv_number }

# y = summ_number - x
# x * (summ_number - x) = proizv_number

# y = summ_number - x
# 1 * x ** x - summ_number * x + proizv_number = 0


Discrim = summ_number ** 2 - 4 * proizv_number
print(Discrim)

if Discrim > 0:
    x1 = (summ_number + Discrim ** 0.5) // 2
    x2 = (summ_number - Discrim ** 0.5) // 2
    print(x1, x2)