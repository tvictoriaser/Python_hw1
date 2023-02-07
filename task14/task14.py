# Требуется вывести все целые степени двойки (т.е. числа вида 2**k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

n = int(input("Введите число: "))
numbers = 1
while numbers <= n:
    print(numbers, end=' ')
    numbers = 2 * numbers

