# №5.3[35]. Напишите функцию, которая принимает число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя нацело: 1 и само число
# Если число простое - функция возвращает True, если нет - возвращает False

# Примеры/Тесты:
# <function_name>(13) -> True
# <function_name>(10) -> False

def plain_num(number:int) -> bool:   #Тут используется анотация типа что number должен быть int, а bool - это return
    if not isinstance(number, int): return None
    for divider in range(2, number):
        if number % divider == 0:
            return False
    return True

print(plain_num(1))
print(plain_num("jdshgsjhdgf"))

