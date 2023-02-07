# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# Пример:
# 5 -> 1 0 1 1 0
# 2

from random import randint
coins = int(input("Введите количество монет: "))
count_0 = 0
count_1 = 0

for _ in range(coins):
    temp = randint(0, 1)
    print(temp, end=' ')
    if temp == 0:
        count_0 += 1
    else:
        count_1 += 1
print()
if count_0 < count_1:
    print(count_0)
else:
    print(count_1)

if coins == count_0 or coins == count_1:
    print('Все монетки повёрнуты одной стороной')

