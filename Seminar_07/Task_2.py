# №7.2[###]. Продолжение предыдущей задачи
# Данные в списке [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]
# необходимо преобразовать к виду:
# Иванов И.И.
# Петров П.П.
# Полученные строки записать в новый файл. Файл должен находиться в поддиретории rezults.
# [*] Усложнение. Данные необходимо записать в два разных файла:
# В первый - в виде Иванов И.И.
# Во второй - в виде Иванов-И-И
# [*****] Усложнение. Вам известно, что (в перспективе) подобных спецификаций может быть много. Не две, а пять или десять
# Как улучшить свой код в этом случае, сделать его легко расширяемым?

from os.path import join


datapath = join(".", "task_7.2_data")

with open(join(datapath, "task_7.2_data.csv"), mode="r", encoding="utf-8") as data_file:
    data = [line.strip().split("#") for line in data_file]

# new_data2 = [f"{fio[0]} {fio[1][0]}.{fio[2][0]}." for fio in data]
new_data2 = [f"{surname} {name[0]}.{parent[0]}." for surname, name, parent in data]

print(*new_data2, sep="\n")

# Полученные строки записать в новый файл. Файл должен находиться в поддиретории rezults.
with open(join(datapath, "result", "new_task_7.2_data.csv"), mode="w", encoding="utf-8") as data_file:
    [data_file.write(el+"\n") for el in new_data2]