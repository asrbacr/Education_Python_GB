# замер скорости - это разница между t2 и t1
from time import perf_counter
from random import randint


def funk_set(list1, list2):
    t1 = perf_counter()
    rez = list(set(list1).difference(set(list2)))
    t2 = perf_counter()
    return rez, t2 - t1


def funk_list(list1, list2):
    t1 = perf_counter()
    new_list = list()
    for i in list1:
        if i not in list2 and i not in new_list:
            new_list.append(i)
    t2 = perf_counter()
    return new_list, t2 - t1


n = 10000
lst1 = [randint(0, int(n)) for _ in range(n)]
lst2 = [randint(0, int(n)) for _ in range(n)]

print(funk_set(lst1, lst2)[1])
print(funk_list(lst1, lst2)[1])