# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

ticket_Number = int(input("Введите шестизначный номер билета: "))
sum_First = ticket_Number // 100000 + ticket_Number // 10000 % 10 + ticket_Number // 1000 % 10
sum_Second = ticket_Number // 100 % 10 + ticket_Number // 10 % 10 + ticket_Number % 10
if sum_First == sum_Second:
    print(f'{ticket_Number} -> yes')
else:
    print(f'{ticket_Number} -> no')