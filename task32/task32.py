# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def array(x):
    list_1 = []
    for _ in range(x):
        list_1.append(int(input('Введите элемент массива: ')))
    return list_1


def index(list_2, minimum, maximum):
    index_list = []
    for i in range(len(list_2)):
        if minimum <= list_2[i] <= maximum:
            index_list.append(i)
    return index_list


size = array(int(input('Введите размер массива: ')))
min_range = int(input('Введите минимум диапазона: '))
max_range = int(input('Введите максимум диапазона: '))
find_index = index(size, min_range, max_range)
print(size)
print(find_index)
