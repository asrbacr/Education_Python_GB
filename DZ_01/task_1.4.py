# 1.4[8]. Требуется определить,
# можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# Примеры/Тесты:
# 3 2 4 -> yes
# 3 2 1 -> no

count_line = 3
count_colums = 2
lobule = 400

if lobule < count_colums * count_line:
    print(f"{count_line} {count_colums} {lobule} -> {'yes' if lobule % count_line == 0 or lobule % count_colums == 0 else 'no'}")
else:
    print(f'Нет {lobule} долек в шоколадке размером {count_line} на {count_colums}')
