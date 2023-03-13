# 1.1[2]. Найдите сумму цифр трехзначного числа. Используйте f-строки чтобы оформить красивый вывод
# (**) Усложнение. Для числа произвольной разрядности добавить в вывод строку с числами, например так:
# 13579 >>> Сумма чисел числа 13579 равна 25(1 + 3 + 5 + 7 + 9)

number = 13579
temp_number = number
summa_number = 0

while temp_number > 0:
    temp_znach = temp_number % 10
    summa_number += temp_znach
    temp_number //= 10

print(f'Сумма чисел числа {number} равна {summa_number}(', end="")

temp_number = number
summa_number = 0

while temp_number > 0:
    temp_znach = temp_number % 10
    summa_number += temp_znach
    temp_number //= 10
    print(temp_znach, end="")
    if temp_number > 0:
        print(" + ", end="")

print(")")
