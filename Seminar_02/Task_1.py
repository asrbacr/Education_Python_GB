# №2.1[9]. По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while
# Примеры/Тесты:
# 5 -> Факториал 5 равен 120
# 0 -> Факториал 0 равен 1

number = 0
n = 0
result = 1

if number == 0:
    print("Факториал 0 равен 1")
else:
    while n < number:
        n += 1
        result *= n
    print(f'Факториал {number} равен {result}')

#___
while n < number and number != 0:
    n += 1
    result *= n
print(f'Факториал {number} равен {result}')

#___

number = 1
n = 1
result 1
while n <= number:
    result *= n
    n += 1
print(f'Факториал {number} равен {result}')
