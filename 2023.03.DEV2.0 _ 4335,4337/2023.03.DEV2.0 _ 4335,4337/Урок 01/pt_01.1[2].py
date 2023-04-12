"""
Найдите сумму цифр трехзначного числа. Используйте f-строки чтобы оформить красивый вывод
Например для числа 145 сумма цифр будет 10: 1 + 4 + 5
Примеры/Тесты:
123 >>> Сумма чисел числа 123 равна 6
100 >>> Сумма чисел числа 100 равна 1
Усложнение [*] Решите для числа произвольной разрядности: произвольное количество цифр в числе.
Усложнение [**] Для числа произвольной разрядности добавить в вывод строку с числами, например так
13579 >>> Сумма чисел числа 13579 равна 25(1 + 3 + 5 + 7 + 9)
Для этого используйте конкатенацию строк и срезы
"""

# Основной вариант решения: трехзначное число
num = 100
d1 = num % 10
d2 = num // 10 % 10
d3 = num // 100 % 10
print(f"Сумма чисел числа {num} равна {d1 + d2 + d3}")

# [*]
num = 13579
num_copy = num
# Для числа произволной разрядности
str1 = ""
sum_digit = 0
while True:
    d = num % 10
    num //= 10
    str1 += f"{d} + "
    sum_digit += d
    if num == 0: break
str1 = str1[::-1][3:]
print(f"Сумма чисел числа {num_copy} равна {sum_digit}: {str1}")
# [Вопрос] Вложенный вызов функций

# [ADD] Использование функции
