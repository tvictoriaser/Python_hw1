# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


def arithmetic_seq(a1, diff, k):
    seq = [a1]
    for i in range(2, k + 1):
        seq.append(a1 + (i - 1) * diff)
    return seq


a_1 = int(input('Введите первый элемент прогрессии: '))
d = int(input('Введите разность между элементами прогрессии: '))
n = int(input('Введите количество элементов прогрессии: '))
array = arithmetic_seq(a_1, d, n)
print(array)