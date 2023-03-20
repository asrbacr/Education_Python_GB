# №4.2[27]. Дана строка, состоящая из слов. Словом считается последовательность 
# непробельных символов идущих подряд, слова разделены одним или большим числом пробелов.
# Слово не зависит от регистра написания букв.
# Определите, сколько различных слов содержится в этом тексте.
# Примеры/Тесты:

# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. 
# So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 14

# Input: Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
# Curabitur a tellus ut arcu gravida porta eget a lacus. Curabitur ornare varius turpis, 
# ultricies mollis sem convallis in. Nunc scelerisque lacinia risus sit amet aliquam.
# Output: 31

# [*] Усложнение. Выведите кол-во слов с учетом регистра и без учета регистра

input_string_1 = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"

print(len(set(input_string_1.lower().split()))) #split() - не создаёт пустые элементы если несколько пробелов
print(len(set(input_string_1.split()))) #со звёздочкой решение

#lower() - все буквы в нижний регистр



