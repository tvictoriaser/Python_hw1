# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

length = int(input("Введите длину шоколадки: "))
width = int(input("Введите ширину шоколадки: "))
amount = int(input("Введите количество долек: "))
if amount & length == 0 or amount % width == 0:
    print(f'{length} {width} {amount} -> yes')
else:
    print(f'{length} {width} {amount} -> no')
