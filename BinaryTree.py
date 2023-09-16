# Задание: 
#    1) Добавить подсчет количества элементов, 
#    2) Вывод всего дерева на экран, 
#    3) Удаление элемента.
#    4) Документация кода

from numbers import Number
from types import NoneType


class Node:
    '''
    Класс Node
    
    Методы:
        __init__ - конструктор
        __str__ - значение узла и листьев
        __lt__ и __gt__ - проверка возможности сравнения элементов
    '''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        res = f'Значение нашего узла: {self.value}'
        if self.left:
            res += f' значение левого: {self.left.value}'
        if self.right:
            res += f' значение правого: {self.right.value}'
        return res
    
    def __lt__(self, other) -> bool:
        if not isinstance(other, type(self)):
            raise TypeError(f"Невозможно сравнить {type(self).__name__} и {type(other).__name__} элемент")
        return self.value.__lt__(other.value)

    def __gt__(self, other) -> bool:
        if not isinstance(other, type(self)):
            raise TypeError(f"Невозможно сравнить {type(self).__name__} и {type(other).__name__} элемент")
        return self.value.__gt__(other.value)



class Binary_tree:
    '''
    Класс BinaryTree.
    Реализует Бинарное дерево

    Атрибуты:
        _allowed_types_: tuple[object]
          Управление тем, какие объекты разрешено хранить внутри элементов дерева
          Объекты должны реализовывать как минимум методы __lt__ и __gt__.

    Методы:
        __init__(root: _allowed_types_ | NoneType = None)
          Конструктор, создает пустое дерево, или устанавливает корневой элемент как Node, или создает корневой элемент с $root в качестве значения
        add(value: _allowed_types_) -> None
          Добавляет элементы в дерево. Проверяет тип значения на соответствие _allowed_types_.
        remove(value: _allowed_types_) -> None
          Поиск элемента в дереве по $value и его удаление
        search(value: _allowed_types_) -> Node | None
          Поиск элемента в дереве и возврат его или None
        print(node: Node | None = None, filter_none: bool = False) -> None
          Выводит дерево, начиная с $node или tree.root
          Если задан фильтр $filter_none, то все значения 'None' маскируются под пустые элементы
        __len__: позволяет использовать встроенную функцию len() над объектом
    '''
    _allowed_types_ = (Node, Number)

    def __init__(self, root: object | None = None):
            if isinstance(root, (Node, NoneType)):
                # TODO: проверяет тип значения узла на соответствие self._allowed_types_ ?
                self.root = root
            else:
                self.root = None
                self.add(root)

    def __len__(self):
        """
        повторное использование метода _get_as_rows_ и подсчет непустых элементов
        """
        return len([True for row in self._get_as_rows_(self.root) for el in row if el is not None])

    def add(self, value: _allowed_types_) -> None:
        """
        Добавляет элементы в дерево. Проверяет тип значения на соответствие _allowed_types_

        Параметры:
            value: добавляет значение

        Возвращает ошибки:
            TypeError: не правильный тип значения
            ValueError: узел с таким значением уже есть в дереве
        """
        if not isinstance(value, self._allowed_types_):
            allowed_type_names = [t.__name__ for t in self._allowed_types_]
            raise TypeError(f"Для значения ожидался один из типов {allowed_type_names}, получено {type(value).__name__}")
        node, parent = self._search_(value, self.root)
        if node is None:
            el = Node(value)
            if parent is None:
                self.root = el
            else:
                if value < parent.value:
                    parent.left = el
                else:
                    parent.right = el
        else:
            raise ValueError(f"Элемент со значением {value} уже существует в дереве")

    def remove(self, value: _allowed_types_) -> None:
        """
        Поиск элесмента в дереве по значения $value и его удаления

        Параметры:
            value: Значение для удаления

        Возвращает ошибки:
            ValueError: Узел со значением не существует в дереве
        """
        node, parent = self._search_(value, self.root)
        if node:
            if node.left is None and node.right is None:
                new_child = None
            elif node.left and node.right:
                right_min_node, right_min_node_parent = self._min_(node)
                right_min_node_parent.left = None
                right_min_node.left = node.left
                right_min_node.right = node.right
                new_child = right_min_node
            else:
                new_child = node.left if node.left else node.right
            if node.value < parent.value:
                parent.left = new_child
            else:
                parent.right = new_child
        else:
            raise IndexError(f"Невозможно удалить значение {value}, которого нет в дереве.")

    def _search_(self, value: _allowed_types_,
                 node: Node,
                 parent: Node | None = None) -> tuple[Node | None, Node | None]:
        """
        Метод внутреннего поиска
        Поиск узла с $value и его родителя
        Поиск начинается с узла $node

        Параметры:
            value: Значение для поиска
            node: с какого узла начинается поиск
            parent(optional): указывает на родителя текущего узла, используется для целей рекурсии
        """
        if node is None or node.value == value:
            return node, parent
        if value < node.value:
            return self._search_(value, node.left, node)
        else:
            return self._search_(value, node.right, node)

    def search(self, value: _allowed_types_) -> Node | None:
        """
        Поиск элемента в дереве и возврат его или None
        Поиск всегда начинается с корня дерева

        Параметры:
            value: Значение для поиска
        """
        return self._search_(value, self.root)[0]

    @staticmethod
    def _get_as_rows_(node: Node) -> list[list[_allowed_types_]]:
        """
        Представление дерева в виде строк
        Включая элементы None

        Параметры:
            node: с какого узла начинать
        """
        result = list()
        if node is not None:
            next_row = [node.left, node.right]
            result.append([node])
            while len([el for el in next_row if el is not None]) > 0:
                curr_row = next_row
                next_row = list()
                row_data = list()
                for el in curr_row:
                    row_data.append(el)
                    if el:
                        next_row.append(el.left)
                        next_row.append(el.right)
                    else:
                        next_row.append(None)
                        next_row.append(None)
                result.append(row_data)
        return result

    def print(self, node: Node | None = None, filter_none: bool = False) -> None:
        """
        Вывести дерево, начиная с $node или корня дерева
        Если установлен фильтр $filter_none, то все значения 'None' маскируются под пустые элементы

         Параметры:
            node(optional): с какого узла начинать поиск, если не задано, то используется корень дерева
            filter_none(optional): маскирует все значения 'None' под пустые элементы, если установлено
        """
        if not node:
            node = self.root
        tree_rows = self._get_as_rows_(node)
        if filter_none:
            tree_rows = [[el if el is not None else ' ' for el in row] for row in tree_rows]
        longest_row_len = max((len(row) for row in tree_rows), default=0)
        longest_el_size = max((len(str(el)) for row in tree_rows for el in row), default=0)+1
        for row in tree_rows:
            print(''.join(str(el).center(longest_el_size*longest_row_len//len(row)) for el in row))
    
# -------

elements = [5, 10, 15, 3, 4, 7, 39, 2, 1]

bt = Binary_tree()
for el in elements:
    bt.add(el)


print(bt.search(15))
bt.print()
