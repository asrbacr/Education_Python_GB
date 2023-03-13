# 1.3[6]. Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# Примеры/Тесты:
# 385916 >>> yes
# 123456 >>> no

number_bilet = 173456

start_number = number_bilet // 1000
end_number = number_bilet % 1000

summ_start_number = 0
while start_number > 0:
    temp_znach = start_number % 10
    summ_start_number += temp_znach
    start_number //= 10

summ_end_number = 0
while end_number > 0:
    temp_znach = end_number % 10
    summ_end_number += temp_znach
    end_number //= 10

#__финальное условие 
# if summ_start_number == summ_end_number:
#     print(f'{number_bilet} >>> yes')
# else:
#     print(f'{number_bilet} >>> no')
#__до сюда

#__через тернарный оператор
# print(number_bilet, '>>>', 'yes' if summ_start_number == summ_end_number else 'no')

# через f строку и тернарный оператор
print(f"{number_bilet} >>> {'yes' if summ_start_number == summ_end_number else 'no'}")