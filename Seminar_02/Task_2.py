# №2.2[11]. Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.
# Примеры/Тесты:
# 5 -> в ряду Фибоначчи 5 имеет порядковый номер 6

# a = int(input('Введите число: '))
number = 21
if number == 0:
    print(f'{number} - 1')
prev = 1
cur = 0

flag = False
for i in range(number):
    # c, b = b, c + b
    temp = cur
    cur = cur + prev
    prev = temp
    # print(c, end=" ")
    if number == cur:
        print(f' в ряду Фибоначчи {number} имеет порядковый номер {i + 3}')
        flag = True
        break
if not flag:
    print('-1')
    # else:
    #     print('-1')

# a = 5
# b = 1
# c = 0
# for i in range(a + 1):
#     (c, b) = (b, c + b)
#     # print(c, end = ' ')

# print(f'{c} является {i} числом')

# ___это с раздающего
number = 0
#int(input('Введите исло: ')) 
if number == 0:
    print(f'{number} - 1')
else:
    prev = 0
    cur = 1
    #flag = False
    for i in range(number):
        tmp = cur
        cur=cur+prev
        prev = tmp
        #c, b = b, c+b
        #print(, end=' ')
        if number == cur:
            print(f'{number} является {i+3} числом')
            # flag = True 
            break
    # if not flag:
    #     print('-1')
    #     # if cur > number:
    #     #     print('-1')
    #     #     break;


    else:
        print('-1')