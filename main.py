"""Описати функцію CircleS (R) дійсного типу,
яка знаходить площу круга радіуса R (R - дійсне).
За допомогою цієї функції знайти площі трьох кіл з
даними радіусами. Площа круга радіуса R обчислюється за
формулою S = π ·"""


def CircleS(R):
    return 3.14 * R * R


print('Введіть радіус першого круга: ')
r1 = float(input())
print('Площа першого круга: ')
print(CircleS(r1))

print('Введіть радіус другого круга: ')
r2 = float(input())
print('Площа другого круга: ')
print(CircleS(r2))

print('Введіть радіус третього круга: ')
r3 = float(input())
print('Площа третьго круга: ')
print(CircleS(r3))
