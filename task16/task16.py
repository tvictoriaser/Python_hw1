# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример:
# 5
# 1 2 3 4 5
# 3
# -> 1
import random

n = int(input("Введите количество элементов в массиве: "))
rand_massive = []
for i in range(n):
    rand_massive.append(random.randint(1, 10))
print(rand_massive)

x = int(input("Введите любое число: "))
count = 0
for i in range(len(rand_massive)):
    if x == rand_massive[i]:
        count += 1
print(f' Число {x} встречается {count} раз')


