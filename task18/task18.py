# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# Пример:
# 5
# 1 2 3 4 5
# 6
# -> 5

import random

n = int(input("Введите количество элементов в массиве: "))
rand_massive = []
for i in range(n):
    rand_massive.append(random.randint(1, 20))
print(rand_massive)

x = int(input("Введите любое число: "))
find_num = rand_massive[0]
for i in rand_massive:
    if abs(i - x) < abs(find_num - x):
        find_num = i
print(f'Самый близкий по величине элемент к заданному числу {x} -> {find_num}')
