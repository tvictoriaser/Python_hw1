# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

from random import randrange

list_1 = [randrange(1, 20) for i in range(int(input("Введите кол-во эл-ов 1-го набора целых чисел: ")))]
list_2 = [randrange(1, 20) for i in range(int(input("Введите кол-во эл-ов 2-го набора целых чисел: ")))]

print(list_1)
print(list_2)

set_1 = set(list_1)
set_2 = set(list_2)
set_3 = sorted(set_1.intersection(set_2))
print(f'{set_3} -> пересечение множеств')



