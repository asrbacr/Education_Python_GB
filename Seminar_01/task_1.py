# №1.1[1]. За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# Реализуйте пользовательский ввод данных и вывод внятного результата.
# Используйте .format() или f-строки
# Примеры/Тесты:
# n = 700, m = 750 -> Чтобы проехать 750км машине потребуется 2дн
# n = 700, m = 600 -> Чтобы проехать 600км машине потребуется 1дн
# n = 700, m = 1400 -> Чтобы проехать 1400км машине потребуется 2дн
# Усложнение[*]. Использовать тернарный оператор

# count = int(input('Введите кол-во км за 1 день: '))
# distance = int(input('Введите кол-во км, которое нужно проехать: '))
count = 700
distance = 600

# days = -distance//count
# print(-days)

# решение
# days = 0
# if distance % count != 0:
#     days = distance // count +1
# else:
#     days = distance // count

# тернарная строка
days2 = distance//count+1 if distance % count != 0 else distance // count

print(f'Чтобы проехать {count}км машине потребуется {days2}дн')  # placeholder
print(f'Чтобы проехать {count}км машине потребуется {distance//count+1 if distance % count != 0 else distance // count}дн')

# Это норм ↓
# day_distance = int(input("Сколько машина проезжает за день: "))
# days = int(input("Сколько машина проезжает за день: "))
# print (f"машина проедет путь за {(days // day_distance) + 1} дней") if days % day_distance != 0 else print (f"машина проедет путь за  {days // day_distance} дней")

