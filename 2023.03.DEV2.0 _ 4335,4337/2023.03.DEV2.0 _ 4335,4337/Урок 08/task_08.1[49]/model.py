def create_rec(surname, name, tel, desc) -> dict:
    """
    Создание записи в виде словаря по данным
    :param surname: Фамилия
    :param name: Имя
    :param tel: Телефон
    :param desc: Описание
    :return: Запись в виде словаря
    """
    return {'surname': surname, 'name': name, 'tel': tel, 'desc': desc}


def select(phone_book: list, template: str, ) -> list:
    """
    Выбор (select) записи по заданному фильтру фамилий
    :param template: Шаблон для поиска фамилии. Ишем совпадения начиная с первой буквы
    :param phone_book: Справочник
    :return: список записей, попавших под фильтр
    """
    return [rec for rec in phone_book if rec['surname'].lower().startswith(template.lower())]


def merge(new_rec: dict, old_rec: dict) -> dict:
    """
    Соединяетс старую и новую записи, берет данные из старой записи, если  вновой это поле пустое
    :param new_rec: Новая запись (возможно с пустыми полями)
    :param old_rec: Старая запись (без пустых полей)
    :return: Запись слитая из двух
    """
    tmp_rec = new_rec.fromkeys(new_rec.keys())
    for key in new_rec.keys():
        tmp_rec[key] = new_rec[key] if new_rec[key] != "" else old_rec[key]
    return tmp_rec


def import_file(filename: str, delimiter="#") -> list:
    """
    Импорт данных из файла
    :param filename:  имя файла(текущая директория)
    :param delimiter: Разделитель полей
    :return: Список словарей(записей)
    """
    rez = []
    with open(filename, mode="r", encoding="utf-8") as file:
        for line in file:
            surname, name, tel, desc = line.strip().split(delimiter)
            rez.append({'surname': surname, 'name': name, 'tel': tel, 'desc': desc})
    return rez


def export_file(filename: str, phone_book: list, delimiter="#"):
    """
    Экспорт справочника в файл
    :param filename: имя файла(текущая директория)
    :param phone_book: Справочник(списко словарей)
    :param delimiter: Разделитель полей
    :return: None
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        for rec in phone_book:
            file.write(",".join(rec.values()))
            file.write(f"\n")


if __name__ == "__main__":
    print(import_file("phone_book1.txt"))

    phone_book_test = [
        {'surname': 'Фамилия_1', 'name': 'Имя_1', 'tel': 'Телефон_1', 'desc': 'Описание_1'},
        {'surname': 'Фамилия_2', 'name': 'Имя_2', 'tel': 'Телефон_2', 'desc': 'Описание_2'},
        {'surname': 'Фамилия_3', 'name': 'Имя_3', 'tel': 'Телефон_3', 'desc': 'Описание_3'},
        {'surname': 'Фамилия_4', 'name': 'Имя_4', 'tel': 'Телефон_4', 'desc': 'Описание_4'},
    ]

    print(export_file("phone_book2.txt", phone_book_test))
    print(import_file("phone_book2.txt"))
