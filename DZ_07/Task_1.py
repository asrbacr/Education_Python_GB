# 7.0[34]: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Написать функцию, которая принимает строку текста и проверяет ее ритм (по Винни-Пуху) Если ритм есть, функция возвращает True, иначе возвращает False

# Примеры/Тесты:
#     <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам") -> True
#     <function_name>("пара-ра-рам рам-пум-пупам па-ре-по-дам") -> True
#     <function_name>("пара-ра-рам рам-пуум-пупам па-ре-по-дам") -> False
#     <function_name>("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па") -> False
#     <function_name>("Пам-парам-пурум Пум-пурум-карам") -> True
# Примечание.

# Подумайте об эффективности алгоритма. Какие структуры данных будут более эффективны по скорости.
# Алгоритм должен работать так, чтобы не делать лишних проверок. Подумайте, возможно некоторые проверки не нужны.
# (*) Усложнение.

# Функция имеет параметр, который определяет, надо ли возвращать полную информацию о кол-ве гласных букв в фразах. Эта информация возвращается в виде списка словарей. Каждый элемент списка(словарь) соответствует фразе.

# Примеры/Тесты:
# 	<function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам", False) -> True
#     <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам", True) -> (True, [{'а': 4}, {'а': 4}, {'а': 4}])
#     <function_name>("пара-ра-рам рам-пум-пупам па-ре-по-дам") -> (True, [{'а': 4}, {'а': 2, 'у': 2}, {'а': 2, 'е': 0, 'о': 0}])
#     <function_name>("пара-ра-рам рам-пуум-пупам па-ре-по-дам") -> (False, [{'а': 4}, {'а': 2, 'у': 3}])
#     <function_name>("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па") -> (False, [{'а': 11}, {'у': 6, 'а': 3}])
#     <function_name>("Пам-парам-пурум Пум-пурум-карам") -> (True, [{'а': 3, 'у': 2}, {'у': 3, 'а': 2}])

text = "пара-ра-рам рам-пам-папам па-ра-па-дам"
# text = "пара-ра-рам рам-пуум-пупам па-ре-по-дам"

list_text = text.split()
res_list = []
# print(list_text)

vowels_rus = {'а','у','о','ы','и','э','я','ю','ё','е'}
# for idx in range(len(list_text)):
result_serch_text = {}
for el in list_text:
    res = 0
    for i, k in enumerate(el):
        if k in vowels_rus:
            res += 1
            result_serch_text[el] = res

print(result_serch_text)

res_sum = []
for i in result_serch_text.items():
    res_sum.append(i)

print(res_sum)

if set(res_sum) == 1:
    print(True)

# print(result_serch_text)

# print(list_text)

# vowels_rus = {'а': 0, 'у': 0, 'о': 0, 'ы': 0,
#               'и': 0, 'э': 0, 'я': 0, 'ю': 0, 'ё': 0, 'е': 0}

# # flag = True
# for el in list_text:
#     # print(f'el = {el}')
#     result_serch_text = {}
#     for idx in range(len(list_text)):
#         res = 0
#         for i, k in enumerate(el):
#             # print(f'i = {i}')
#             # print(f'k = {k}')
#             # if k in result_serch_text:
#             if k in vowels_rus.keys():
#                 # if result_serch_text[k] in
#                 res += 1
#                 # res = result_serch_text[k] + 1
#                 result_serch_text[k] = res
#                 # result_serch_text[k] = res
#     res_list.append((result_serch_text))

# print(result_serch_text)