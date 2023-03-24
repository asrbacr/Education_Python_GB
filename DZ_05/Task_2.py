# 5.2[28]: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(0,0) -> 0
# <function_name>(0,2) -> 2
# <function_name>(3,0) -> 3

def Summ_number(num_one, num_two):
    if num_two == 0:
        return num_one
    return Summ_number(num_one + 1, num_two - 1)


print(Summ_number(3, 4))

