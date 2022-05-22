"""Описати функцію Mean (X, Y, AMean, GMean),
яка обчислює середнє арифметичне AMean = (X + Y) / 2 і
середнє геометричне GMean = (X · Y) 1/2 двох позитивних чисел
X і Y (X і Y - вхідні , AMean і GMean - вихідні параметри дійсного
типу). За допомогою цієї функції знайти середнє арифметичне і
середнє геометричне для пар (A, B), (A, C), (A, D),
якщо дані A, B, C, D."""


import math


def AMean(X, Y):
    return (X + Y) / 2


def GMean(X, Y):
    return math.sqrt(X * Y)


print('A: ')
A = float(input())
print('B: ')
B = float(input())
print('C: ')
C = float(input())
print('D: ')
D = float(input())

print(AMean(A, B), ' ', GMean(A, B))

print(AMean(A, C), ' ', GMean(A, C))

print(AMean(A, D), ' ', GMean(A, D))
