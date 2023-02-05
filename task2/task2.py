# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

three_Digit_Number = int(input("Введите трёхзначное число: "))
if 99 < three_Digit_Number < 1000:
    sum_Numbers = three_Digit_Number // 100 + (three_Digit_Number // 10 % 10) + three_Digit_Number % 10
    print(f'{three_Digit_Number} -> {sum_Numbers}')
else:
    print('Вы ввели неверное число')

