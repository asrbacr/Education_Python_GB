# 1.1[2]. Найдите сумму цифр трехзначного числа. Используйте f-строки чтобы оформить красивый вывод
# Например для числа 145 сумма цифр будет 10: 1 + 4 + 5
# Примеры/Тесты:
# 123 >>> Сумма чисел числа 123 равна 6
# 100 >>> Сумма чисел числа 100 равна 1

number = 1238768
temp_number = number
summa_number = 0

while temp_number > 0:
    temp_znach = temp_number % 10
    summa_number += temp_znach
    temp_number //= 10
    

print(f'Сумма чисел числа {number} равна {summa_number}')


