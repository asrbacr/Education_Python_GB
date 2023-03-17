# 3.2[18]: Требуется найти в списке целых чисел самый близкий 
# по величине элемент к заданному числу X. 
# Пользователь вводит это число с клавиатуры, список можно считать заданным. 
# Введенное число не обязательно содержится в списке.
# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9
# Output: 10

elements = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
serch_number = 9
summ_serch = 0
near_number = 0 
index = 0

for i in range(len(elements)):
    if elements[i] == serch_number:
        summ_serch += 1

if summ_serch == 0:
    for i in elements:# range(len(elements)):
        if serch_number > elements[i]:
            print(elements[i])
            temp = elements[i] - serch_number # 1
            print(temp)
            index = i  
            print(index)                       # 0

        # else:


print(elements[index])